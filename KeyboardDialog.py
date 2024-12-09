import keyboard
from django.contrib.admin import action

import Consts

from PyQt6.QtCore import Qt, QSettings
from PyQt6.QtGui import QIcon, QIntValidator
from PyQt6.QtWidgets import QLineEdit, QButtonGroup, QDialog, QSpinBox

from UI import Ui_KeyboardDialog
import Actions


class KeyboardDialog(QDialog):
    def __init__(self, key, value):
        super().__init__()
        self.key = key
        self.value = value
        self.initUI()
        self.show()

    def initUI(self):
        self.ui = Ui_KeyboardDialog.Ui_Dialog()
        self.ui.setupUi(self)

        self.setWindowIcon(QIcon("Icons/" + Consts.APPLICATION_ICON))
        self.setModal(True)

        self.settings = QSettings()

        self.ui.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.button_group_action = QButtonGroup()
        self.button_group_action.addButton(self.ui.single_click_button)
        self.button_group_action.addButton(self.ui.press_button)
        self.button_group_action.addButton(self.ui.release_button)
        self.button_group_action.addButton(self.ui.write_button)
        self.ui.single_click_button.click()

        self.ui.first_reset_button.setIcon(QIcon("Icons/" + Consts.RESET_ICON))
        self.ui.second_reset_button.setIcon(QIcon("Icons/" + Consts.RESET_ICON))
        self.ui.third_reset_button.setIcon(QIcon("Icons/" + Consts.RESET_ICON))

        self.ui.first_reset_button.clicked.connect(self.reset)
        self.ui.second_reset_button.clicked.connect(self.reset)
        self.ui.third_reset_button.clicked.connect(self.reset)

        self.ui.first_key_button.clicked.connect(self.change)
        self.ui.second_key_button.clicked.connect(self.change)
        self.ui.third_key_button.clicked.connect(self.change)

        self.ui.apply_button.clicked.connect(self.accept)
        self.ui.back_button.clicked.connect(self.reject)

    def reset(self):
        widget = self.sender()
        if widget == self.ui.first_reset_button:
            self.ui.first_key_button.setText("")
        elif widget == self.ui.second_reset_button:
            self.ui.second_key_button.setText("")
        elif widget == self.ui.third_reset_button:
            self.ui.second_key_button.setText("")

    def change(self):
        key = keyboard.read_key().translate(Consts.KEYBOARD_KEYS).capitalize()
        if self.sender() == self.ui.first_key_button:
            self.ui.first_key_button.setText(key)
        elif self.sender() == self.ui.second_key_button:
            self.ui.second_key_button.setText(key)
        elif self.sender() == self.ui.third_key_button:
            self.ui.third_key_button.setText(key)

    def keyPressEvent(self, event):
        pass

    def get(self):
        action = None
        text = ""
        if self.ui.single_click_button.isChecked():
            action = Actions.KeyboardAction.SINGLE_CLICK
        elif self.ui.press_button.isChecked():
            action = Actions.KeyboardAction.PRESS
        elif self.ui.release_button.isChecked():
            action = Actions.KeyboardAction.RELEASE
        elif self.ui.write_button.isChecked():
            action = Actions.KeyboardAction.WRITE_TEXT
            text = self.ui.write_text_edit.text()

        arr = []
        if self.ui.first_key_button.text():
            arr.append(self.ui.first_key_button.text())
        if self.ui.second_key_button.text():
            arr.append(self.ui.second_key_button.text())
        if self.ui.third_key_button.text():
            arr.append(self.ui.third_key_button.text())
        res = []
        for x in arr:
            if x not in res:
                res.append(x)
        key = "+".join(res)
        return Actions.KeyboardAction(key=key, action=action, text=text)
