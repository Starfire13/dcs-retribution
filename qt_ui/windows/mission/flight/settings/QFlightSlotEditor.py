import logging
from typing import Optional, Callable

from PySide6.QtCore import Signal, QModelIndex
from PySide6.QtWidgets import (
    QLabel,
    QGroupBox,
    QSpinBox,
    QGridLayout,
    QComboBox,
    QHBoxLayout,
    QCheckBox,
    QVBoxLayout,
    QPushButton,
    QDialog,
    QWidget,
    QSizePolicy,
)

from game import Game
from game.ato.closestairfields import ClosestAirfields
from game.ato.flight import Flight
from game.ato.flightroster import FlightRoster
from game.ato.iflightroster import IFlightRoster
from game.dcs.aircrafttype import AircraftType
from game.squadrons import Squadron
from game.squadrons.pilot import Pilot
from game.theater import ControlPoint, OffMapSpawn
from game.utils import nautical_miles
from qt_ui.models import PackageModel


class PilotSelector(QComboBox):
    available_pilots_changed = Signal()

    def __init__(
        self, squadron: Optional[Squadron], roster: Optional[IFlightRoster], idx: int
    ) -> None:
        super().__init__()
        self.squadron = squadron
        self.roster = roster
        self.pilot_index = idx
        self.rebuild()

    @staticmethod
    def text_for(pilot: Pilot) -> str:
        return pilot.name

    def _do_rebuild(self) -> None:
        self.clear()
        if self.roster is None or self.pilot_index >= self.roster.max_size:
            self.addItem("No aircraft", None)
            self.setDisabled(True)
            return

        if self.squadron is None:
            raise RuntimeError("squadron cannot be None if roster is set")

        self.setEnabled(True)
        self.addItem("Unassigned", None)
        choices = list(self.squadron.available_pilots)
        current_pilot = self.roster.pilot_at(self.pilot_index)
        if current_pilot is not None:
            choices.append(current_pilot)
        # Put players first, otherwise alphabetically.
        for pilot in sorted(choices, key=lambda p: (not p.player, p.name)):
            self.addItem(self.text_for(pilot), pilot)
        if current_pilot is None:
            self.setCurrentText("Unassigned")
        else:
            self.setCurrentText(self.text_for(current_pilot))
        self.currentIndexChanged.connect(self.replace_pilot)

    def rebuild(self) -> None:
        # The contents of the selector depend on the selection of the other selectors
        # for the flight, so changing the selection of one causes each selector to
        # rebuild. A rebuild causes a selection change, so if we don't block signals
        # during a rebuild we'll never stop rebuilding.
        self.blockSignals(True)
        try:
            self._do_rebuild()
        finally:
            self.blockSignals(False)

    def replace_pilot(self, index: QModelIndex) -> None:
        if self.itemText(index) == "No aircraft":
            # The roster resize is handled separately, so we have no pilots to remove.
            return
        pilot = self.itemData(index)
        if pilot == self.roster.pilot_at(self.pilot_index):
            return
        self.roster.set_pilot(self.pilot_index, pilot)
        self.available_pilots_changed.emit()

    def replace(
        self, squadron: Optional[Squadron], new_roster: Optional[FlightRoster]
    ) -> None:
        self.squadron = squadron
        self.roster = new_roster
        self.rebuild()


