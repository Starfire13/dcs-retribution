from __future__ import annotations

import logging
from typing import Optional, TYPE_CHECKING

from game.squadrons import Squadron
from game.squadrons.squadrondef import SquadronDef
from game.squadrons.squadrondefloader import SquadronDefLoader
from gen.flights.flight import FlightType
from .campaignairwingconfig import CampaignAirWingConfig, SquadronConfig
from .squadrondefgenerator import SquadronDefGenerator
from ..dcs.aircrafttype import AircraftType
from ..theater import ControlPoint

if TYPE_CHECKING:
    from game import Game
    from game.coalition import Coalition


class DefaultSquadronAssigner:
    def __init__(
        self, config: CampaignAirWingConfig, game: Game, coalition: Coalition
    ) -> None:
        self.config = config
        self.game = game
        self.coalition = coalition
        self.air_wing = coalition.air_wing
        self.squadron_defs = SquadronDefLoader(game, coalition).load()
        self.squadron_def_generator = SquadronDefGenerator(self.coalition)

    def claim_squadron_def(self, squadron: SquadronDef) -> None:
        try:
            self.squadron_defs[squadron.aircraft].remove(squadron)
        except ValueError:
            pass

    def assign(self) -> None:
        for control_point in self.game.theater.control_points_for(
            self.coalition.player
        ):
            for squadron_config in self.config.by_location[control_point]:
                squadron_def = self.find_squadron_for(squadron_config, control_point)
                if squadron_def is None:
                    logging.info(
                        f"{self.coalition.faction.name} has no aircraft compatible "
                        f"with {squadron_config.primary} at {control_point}"
                    )
                    continue

                self.claim_squadron_def(squadron_def)
                squadron = Squadron.create_from(
                    squadron_def, control_point, self.coalition, self.game
                )
                squadron.set_auto_assignable_mission_types(
                    squadron_config.auto_assignable
                )
                self.air_wing.add_squadron(squadron)

    def find_squadron_for(
        self, config: SquadronConfig, control_point: ControlPoint
    ) -> Optional[SquadronDef]:
        for preferred_aircraft in config.aircraft:
            squadron_def = self.find_preferred_squadron(
                preferred_aircraft, config.primary, control_point
            )
            if squadron_def is not None:
                return squadron_def

        # If we didn't find any of the preferred types we should use any squadron
        # compatible with the primary task.
        squadron_def = self.find_squadron_for_task(config.primary, control_point)
        if squadron_def is not None:
            return squadron_def

        # If we can't find any squadron matching the requirement, we should
        # create one.
        return self.squadron_def_generator.generate_for_task(
            config.primary, control_point
        )

    def find_preferred_squadron(
        self, preferred_aircraft: str, task: FlightType, control_point: ControlPoint
    ) -> Optional[SquadronDef]:
        # Attempt to find a squadron with the name in the request.
        squadron_def = self.find_squadron_by_name(
            preferred_aircraft, task, control_point
        )
        if squadron_def is not None:
            return squadron_def

        # If the name didn't match a squadron available to this coalition, try to find
        # an aircraft with the matching name that meets the requirements.
        try:
            aircraft = AircraftType.named(preferred_aircraft)
        except KeyError:
            # No aircraft with this name.
            return None

        if aircraft not in self.coalition.faction.aircrafts:
            return None

        squadron_def = self.find_squadron_for_airframe(aircraft, task, control_point)
        if squadron_def is not None:
            return squadron_def

        # No premade squadron available for this aircraft that meets the requirements,
        # so generate one if possible.
        return self.squadron_def_generator.generate_for_aircraft(aircraft)

    @staticmethod
    def squadron_compatible_with(
        squadron: SquadronDef, task: FlightType, control_point: ControlPoint
    ) -> bool:
        return squadron.operates_from(control_point) and task in squadron.mission_types

    def find_squadron_for_airframe(
        self, aircraft: AircraftType, task: FlightType, control_point: ControlPoint
    ) -> Optional[SquadronDef]:
        for squadron in self.squadron_defs[aircraft]:
            if self.squadron_compatible_with(squadron, task, control_point):
                return squadron
        return None

    def find_squadron_by_name(
        self, name: str, task: FlightType, control_point: ControlPoint
    ) -> Optional[SquadronDef]:
        for squadrons in self.squadron_defs.values():
            for squadron in squadrons:
                if squadron.name == name and self.squadron_compatible_with(
                    squadron, task, control_point
                ):
                    return squadron
        return None

    def find_squadron_for_task(
        self, task: FlightType, control_point: ControlPoint
    ) -> Optional[SquadronDef]:
        for squadrons in self.squadron_defs.values():
            for squadron in squadrons:
                if self.squadron_compatible_with(squadron, task, control_point):
                    return squadron
        return None
