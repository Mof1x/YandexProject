import Consts

from PyQt6.QtCore import Qt, QSettings
from PyQt6.QtGui import QIcon, QIntValidator
from PyQt6.QtWidgets import QLineEdit, QButtonGroup, QDialog, QSpinBox

from UI import Ui_MouseDialog
import Actions


class MouseDialog(QDialog):
    def __init__(self, key, value):
        super().__init__()
        self.key = key
        self.value = value
        self.initUI()
        self.show()

    def initUI(self):
        self.ui = Ui_MouseDialog.Ui_Dialog()
        self.ui.setupUi(self)

        self.setWindowIcon(QIcon("Icons/" + Consts.APPLICATION_ICON))
        self.setModal(True)

        self.settings = QSettings()

        self.ui.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.button_group_action = QButtonGroup()
        self.button_group_action.addButton(self.ui.single_click_button)
        self.button_group_action.addButton(self.ui.double_click_button)
        self.button_group_action.addButton(self.ui.press_button)
        self.button_group_action.addButton(self.ui.release_button)
        self.ui.single_click_button.click()

        self.button_group = QButtonGroup()
        self.button_group.addButton(self.ui.lm_button)
        self.button_group.addButton(self.ui.rm_button)
        self.button_group.addButton(self.ui.cm_button)
        self.ui.lm_button.click()

        self.button_group_move_action = QButtonGroup()
        self.button_group_move_action.addButton(self.ui.move_on_button)
        self.button_group_move_action.addButton(self.ui.move_in_button)
        self.ui.move_on_button.click()

        self.x_edit = QLineEdit("0")
        self.y_edit = QLineEdit("0")
        self.x_edit.setValidator(QIntValidator())
        self.y_edit.setValidator(QIntValidator())

        self.ui.x_edit_layout.addRow("X: ", self.x_edit)
        self.ui.y_edit_layout.addRow("Y: ", self.y_edit)

        self.duration_edit = QLineEdit("0")
        self.duration_edit.setValidator(QIntValidator())
        self.ui.duration_layout.addRow(Consts.DURATION + ": ", self.duration_edit)

        self.mouse_wheel = QSpinBox()
        self.ui.mouse_wheel_layout.addRow(Consts.MOUSE_WHEEL + ": ", self.mouse_wheel)

        self.ui.apply_button.clicked.connect(self.applyButton)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Escape:
            pass

    def applyButton(self):
        self.accept()

    def get(self):
        line = self.button_group_action.checkedButton().text()
        action = None
        if line == Consts.SINGLE_CLICK:
            action = Actions.MouseAction.SINGLE_CLICK
        elif line == Consts.DOUBLE_CLICK:
            action = Actions.MouseAction.DOUBLE_CLICK
        elif line == Consts.PRESS:
            action = Actions.MouseAction.PRESS
        elif line == Consts.RELEASE:
            action = Actions.MouseAction.RELEASE

        line = self.button_group.checkedButton().text()
        button = None
        if line == Consts.LMB:
            button = "left"
        elif line == Consts.RMB:
            button = "right"
        elif line == Consts.MOUSE_WHEEL:
            button = "middle"

        action_move = None
        line = self.button_group_move_action.checkedButton().text()
        if line == Consts.ON:
            action_move = Actions.MouseAction.DRAG
        elif line == Consts.IN:
            action_move = Actions.MouseAction.MOVE

        x = int(self.x_edit.text())
        y = int(self.y_edit.text())

        duration = int(self.duration_edit.text())

        wheel = int(self.mouse_wheel.text())

        return Actions.MouseAction(action=action, button=button, action_move=action_move, x_y=(x, y), duration=duration,
                                   wheel=wheel)