class PilotControls(QHBoxLayout):
    player_toggled = Signal()

    def __init__(
        self,
        squadron: Optional[Squadron],
        roster: Optional[FlightRoster],
        idx: int,
        pilots_changed: Signal,
    ) -> None:
        super().__init__()
        self.roster = roster
        self.pilot_index = idx
        self.pilots_changed = pilots_changed

        self.selector = PilotSelector(squadron, roster, idx)
        self.selector.setSizePolicy(
            QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed
        )
        self.selector.currentIndexChanged.connect(self.on_pilot_changed)
        self.addWidget(self.selector)

        self.player_checkbox = QCheckBox(text="Player")
        self.player_checkbox.setToolTip("Checked if this pilot is a player.")
        self.on_pilot_changed(self.selector.currentIndex())
        enabled = False
        if self.roster is not None and squadron is not None:
            enabled = squadron.aircraft.flyable
        self.player_checkbox.setEnabled(enabled)
        self.addWidget(self.player_checkbox)

        self.player_checkbox.toggled.connect(self.on_player_toggled)

    @property
    def pilot(self) -> Optional[Pilot]:
        if self.roster is None or self.pilot_index >= self.roster.max_size:
            return None
        return self.roster.pilot_at(self.pilot_index)

    def on_player_toggled(self, checked: bool) -> None:
        pilot = self.pilot
        if pilot is None:
            logging.error("Cannot toggle state of a pilot when none is selected")
            return
        pilot.player = checked
        self.player_toggled.emit()

        self.pilots_changed.emit()

    def on_pilot_changed(self, index: int) -> None:
        pilot = self.selector.itemData(index)
        self.player_checkbox.blockSignals(True)
        try:
            if self.roster and self.roster.squadron.aircraft.flyable:
                self.player_checkbox.setChecked(pilot is not None and pilot.player)
            else:
                self.player_checkbox.setChecked(False)
        finally:
            if self.roster is not None:
                self.player_checkbox.setEnabled(self.roster.squadron.aircraft.flyable)
            self.player_checkbox.blockSignals(False)
            # on_pilot_changed should emit pilots_changed in its finally block,
            # otherwise the start-type isn't updated if you have a single client
            # pilot which you switch to a non-client pilot
            self.pilots_changed.emit()

    def update_available_pilots(self) -> None:
        self.selector.rebuild()

    def enable_and_reset(self) -> None:
        self.selector.rebuild()
        self.player_checkbox.setEnabled(True)
        self.on_pilot_changed(self.selector.currentIndex())

    def disable_and_clear(self) -> None:
        self.selector.rebuild()
        self.player_checkbox.blockSignals(True)
        try:
            self.player_checkbox.setEnabled(False)
            self.player_checkbox.setChecked(False)
        finally:
            self.player_checkbox.blockSignals(False)

    def replace(
        self, squadron: Optional[Squadron], new_roster: Optional[FlightRoster]
    ) -> None:
        self.roster = new_roster
        if self.roster is None or self.pilot_index >= self.roster.max_size:
            self.disable_and_clear()
        else:
            self.enable_and_reset()
        self.selector.replace(squadron, new_roster)


class FlightRosterEditor(QVBoxLayout):
    MAX_PILOTS = 4
    pilots_changed = Signal()

    def __init__(
        self,
        squadron: Optional[Squadron],
        roster: Optional[IFlightRoster],
    ) -> None:
        super().__init__()
        self.roster = roster

        self.pilot_controls = []
        for pilot_idx in range(self.MAX_PILOTS):

            def make_reset_callback(source_idx: int) -> Callable[[int], None]:
                def callback() -> None:
                    self.update_available_pilots(source_idx)

                return callback

            controls = PilotControls(squadron, roster, pilot_idx, self.pilots_changed)
            controls.selector.available_pilots_changed.connect(
                make_reset_callback(pilot_idx)
            )
            self.pilot_controls.append(controls)
            self.addLayout(controls)

    def update_available_pilots(self, source_idx: int) -> None:
        for idx, controls in enumerate(self.pilot_controls):
            # No need to reset the source of the reset, it was just manually selected.
            if idx != source_idx:
                controls.update_available_pilots()

    def resize(self, new_size: int) -> None:
        if new_size > self.MAX_PILOTS:
            raise ValueError("A flight may not have more than four pilots.")
        if self.roster is not None:
            self.roster.resize(new_size)
        for controls in self.pilot_controls[:new_size]:
            controls.enable_and_reset()
        for controls in self.pilot_controls[new_size:]:
            controls.disable_and_clear()

    def replace(
        self, squadron: Optional[Squadron], new_roster: Optional[FlightRoster]
    ) -> None:
        if self.roster is not None:
            self.roster.clear()
        self.roster = new_roster
        for controls in self.pilot_controls:
            controls.replace(squadron, new_roster)


