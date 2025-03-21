import logging
import traceback
import webbrowser
from datetime import datetime
from pathlib import Path
from typing import Optional

from PySide6.QtCore import QSettings, Qt, Signal
from PySide6.QtGui import QCloseEvent, QIcon, QAction, QGuiApplication, QActionGroup
from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QMainWindow,
    QMessageBox,
    QSplitter,
    QVBoxLayout,
    QWidget,
)

import qt_ui.uiconstants as CONST
from game import Game, VERSION, persistency, Migrator
from game.debriefing import Debriefing
from game.game import TurnState
from game.layout import LAYOUTS
from game.persistency import pre_pretense_backups_dir
from game.pretense.pretensemissiongenerator import PretenseMissionGenerator
from game.server import EventStream, GameContext
from game.server.dependencies import QtCallbacks, QtContext
from game.theater import ControlPoint, MissionTarget, TheaterGroundObject
from qt_ui import liberation_install
from qt_ui.dialogs import Dialog
from qt_ui.models import GameModel
from qt_ui.simcontroller import SimController
from qt_ui.uiconstants import URLS
from qt_ui.uiflags import UiFlags
from qt_ui.uncaughtexceptionhandler import UncaughtExceptionHandler
from qt_ui.widgets.QTopPanel import QTopPanel
from qt_ui.widgets.ato import QAirTaskingOrderPanel
from qt_ui.widgets.map.QLiberationMap import QLiberationMap
from qt_ui.windows.GameUpdateSignal import GameUpdateSignal
from qt_ui.windows.QDebriefingWindow import QDebriefingWindow
from qt_ui.windows.basemenu.QBaseMenu2 import QBaseMenu2
from qt_ui.windows.groundobject.QGroundObjectMenu import QGroundObjectMenu
from qt_ui.windows.infos.QInfoPanel import QInfoPanel
from qt_ui.windows.logs.QLogsWindow import QLogsWindow
from qt_ui.windows.newgame.QNewGameWizard import NewGameWizard
from qt_ui.windows.notes.QNotesWindow import QNotesWindow
from qt_ui.windows.preferences.QLiberationPreferencesWindow import (
    QLiberationPreferencesWindow,
)
from qt_ui.windows.settings.QSettingsWindow import QSettingsWindow
from qt_ui.windows.stats.QStatsWindow import QStatsWindow


