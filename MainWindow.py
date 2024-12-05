
import Actions
import Consts
import SettingDialog

from PyQt6.QtCore import QSettings
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow

from Consts import KEYBOARD
from UI import Ui_MainWindow

import keyboard
import mouse


class MainWindow(QMainWindow):

    def __init__(self, widget):
        super().__init__()
        self.widget = widget
        self.settings = QSettings()

        self.initUI()

    def initUI(self):
        self.ui = Ui_MainWindow.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.emergency_stop_button.setText(
            Consts.EMERGENCY_EXIT + " " + self.settings.value(Consts.SETTINGS_EMERGENCY_STOP,
                                                              Consts.DEFAULT_EMERGENCY_STOP))
        self.ui.emergency_stop_button.clicked.connect(self.finish)

        self.ui.emergency_stop_button_settings.setIcon(QIcon("Icons/" + Consts.SETTINGS_ICON))
        self.ui.emergency_stop_button_settings.clicked.connect(self.goToSettings)
        self.ui.binds_button.clicked.connect(self.goToBinds)
        self.ui.add_binds_button.clicked.connect(self.goToAddBinds)

    def goToSettings(self):
        self.w1 = SettingDialog.Settings(Consts.SETTINGS_EMERGENCY_STOP, Consts.DEFAULT_EMERGENCY_STOP)
        if self.w1.exec():
            value = self.w1.get()
            self.settings.setValue(Consts.SETTINGS_EMERGENCY_STOP, value)
            self.ui.emergency_stop_button.setText(
                Consts.EMERGENCY_EXIT + " " + self.settings.value(Consts.SETTINGS_EMERGENCY_STOP,
                                                                  Consts.DEFAULT_EMERGENCY_STOP))
            print("Success!")
        else:
            print("Cancel!")

    def goToBinds(self):
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)
        self.widget.currentWidget().initUI()

    def goToAddBinds(self):
        self.widget.setCurrentIndex(self.widget.currentIndex() + 2)
        self.widget.currentWidget().initUI()

    def finish(self):
        self.close()

    def closeEvent(self, event):
        QApplication.closeAllWindows()
        QApplication.quit()
        event.accept()
