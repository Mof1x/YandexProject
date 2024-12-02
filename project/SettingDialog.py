import keyboard

import Consts

from PyQt6.QtCore import Qt, QSettings
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QDialog

from UI import Ui_SettingsWindow


class Settings(QDialog):
    def __init__(self, key, value):
        super().__init__()
        self.key = key
        self.value = value
        self.settings = QSettings()

        self.initUI()

    def initUI(self):
        self.ui = Ui_SettingsWindow.Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Назначьте кнопку")
        self.setWindowIcon(QIcon(Consts.SETTINGS_ICON))

        self.ui.label.setText(self.settings.value(self.key, self.value))
        self.ui.change_button.setText(Consts.CHANGE)
        self.ui.apply_button.setText(Consts.APPLY)

        self.ui.label_layout.addRow(Consts.KEY + ": ", self.ui.label)
        self.ui.label_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.ui.change_button.clicked.connect(self.change)
        self.ui.apply_button.clicked.connect(self.apply)

    def change(self):
        flag = False
        while True:
            key_1 = keyboard.read_key()
            if keyboard.is_pressed(key_1):
                while keyboard.is_pressed(key_1):
                    key_2 = keyboard.read_key()
                    if key_1 != key_2:
                        self.ui.label.setText((key_1 + " + " + key_2).title())
                        flag = True
                        break
                else:
                    self.ui.label.setText((key_1).title())
                    flag = True
            if flag:
                break

    def apply(self):
        self.accept()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Escape:
            pass

    def get(self):
        self.value = self.ui.label.text()
        return self.value
