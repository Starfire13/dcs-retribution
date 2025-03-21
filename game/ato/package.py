from __future__ import annotations

import logging
from collections import defaultdict
from copy import deepcopy
from datetime import datetime
from typing import Dict, Optional, TYPE_CHECKING

from game.db import Database
from game.utils import Speed
from .closestairfields import ObjectiveDistanceCache
from .flight import Flight
from .flightplans.formation import FormationFlightPlan
from .flighttype import FlightType
from .packagewaypoints import PackageWaypoints
from .traveltime import TotEstimator
from ..radio.RadioFrequencyContainer import RadioFrequencyContainer
from ..radio.radios import RadioFrequency

if TYPE_CHECKING:
    from game.theater import ControlPoint, MissionTarget


class Package(RadioFrequencyContainer):
    """A mission package."""

    def __init__(
        self,
        target: MissionTarget,
        db: Database[Flight],
        auto_asap: bool = False,
        custom_name: str | None = None,
        frequency: RadioFrequency | None = None,
    ) -> None:
        self.target = target
        self._db = db
        self.frequency = frequency
        self.custom_name = custom_name

        # True if the package ToT should be reset to ASAP whenever the player makes a
        # change. This is really a UI property rather than a game property, but we want
        # it to persist in the save.
        self.auto_asap = auto_asap
        self.flights: list[Flight] = []

        # Desired TOT as an offset from mission start. Obviously datetime.min is bogus,
        # but it's going to be replaced by whatever is scheduling the package very soon.
        # TODO: Constructor should maybe take the current time and use that to preserve
        # the old behavior?
        self.time_over_target: datetime = datetime.min
        self.waypoints: PackageWaypoints | None = None

    @property
    def has_players(self) -> bool:
        return any(flight.client_count for flight in self.flights)

    def formation_speed(self, is_helo: bool) -> Optional[Speed]:
        """The speed of the package when in formation.

        If none of the flights in the package will join a formation, this
        returns None. This is not uncommon, since only strike-like (strike,
        DEAD, anti-ship, BAI, etc.) flights and their escorts fly in formation.
        Others (CAP and CAS, currently) will coordinate in target timing but
        fly their own path to the target.
        """
        speeds = []
        for flight in self.flights:
            if (
                isinstance(flight.flight_plan, FormationFlightPlan)
                and flight.is_helo == is_helo
            ):
                speeds.append(flight.flight_plan.best_flight_formation_speed)
        if not speeds:
            return None
        return min(speeds)

    # TODO: Should depend on the type of escort.
    # SEAD might be able to leave before CAP.
    @property
    def escort_start_time(self) -> datetime | None:
        times = []
        for flight in self.flights:
            waypoint = flight.flight_plan.request_escort_at()
            if waypoint is None:
                continue
            tot = flight.flight_plan.tot_for_waypoint(waypoint)
            if tot is None:
                logging.error(
                    f"{flight} requested escort at {waypoint} but that "
                    "waypoint has no TOT. It may not be escorted."
                )
                continue
            times.append(tot)
        if times:
            return min(times)
        return None

    @property
    def escort_end_time(self) -> datetime | None:
        times = []
        for flight in self.flights:
            waypoint = flight.flight_plan.dismiss_escort_at()
            if waypoint is None:
                continue
            tot = flight.flight_plan.tot_for_waypoint(waypoint)
            if tot is None:
                tot = flight.flight_plan.depart_time_for_waypoint(waypoint)
            if tot is None:
                logging.error(
                    f"{flight} dismissed escort at {waypoint} but that "
                    "waypoint has no TOT or departure time. It may not be "
                    "escorted."
                )
                continue
            times.append(tot)
        if times:
            return max(times)
        return None

    @property
    def mission_departure_time(self) -> datetime | None:
        times = []
        for flight in self.flights:
            times.append(flight.flight_plan.mission_departure_time)
        if times:
            return max(times)
        return None

    def set_tot_asap(self, now: datetime) -> None:
        self.time_over_target = TotEstimator(self).earliest_tot(now)

    def add_flight(self, flight: Flight) -> None:
        """Adds a flight to the package."""
        self.flights.append(flight)
        self._db.add(flight.id, flight)

    def remove_flight(self, flight: Flight) -> None:
        """Removes a flight from the package."""
        self.flights.remove(flight)
        self._db.remove(flight.id)
        flight.return_pilots_and_aircraft()
        if flight.cargo is not None:
            flight.cargo.transport = None
        if not self.flights:
            self.waypoints = None

    @property
    def primary_flight(self) -> Optional[Flight]:
        task = self.primary_task
        if not task:
            return None
        primaries = [x for x in self.flights if x.flight_type == task]
        if len(primaries) > 0:
            return primaries[0]
        return None

    @property
    def primary_task(self) -> Optional[FlightType]:
        if not self.flights:
            return None

        flight_counts: Dict[FlightType, int] = defaultdict(lambda: 0)
        for flight in self.flights:
            flight_counts[flight.flight_type] += 1

        # The package will contain a mix of mission types, but in general we can
        # determine the goal of the mission because some mission types are more
        # likely to be the main task than others. For example, a package with
        # only CAP flights is a CAP package, a flight with CAP and strike is a
        # strike package, a flight with CAP and DEAD is a DEAD package, and a
        # flight with strike and SEAD is an OCA/Strike package. This list defines the
        # priority order for package task names. The package's primary task will be the
        # first task in this list that matches a flight in the package.
        tasks_by_priority = [
            FlightType.CAS,
            FlightType.STRIKE,
            FlightType.ANTISHIP,
            FlightType.OCA_AIRCRAFT,
            FlightType.OCA_RUNWAY,
            FlightType.BAI,
            FlightType.DEAD,
            FlightType.TRANSPORT,
            FlightType.AIR_ASSAULT,
            FlightType.ARMED_RECON,
            FlightType.SEAD,
            FlightType.SEAD_SWEEP,
            FlightType.TARCAP,
            FlightType.BARCAP,
            FlightType.AEWC,
            FlightType.FERRY,
            FlightType.RECOVERY,
            FlightType.REFUELING,
            FlightType.SWEEP,
            FlightType.SEAD_ESCORT,
            FlightType.ESCORT,
        ]
        for task in tasks_by_priority:
            if flight_counts[task]:
                return task

        # If we get here, our task_priorities list above is incomplete. Log the
        # issue and return the type of *any* flight in the package.
        some_mission = next(iter(self.flights)).flight_type
        logging.warning(f"Unhandled mission type: {some_mission}")
        return some_mission

    @property
    def package_description(self) -> str:
        """Generates a package description based on flight composition."""
        task = self.primary_task
        if task is None:
            return "No mission"
        oca_strike_types = {FlightType.OCA_AIRCRAFT, FlightType.OCA_RUNWAY}
        if task in oca_strike_types:
            return "OCA Strike"
        return str(task)

    def departure_closest_to_target(self) -> ControlPoint:
        # We'll always have a package, but if this is being planned via the UI
        # it could be the first flight in the package.
        if not self.flights:
            raise RuntimeError(
                "Cannot determine source airfield for package with no flights"
            )

        # The package airfield is either the flight's airfield (when there is no
        # package) or the closest airfield to the objective that is the
        # departure airfield for some flight in the package.
        cache = ObjectiveDistanceCache.get_closest_airfields(self.target)
        for airfield in cache.operational_airfields:
            for flight in self.flights:
                if flight.departure == airfield:
                    return airfield
        raise RuntimeError("Could not find any airfield assigned to this package")

    @staticmethod
    def clone_package(package: Package) -> Package:
        clone = Package(package.target, package._db, package.auto_asap)
        clone.time_over_target = deepcopy(package.time_over_target)
        for f in package.flights:
            cf = Flight.clone_flight(f)
            cf.flight_plan.layout = deepcopy(f.flight_plan.layout)
            cf.package = clone
            clone.add_flight(cf)
        return clone

    def all_flights_waiting_for_start(self) -> bool:
        """Returns True if all flights in the package are waiting for start."""
        for flight in self.flights:
            if not flight.state.is_waiting_for_start:
                return False
        return True
