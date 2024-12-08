from PIL.DdsImagePlugin import item1
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon
from PyQt6.QtPrintSupport import QPageSetupDialog

import Consts
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton, QDialog, QDialogButtonBox, QVBoxLayout, \
    QProgressDialog, QInputDialog, QSizePolicy

from Consts import WRITE_TEXT
from CustomDialog import CustomDialog
from KeyboardDialog import KeyboardDialog
from MouseDialog import MouseDialog
from ListWidget import ListWidget
from UI import Ui_ActionItem, Ui_FinalActionItem, Ui_AcceptDialog, Ui_CycleActionItem
import Actions



class ActionItem(QWidget):
    def __init__(self, parent_list_widget, item, widget=None):
        super().__init__()
        self.parent_list_widget = parent_list_widget
        self.item = item
        self.widget = widget

    def deleteButton(self):
        dialog = CustomDialog()
        if dialog.exec():
            self.parent_list_widget.takeItem(self.parent_list_widget.indexFromItem(self.item).row())
            self.ui.list_item_layout.update()

    def editButton(self):
        dialog = CustomDialog()
        if dialog.exec():
            self.parent_list_widget.removeItemWidget(self.item)
            widget = AddActionItem(self.parent_list_widget, self.item)
            self.parent_list_widget.setItemWidget(self.item, widget)
            self.item.setSizeHint(widget.minimumSizeHint())

    def getAction(self):
        return self.action


class AddActionItem(ActionItem):
    def __init__(self, list_widget, item):
        super().__init__(list_widget, item)
        self.initUi()

    def initUi(self):
        self.ui = Ui_ActionItem.Ui_Form()
        self.ui.setupUi(self)
        self.ui.delete_button.setIcon(QIcon("Icons/" + Consts.TRASHCAN_ICON))

        self.ui.delete_button.clicked.connect(self.deleteButton)
        self.ui.mouse_button.clicked.connect(self.goToMouseDialog)
        self.ui.keyboard_button.clicked.connect(self.goToKeyboardDialog)
        self.ui.timer_button.clicked.connect(self.goToTimerDialog)
        self.ui.cycle_button.clicked.connect(self.addCycle)

    def goToMouseDialog(self):
        self.dialog = MouseDialog(Consts.SETTINGS_EMERGENCY_STOP, Consts.DEFAULT_EMERGENCY_STOP)
        if self.dialog.exec():
            action = self.dialog.get()
            self.parent_list_widget.removeItemWidget(self.item)
            widget = FinalAddActionItem(self.parent_list_widget, self.item, action)
            self.widget = widget
            self.parent_list_widget.setItemWidget(self.item, widget)
            print("Success!")
        else:
            print("Cancel!")

    def goToKeyboardDialog(self):
        self.dialog = KeyboardDialog(Consts.SETTINGS_EMERGENCY_STOP, Consts.DEFAULT_EMERGENCY_STOP)
        if self.dialog.exec():
            action = self.dialog.get()
            self.parent_list_widget.removeItemWidget(self.item)
            widget = FinalAddActionItem(self.parent_list_widget, self.item, action)
            self.widget = widget
            self.parent_list_widget.setItemWidget(self.item, widget)
            print("Success!")
        else:
            print("Cancel!")

    def goToTimerDialog(self):
        self.dialog = QInputDialog(self)
        self.dialog.setInputMode(QInputDialog.InputMode.IntInput)
        num, flag = self.dialog.getInt(self, "", Consts.MILLISECONDS, 0, 0, 10 ** 6, 1)
        if flag:
            action = Actions.Sleep(num)
            widget = FinalAddActionItem(self.parent_list_widget, self.item, action)
            self.widget = widget
            self.parent_list_widget.setItemWidget(self.item, widget)

    def addCycle(self):
        self.parent_list_widget.removeItemWidget(self.item)
        widget = CycleAddActionItem(self.parent_list_widget, self.item)
        self.parent_list_widget.setItemWidget(self.item, widget)


class CycleAddActionItem(ActionItem):
    def __init__(self, parent_list_widget, item):
        super().__init__(parent_list_widget, item)
        self.initUi()

    def initUi(self):
        self.ui = Ui_CycleActionItem.Ui_Form()
        self.ui.setupUi(self)

        self.list_widget = ListWidget()

        self.ui.list_item_layout.addWidget(self.list_widget)

        self.item.setSizeHint(QSize(350, 300))

        self.ui.edit_button.setIcon(QIcon("Icons/" + Consts.EDIT_ICON))
        self.ui.delete_button.setIcon(QIcon("Icons/" + Consts.TRASHCAN_ICON))

        self.ui.edit_button.clicked.connect(self.editButton)
        self.ui.delete_button.clicked.connect(self.deleteButton)

    def getAction(self):
        always = self.ui.always_button.isChecked()
        n = int(self.ui.count_edit.text())
        actions = self.list_widget.getActions()
        return Actions.Cycle(always, n, actions)


class FinalAddActionItem(ActionItem):
    def __init__(self, list_widget, item, action):
        super().__init__(list_widget, item)
        self.action = action
        self.initUi()

    def initUi(self):
        self.ui = Ui_FinalActionItem.Ui_Form()
        self.ui.setupUi(self)
        self.ui.edit_button.setIcon(QIcon("Icons/" + Consts.EDIT_ICON))
        self.ui.delete_button.setIcon(QIcon("Icons/" + Consts.TRASHCAN_ICON))
        self.ui.edit_button.clicked.connect(self.editButton)
        self.ui.delete_button.clicked.connect(self.deleteButton)
        if self.action.__class__.__name__ == "MouseAction":
            self.printMouseAction()
        elif self.action.__class__.__name__ == "KeyboardAction":
            self.printKeyboardAction()
        elif self.action.__class__.__name__ == "Sleep":
            self.printTimerAction()

    def printMouseAction(self):
        self.ui.nameAction_label.setText(Consts.MOUSE_ACTION)
        line = (f"{Consts.ACTION}: {self.action.action}\n"
                f"{Consts.BUTTON}: {self.action.button}\n"
                f"{Consts.MOVE_MOUSE} {self.action.action_move}: {self.action.x_y[0]}, {self.action.x_y[1]}\n"
                f"{Consts.DURATION}: {self.action.duration}\n"
                f"{Consts.MOUSE_WHEEL}: {self.action.wheel}\n")
        self.ui.action_label.setText(line)
        self.item.setSizeHint(QSize(380, 200))

    def printKeyboardAction(self):
        self.ui.nameAction_label.setText(Consts.KEYBOARD_ACTION)
        line = (f"{Consts.ACTION}: {self.action.action}\n"
                f"{Consts.BUTTONS}: {self.action.key}\n"
                f"{WRITE_TEXT}: {self.action.text}\n")
        self.ui.action_label.setText(line)
        self.item.setSizeHint(QSize(380, 200))

    def printTimerAction(self):
        self.ui.nameAction_label.setText(Consts.TIMER)
        line = (f"{Consts.DURATION}: {self.action.time}")
        self.ui.action_label.setText(line)
        self.item.setSizeHint(QSize(380, 100))