class QSquadronSelector(QDialog):
    def __init__(self, flight: Flight, parent: Optional[QWidget] = None):
        super().__init__(parent)
        self.flight = flight
        self.parent = parent
        self.init()

    def init(self):
        vbox = QVBoxLayout()
        self.setLayout(vbox)

        self.selector = QComboBox()
        air_wing = self.flight.coalition.air_wing
        for squadron in air_wing.best_squadrons_for(
            self.flight.package.target,
            self.flight.flight_type,
            self.flight.roster.max_size,
            self.flight.is_helo,
            True,
            ignore_range=True,
        ):
            if squadron is self.flight.squadron:
                continue
            self.selector.addItem(
                f"{squadron.name} - {squadron.aircraft.variant_id}", squadron
            )

        vbox.addWidget(self.selector)

        hbox = QHBoxLayout()
        accept = QPushButton("Accept")
        accept.clicked.connect(self.accept)
        hbox.addWidget(accept)
        cancel = QPushButton("Cancel")
        cancel.clicked.connect(self.reject)
        hbox.addWidget(cancel)

        vbox.addLayout(hbox)


class QFlightSlotEditor(QGroupBox):
    flight_resized = Signal(int)
    squadron_changed = Signal(Flight)

    def __init__(
        self,
        package_model: PackageModel,
        flight: Flight,
        game: Game,
    ):
        super().__init__("Slots")
        self.package_model = package_model
        self.flight = flight
        self.game = game
        self.closest_airfields = ClosestAirfields(
            flight.package.target,
            list(game.theater.control_points_for(self.flight.coalition.player)),
        )
        available = self.flight.squadron.untasked_aircraft
        max_count = self.flight.count + available
        if max_count > 4:
            max_count = 4

        layout = QGridLayout()

        self.aircraft_count = QLabel("Aircraft count:")
        self.aircraft_count_spinner = QSpinBox()
        self.aircraft_count_spinner.setMinimum(1)
        self.aircraft_count_spinner.setMaximum(max_count)
        self.aircraft_count_spinner.setValue(flight.count)
        self.aircraft_count_spinner.valueChanged.connect(self._changed_aircraft_count)

        layout.addWidget(self.aircraft_count, 0, 0)
        layout.addWidget(self.aircraft_count_spinner, 0, 1)

        layout.addWidget(QLabel("Squadron:"), 1, 0)
        hbox = QHBoxLayout()
        hbox.addWidget(QLabel(str(self.flight.squadron)))
        squadron_btn = QPushButton("Change Squadron")
        squadron_btn.clicked.connect(self._change_squadron)
        hbox.addWidget(squadron_btn)
        layout.addLayout(hbox, 1, 1)

        layout.addWidget(QLabel("Assigned pilots:"), 2, 0)
        self.roster_editor = FlightRosterEditor(flight.squadron, flight.roster)
        layout.addLayout(self.roster_editor, 2, 1)

        self.setLayout(layout)

    def _change_squadron(self):
        dialog = QSquadronSelector(self.flight)
        if dialog.exec():
            squadron: Optional[Squadron] = dialog.selector.currentData()
            if not squadron:
                return
            flight = Flight(
                self.package_model.package,
                squadron,
                self.flight.count,
                self.flight.flight_type,
                self.flight.start_type,
                self._find_divert_field(squadron.aircraft, squadron.location),
                frequency=self.flight.frequency,
                cargo=self.flight.cargo,
                channel=self.flight.tacan,
                callsign_tcn=self.flight.tcn_name,
            )
            self.package_model.add_flight(flight)
            self.package_model.delete_flight(self.flight)
            self.squadron_changed.emit(flight)

    def _find_divert_field(
        self, aircraft: AircraftType, arrival: ControlPoint
    ) -> Optional[ControlPoint]:
        divert_limit = nautical_miles(150)
        for airfield in self.closest_airfields.operational_airfields_within(
            divert_limit
        ):
            if airfield.captured != self.flight.coalition.player:
                continue
            if airfield == arrival:
                continue
            if not airfield.can_operate(aircraft):
                continue
            if isinstance(airfield, OffMapSpawn):
                continue
            return airfield
        return None

    def _changed_aircraft_count(self):
        old_count = self.flight.count
        new_count = int(self.aircraft_count_spinner.value())
        try:
            self.flight.resize(new_count)
        except ValueError:
            # The UI should have prevented this, but if we ran out of aircraft
            # then roll back the inventory change.
            difference = new_count - self.flight.count
            available = self.flight.squadron.untasked_aircraft
            logging.error(
                f"Could not add {difference} additional aircraft to "
                f"{self.flight} because {self.flight.departure} has only "
                f"{available} {self.flight.unit_type} remaining"
            )
            self.flight.resize(old_count)
            return
        self.roster_editor.resize(new_count)
        self.flight_resized.emit(new_count)