class QLiberationWindow(QMainWindow):
    new_package_signal = Signal(MissionTarget)
    tgo_info_signal = Signal(TheaterGroundObject)
    control_point_info_signal = Signal(ControlPoint)

    def __init__(self, game: Game | None, ui_flags: UiFlags) -> None:
        super().__init__()

        self._uncaught_exception_handler = UncaughtExceptionHandler(self)

        self.game = game
        self.sim_controller = SimController(self.game)
        self.sim_controller.sim_update.connect(EventStream.put_nowait)
        self.game_model = GameModel(game, self.sim_controller)
        GameContext.set_model(self.game_model)
        self.new_package_signal.connect(
            lambda target: Dialog.open_new_package_dialog(target, self)
        )
        self.tgo_info_signal.connect(self.open_tgo_info_dialog)
        self.control_point_info_signal.connect(self.open_control_point_info_dialog)
        QtContext.set_callbacks(
            QtCallbacks(
                lambda target: self.new_package_signal.emit(target),
                lambda tgo: self.tgo_info_signal.emit(tgo),
                lambda cp: self.control_point_info_signal.emit(cp),
            )
        )
        Dialog.set_game(self.game_model)
        self.ato_panel = QAirTaskingOrderPanel(self.game_model)
        self.info_panel = QInfoPanel(self.game)
        self.liberation_map = QLiberationMap(
            self.game_model, ui_flags.dev_ui_webserver, self
        )

        self.setGeometry(300, 100, 270, 100)
        self.updateWindowTitle()
        self.setWindowIcon(QIcon("./resources/icon.png"))
        self.statusBar().showMessage("Ready")

        self.initUi(ui_flags)
        self.initActions()
        self.initToolbar()
        self.initMenuBar()
        self.connectSignals()

        # Default to maximized on the main display if we don't have any persistent
        # configuration.
        screen = QGuiApplication.primaryScreen().availableSize()
        self.setGeometry(0, 0, screen.width(), screen.height())
        self.setWindowState(Qt.WindowState.WindowMaximized)

        # But override it with the saved configuration if it exists.
        self._restore_window_geometry()

        if self.game is None:
            last_save_file = liberation_install.get_last_save_file()
            if last_save_file:
                logging.info("Loading last saved game : " + str(last_save_file))
                game = persistency.load_game(last_save_file)
                game = self.migrate_game(game, last_save_file)
                self.onGameGenerated(game)
                self.updateWindowTitle(last_save_file if game else None)
            else:
                logging.info("No existing save game")
        else:
            self.onGameGenerated(self.game)

    def initUi(self, ui_flags: UiFlags) -> None:
        hbox = QSplitter(Qt.Orientation.Horizontal)
        vbox = QSplitter(Qt.Orientation.Vertical)
        hbox.addWidget(self.ato_panel)
        hbox.addWidget(vbox)
        vbox.addWidget(self.liberation_map)
        vbox.addWidget(self.info_panel)

        # Will make the ATO sidebar as small as necessary to fit the content. In
        # practice this means it is sized by the hints in the panel.
        hbox.setSizes([1, 10000000])
        vbox.setSizes([600, 100])

        self.top_panel = QTopPanel(self.game_model, self.sim_controller, ui_flags)
        vbox = QVBoxLayout()
        vbox.setContentsMargins(0, 0, 0, 0)
        vbox.addWidget(self.top_panel)
        vbox.addWidget(hbox)

        central_widget = QWidget()
        central_widget.setLayout(vbox)
        self.setCentralWidget(central_widget)

    def connectSignals(self):
        GameUpdateSignal.get_instance().gameupdated.connect(self.setGame)
        GameUpdateSignal.get_instance().debriefingReceived.connect(self.onDebriefing)
        GameUpdateSignal.get_instance().game_state_changed.connect(self.onEndGame)

    def initActions(self):
        self.newGameAction = QAction("&New Game", self)
        self.newGameAction.setIcon(QIcon(CONST.ICONS["New"]))
        self.newGameAction.triggered.connect(self.newGame)
        self.newGameAction.setShortcut("CTRL+N")

        self.openAction = QAction("&Open", self)
        self.openAction.setIcon(QIcon(CONST.ICONS["Open"]))
        self.openAction.triggered.connect(self.openFile)
        self.openAction.setShortcut("CTRL+O")

        self.saveGameAction = QAction("&Save", self)
        self.saveGameAction.setIcon(QIcon(CONST.ICONS["Save"]))
        self.saveGameAction.triggered.connect(self.saveGame)
        self.saveGameAction.setShortcut("CTRL+S")

        self.saveAsAction = QAction("Save &As", self)
        self.saveAsAction.setIcon(QIcon(CONST.ICONS["Save"]))
        self.saveAsAction.triggered.connect(self.saveGameAs)
        self.saveAsAction.setShortcut("CTRL+A")

        self.showAboutDialogAction = QAction("&About DCS Retribution", self)
        self.showAboutDialogAction.setIcon(QIcon.fromTheme("help-about"))
        self.showAboutDialogAction.triggered.connect(self.showAboutDialog)

        self.showLiberationPrefDialogAction = QAction("&Preferences", self)
        self.showLiberationPrefDialogAction.setIcon(QIcon.fromTheme("help-about"))
        self.showLiberationPrefDialogAction.triggered.connect(self.showLiberationDialog)

        self.openDiscordAction = QAction("&Discord Server", self)
        self.openDiscordAction.setIcon(CONST.ICONS["Discord"])
        self.openDiscordAction.triggered.connect(
            lambda: webbrowser.open_new_tab(
                "https://" + "discord.gg" + "/" + "b4x34Bg" + "4We"
            )
        )

        self.openGithubAction = QAction("&Github Repo", self)
        self.openGithubAction.setIcon(CONST.ICONS["Github"])
        self.openGithubAction.triggered.connect(
            lambda: webbrowser.open_new_tab(URLS["Repository"])
        )

        self.ukraineAction = QAction("&Ukraine", self)
        self.ukraineAction.setIcon(CONST.ICONS["Ukraine"])
        self.ukraineAction.triggered.connect(
            lambda: webbrowser.open_new_tab("https://shdwp.github.io/ukraine/")
        )

        self.pretenseLinkAction = QAction("&DCS: Pretense", self)
        self.pretenseLinkAction.setIcon(QIcon(CONST.ICONS["Pretense_discord"]))
        self.pretenseLinkAction.triggered.connect(
            lambda: webbrowser.open_new_tab(
                "https://" + "discord.gg" + "/" + "PtPsb9Mpk6"
            )
        )

        self.newPretenseAction = QAction(
            "&Generate a Pretense Campaign from the running campaign", self
        )
        self.newPretenseAction.setIcon(QIcon(CONST.ICONS["Pretense_generate"]))
        self.newPretenseAction.triggered.connect(self.newPretenseCampaign)

        self.openLogsAction = QAction("Show &logs", self)
        self.openLogsAction.triggered.connect(self.showLogsDialog)

        self.openSettingsAction = QAction("Settings", self)
        self.openSettingsAction.setIcon(CONST.ICONS["Settings"])
        self.openSettingsAction.triggered.connect(self.showSettingsDialog)

        self.openStatsAction = QAction("Stats", self)
        self.openStatsAction.setIcon(CONST.ICONS["Statistics"])
        self.openStatsAction.triggered.connect(self.showStatsDialog)

        self.openNotesAction = QAction("Notes", self)
        self.openNotesAction.setIcon(CONST.ICONS["Notes"])
        self.openNotesAction.triggered.connect(self.showNotesDialog)

        self.importTemplatesAction = QAction("Import Layouts", self)
        self.importTemplatesAction.triggered.connect(self.import_templates)

        self.enable_game_actions(False)

    def enable_game_actions(self, enabled: bool):
        self.openSettingsAction.setVisible(enabled)
        self.openStatsAction.setVisible(enabled)
        self.openNotesAction.setVisible(enabled)

        # Also Disable SaveAction to prevent Keyboard Shortcut
        self.saveGameAction.setEnabled(enabled)
        self.saveGameAction.setVisible(enabled)
        self.saveAsAction.setEnabled(enabled)
        self.saveAsAction.setVisible(enabled)

    def initToolbar(self):
        self.tool_bar = self.addToolBar("File")
        self.tool_bar.addAction(self.newGameAction)
        self.tool_bar.addAction(self.openAction)
        self.tool_bar.addAction(self.saveGameAction)

        self.links_bar = self.addToolBar("Links")
        self.links_bar.addAction(self.openDiscordAction)
        self.links_bar.addAction(self.openGithubAction)
        self.links_bar.addAction(self.ukraineAction)
        self.links_bar.addAction(self.pretenseLinkAction)
        self.links_bar.addAction(self.newPretenseAction)

        self.actions_bar = self.addToolBar("Actions")
        self.actions_bar.addAction(self.openSettingsAction)
        self.actions_bar.addAction(self.openStatsAction)
        self.actions_bar.addAction(self.openNotesAction)

    def initMenuBar(self):
        self.menu = self.menuBar()

        file_menu = self.menu.addMenu("&File")
        file_menu.addAction(self.newGameAction)
        file_menu.addAction(self.openAction)
        file_menu.addSeparator()
        file_menu.addAction(self.saveGameAction)
        file_menu.addAction(self.saveAsAction)
        file_menu.addSeparator()
        file_menu.addAction(self.showLiberationPrefDialogAction)
        file_menu.addSeparator()
        file_menu.addAction("E&xit", self.close)

        tools_menu = self.menu.addMenu("&Developer tools")
        tools_menu.addAction(self.importTemplatesAction)

        help_menu = self.menu.addMenu("&Help")
        help_menu.addAction(self.openDiscordAction)
        help_menu.addAction(self.openGithubAction)
        help_menu.addAction(self.ukraineAction)
        help_menu.addAction(
            "&Releases", lambda: webbrowser.open_new_tab(URLS["Releases"])
        )
        help_menu.addAction(
            "&Online Manual", lambda: webbrowser.open_new_tab(URLS["Manual"])
        )
        help_menu.addAction(
            "&ED Forum Thread", lambda: webbrowser.open_new_tab(URLS["ForumThread"])
        )
        help_menu.addAction(
            "Report an &issue", lambda: webbrowser.open_new_tab(URLS["Issues"])
        )
        help_menu.addAction(self.openLogsAction)

        help_menu.addSeparator()
        help_menu.addAction(self.showAboutDialogAction)

    @staticmethod
    def make_display_rule_action(
        display_rule, group: Optional[QActionGroup] = None
    ) -> QAction:
        def make_check_closure():
            def closure():
                display_rule.value = action.isChecked()

            return closure

        action = QAction(f"&{display_rule.menu_text}", group)

        if display_rule.menu_text in CONST.ICONS.keys():
            action.setIcon(CONST.ICONS[display_rule.menu_text])

        action.setCheckable(True)
        action.setChecked(display_rule.value)
        action.toggled.connect(make_check_closure())
        return action

    def newGame(self):
        wizard = NewGameWizard(self)
        wizard.show()
        wizard.accepted.connect(lambda: self.onGameGenerated(wizard.generatedGame))

    def newPretenseCampaign(self):
        output = persistency.mission_path_for("pretense_campaign.miz")
        try:
            PretenseMissionGenerator(
                self.game, self.game.conditions.start_time
            ).generate_miz(output)
        except Exception as e:
            now = datetime.now()
            date_time = now.strftime("%Y-%d-%mT%H_%M_%S")
            path = pre_pretense_backups_dir()
            tgt = path / f"pre-pretense-backup_{date_time}.retribution"
            path /= f".pre-pretense-backup.retribution"
            if path.exists():
                with open(path, "rb") as source:
                    with open(tgt, "wb") as target:
                        target.write(source.read())
            raise e

        title = "Pretense campaign generated"
        msg = f"A Pretense campaign mission has been successfully generated in {output}"
        QMessageBox.information(QApplication.focusWidget(), title, msg, QMessageBox.Ok)

    def openFile(self):
        if self.game is not None and self.game.savepath:
            save_dir = self.game.savepath
        else:
            save_dir = str(persistency.save_dir())
        file = QFileDialog.getOpenFileName(
            self,
            "Select game file to open",
            dir=save_dir,
            filter="*.retribution;;*.liberation",
        )
        if file is not None and file[0] != "":
            game = persistency.load_game(file[0])
            game = self.migrate_game(game, file[0])
            GameUpdateSignal.get_instance().game_loaded.emit(game)

            self.updateWindowTitle(file[0])

    def migrate_game(self, game, path):
        if game:
            is_liberation = ".liberation" in path
            try:
                Migrator(game, is_liberation)
                return game
            except Exception as e:
                logging.exception(e)
                self.incompatible_save_popup(path)
        else:
            self.incompatible_save_popup(path)
        return None

    def incompatible_save_popup(self, path):
        relative_path = Path(path)
        QMessageBox.critical(
            self,
            "Incompatible save",
            "Incompatible save file detected, please report the issue on GitHub or Discord.\n"
            f"Make sure to include the campaign that fails to load, i.e.:\n\n{relative_path}",
        )

    def saveGame(self):
        logging.info("Saving game")

        if self.game.savepath:
            persistency.save_game(self.game)
            liberation_install.setup_last_save_file(self.game.savepath)
            liberation_install.save_config()
        else:
            self.saveGameAs()

    def saveGameAs(self):
        if self.game is not None and self.game.savepath:
            save_dir = self.game.savepath
        else:
            save_dir = str(persistency.save_dir())
        file = QFileDialog.getSaveFileName(
            self,
            "Save As",
            dir=save_dir,
            filter="*.retribution;;*.liberation",
        )
        if file is not None:
            self.game.savepath = file[0]
            persistency.save_game(self.game)
            liberation_install.setup_last_save_file(self.game.savepath)
            liberation_install.save_config()

            self.updateWindowTitle(file[0])

    def updateWindowTitle(self, save_path: Optional[str] = None) -> None:
        """
        to DCS Retribution - vX.X.X - file_name
        """
        window_title = f"DCS Retribution - v{VERSION}"
        if save_path:  # appending the file name to title as it is updated
            file_name = save_path.split("/")[-1].rsplit(".", 1)[0]
            window_title = f"{window_title} - {file_name}"
        self.setWindowTitle(window_title)

    def onGameGenerated(self, game: Game):
        self.updateWindowTitle()
        logging.info("On Game generated")
        self.game = game
        GameUpdateSignal.get_instance().game_loaded.emit(self.game)

    def onEndGame(self, state: TurnState):
        if state == TurnState.CONTINUE:
            return

        for window in QApplication.topLevelWidgets():
            if window is not self:
                window.close()

        GameUpdateSignal.get_instance().updateGame(None)

        self.top_panel.setControls(False)

        title = "Victory!" if TurnState.WIN else "Defeat!"
        msgvar = "won" if TurnState.WIN else "lost"
        msg = f"You have {msgvar} the campaign, do you wish to start a new one?"
        result = QMessageBox.information(
            QApplication.focusWidget(),
            title,
            msg,
            QMessageBox.StandardButton.Yes,
            QMessageBox.StandardButton.No,
        )

        if result is not None and result == QMessageBox.StandardButton.Yes:
            self.newGame()

    def setGame(self, game: Optional[Game]):
        try:
            self.game = game
            if self.info_panel is not None:
                self.info_panel.setGame(game)
            self.sim_controller.set_game(game)
            self.game_model.set(self.game)
            self.game_model.init_comms_registry()
        except AttributeError:
            logging.exception("Incompatible save game")
            QMessageBox.critical(
                self,
                "Could not load save game",
                "The save game you have loaded is incompatible with this "
                "version of DCS Retribution.\n"
                "\n"
                f"{traceback.format_exc()}",
                QMessageBox.StandardButton.Ok,
            )
            GameUpdateSignal.get_instance().updateGame(None)
        finally:
            self.enable_game_actions(self.game is not None)

    def showAboutDialog(self):
        contributors = [
            "shdwp",
            "Khopa",
            "ColonelPanic",
            "RndName",
            "Roach",
            "Malakhit",
            "Wrycu",
            "calvinmorrow",
            "JohanAberg",
            "Deus",
            "SiKruger",
            "Mustang-25",
            "bgreman",
            "magwo",
            "SnappyComebacks",
            "kavinsky",
            "Schneefl0cke",
            "pbzweihander",
            "Raskil",
            "nosv1",
            "jake-lewis",
            "teamMOYA",
            "benedikt-wegmann",
            "movq",
            "bbirchnz",
            "eddiwood",
            "root0fall",
            "calvinmorrow",
            "UKayeF",
            "Captain Cody",
            "steveveepee",
            "pedromagueija",
            "parithon",
            "TheCandianVendingMachine",
            "bwRavencl",
            "davidp57",
            "Plob",
            "Hawkmoon",
            "alrik11es",
            "Starfire13",
            "Hornet2041/Lion",
            "SgtFuzzle17",
            "Doc_of_Mur",
            "NickJZX",
            "Sith1144",
            "Raffson",
            "MetalStormGhost",
            "HolyOrangeJuice (WRL)",
            "Adecarcer",
            "pande4360",
            "zhexu14",
            "ColonelAkirNakesh",
            "Nosajthedevil",
            "kivipe",
            "Turbolious",
            "ingax01",
            "M-Chimiste",
            "tmz42",
        ]
        text = (
            "<h3>DCS Retribution " + VERSION + "</h3>" + "<b>Source code : </b>"
            "<a href='https://github.com/dcs-retribution/dcs-retribution' style='color:white'>"
            "https://github.com/dcs-retribution/dcs-retribution </a>"
            + "<h4>Authors</h4>"
            + "<p>DCS Retribution is an (independent) fork of DCS Liberation, "
            "which was originally developed by <b>shdwp</b>. "
            "DCS Liberation 2.0 is a partial rewrite based on this work by <b>Khopa</b>. "
            "DCS Retribution was forked during development of "
            "DCS Liberation v6.0.0 in 2022 by <b>Raffson</> & <b>MetalStormGhost</>."
            "<h4>Contributors</h4>"
            + ", ".join(contributors)
            + "<h4>Special Thanks  :</h4>"
            "<b>rp-</b> <i>for the pydcs framework</i><br/>"
            "<b>Grimes (mrSkortch)</b> & <b>Speed</b> <i>for the MIST framework</i><br/>"
            "<b>Ciribob </b> <i>for the JTACAutoLase.lua script</i><br/>"
            "<b>Walder </b> <i>for the Skynet-IADS script</i><br/>"
            "<b>Anubis Yinepu </b> <i>for the Hercules Cargo script</i><br/>"
            '<a href="https://www.flaticon.com/free-icons/bug" title="bug icons" style="color: #ffffff">Bug icons created by Freepik - Flaticon</a><br />'
            'Contains information from <a href="https://osmdata.openstreetmap.de/" style="color: #ffffff">OpenStreetMap © OpenStreetMap contributors</a>, which is made available here under the <a href="https://opendatacommons.org/licenses/odbl/1-0/" style="color: #ffffff">Open Database License (ODbL)</a>.<br />'
            '<a href="https://download.geofabrik.de/index.html/" style="color: #ffffff">OpenStreetMap Data Extracts from Geofabrik</a><br />'
            '<a href="https://www.earthdata.nasa.gov/" style="color: #ffffff">NASA EarthData</a><br />'
            + "<h4>Splash Screen  :</h4>"
            + "Artwork by Andriy Dankovych (CC BY-SA)"
            " <a href='https://www.facebook.com/AndriyDankovych' style='color:white'>"
            "[https://www.facebook.com/AndriyDankovych]</a>"
        )
        about = QMessageBox()
        about.setWindowTitle("About DCS Retribution")
        about.setIcon(QMessageBox.Icon.Information)
        about.setText(text)
        logging.info(about.textFormat())
        about.exec_()

    def showLiberationDialog(self):
        self.subwindow = QLiberationPreferencesWindow()
        self.subwindow.show()

    def showSettingsDialog(self) -> None:
        self.dialog = QSettingsWindow(self.game)
        self.dialog.show()

    def showStatsDialog(self):
        self.dialog = QStatsWindow(self.game)
        self.dialog.show()

    def showNotesDialog(self):
        self.dialog = QNotesWindow(self.game)
        self.dialog.show()

    def import_templates(self):
        LAYOUTS.import_templates()

    def showLogsDialog(self):
        self.dialog = QLogsWindow(self)
        self.dialog.show()

    def onDebriefing(self, debrief: Debriefing):
        logging.info("On Debriefing")
        self.debriefing = QDebriefingWindow(debrief)
        self.debriefing.show()
        self.game_model.init_comms_registry()

    def open_tgo_info_dialog(self, tgo: TheaterGroundObject) -> None:
        QGroundObjectMenu(self, tgo, tgo.control_point, self.game_model).show()

    def open_control_point_info_dialog(self, cp: ControlPoint) -> None:
        self._cp_dialog = QBaseMenu2(None, cp, self.game_model)
        self._cp_dialog.show()

    def _qsettings(self) -> QSettings:
        return QSettings("DCS Retribution", "Qt UI")

    def _restore_window_geometry(self) -> None:
        settings = self._qsettings()
        self.restoreGeometry(settings.value("geometry"))
        self.restoreState(settings.value("windowState"))

    def _save_window_geometry(self) -> None:
        settings = self._qsettings()
        settings.setValue("geometry", self.saveGeometry())
        settings.setValue("windowState", self.saveState())

    def closeEvent(self, event: QCloseEvent) -> None:
        result = QMessageBox.question(
            self,
            "Quit Retribution?",
            "Would you like to save before quitting?",
            QMessageBox.StandardButton.Yes
            | QMessageBox.StandardButton.No
            | QMessageBox.StandardButton.Cancel,
            QMessageBox.StandardButton.Cancel,
        )
        if result in [QMessageBox.StandardButton.Yes, QMessageBox.StandardButton.No]:
            if result == QMessageBox.StandardButton.Yes:
                self.saveGame()
            self._save_window_geometry()
            super().closeEvent(event)
            self.dialog = None
            self.debriefing = None
            for window in QApplication.topLevelWidgets():
                window.close()
        else:
            event.ignore()
