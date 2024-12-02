import Consts
import SettingDialog

from PyQt6.QtCore import QSettings
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow

from UI import Ui_MainWindow


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
            Consts.EMERGENCY_STOP + " " + self.settings.value(Consts.SETTINGS_EMERGENCY_STOP,
                                                              Consts.DEFAULT_EMERGENCY_STOP))
        self.ui.emergency_stop_button_settings.setText("")
        self.ui.binds_button.setText(Consts.BINDS)
        self.ui.add_binds_button.setText(Consts.ADD_BINDS)
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
                Consts.EMERGENCY_STOP + " " + self.settings.value(Consts.SETTINGS_EMERGENCY_STOP,
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

    def closeEvent(self, event):
        QApplication.closeAllWindows()
        QApplication.quit()
        event.accept()
