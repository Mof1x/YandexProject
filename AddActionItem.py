from PIL.DdsImagePlugin import item1
from PyQt6.QtGui import QIcon
from PyQt6.QtPrintSupport import QPageSetupDialog

import Consts
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton, QDialog, QDialogButtonBox, QVBoxLayout, \
    QProgressDialog, QInputDialog, QSizePolicy

from CycleItem import CycleItem
from ListWidget import ListWidget
from UI import Ui_ActionItem, UI_FinalActionItem, UI_AcceptDialog, UI_CycleItem
import Actions

import MouseDialog


class AddActionItem(QWidget):
    def __init__(self, list_widget, item, action=None):
        super().__init__()
        self.list_widget = list_widget
        self.item = item
        self.action = action

        self.initUi()

    def initUi(self):
        self.ui = Ui_ActionItem.Ui_Form()
        self.ui.setupUi(self)
        self.ui.delete_button.setIcon(QIcon("Icons/" + Consts.TRASHCAN_ICON))

        self.ui.delete_button.clicked.connect(self.deleteButton)
        self.ui.mouse_button.clicked.connect(self.goToMouseDialog)
        self.ui.timer_button.clicked.connect(self.goToTimerDialog)
        self.ui.cycle_button.clicked.connect(self.addCycle)

    def deleteButton(self):
        dialog = CustomDialog()
        if dialog.exec():
            print(self.item)
            self.list_widget.takeItem(self.list_widget.indexFromItem(self.item).row())
            self.ui.list_item_layout.update()

    def editButton(self):
        dialog = CustomDialog()

        if dialog.exec():
            self.list_widget.removeItemWidget(self.item)
            widget = AddActionItem(self.list_widget, self.item)
            self.list_widget.setItemWidget(self.item, widget)
            self.item.setSizeHint(widget.minimumSizeHint())

    def goToMouseDialog(self):
        self.dialog = MouseDialog.MouseDialog(Consts.SETTINGS_EMERGENCY_STOP, Consts.DEFAULT_EMERGENCY_STOP)
        if self.dialog.exec():
            self.action = self.dialog.get()
            self.list_widget.removeItemWidget(self.item)

            widget = FinalAddActionItem(self.list_widget, self.item, self.action)
            self.list_widget.setItemWidget(self.item, widget)
            print("Success!")
        else:
            print("Cancel!")

    def goToTimerDialog(self):
        self.dialog = QInputDialog(self)
        self.dialog.setInputMode(QInputDialog.InputMode.IntInput)
        num, flag = self.dialog.getInt(self, "", Consts.MILLISECONDS, 0, 0, 10 ** 6, 1)
        if flag:
            self.action = Actions.Sleep(num)
            widget = FinalAddActionItem(self.list_widget, self.item, self.action)
            self.list_widget.setItemWidget(self.item, widget)

    def addCycle(self):
        self.list_widget.removeItemWidget(self.item)
        self.list_widget.setItemWidget(self.item, CycleAddActionItem(self.list_widget, self.item))

    def get(self):
        return self.action


class FinalAddActionItem(AddActionItem):
    def __init__(self, list_widget, item, action=None):
        super().__init__(list_widget, item, action)

    def initUi(self):
        self.ui = UI_FinalActionItem.Ui_Form()
        self.ui.setupUi(self)
        self.ui.edit_button.setIcon(QIcon("Icons/" + Consts.EDIT_ICON))
        self.ui.delete_button.setIcon(QIcon("Icons/" + Consts.TRASHCAN_ICON))
        self.ui.edit_button.clicked.connect(self.editButton)
        self.ui.delete_button.clicked.connect(self.deleteButton)


class CycleAddActionItem(AddActionItem):
    def __init__(self, list_widget, item, action=None):
        super().__init__(list_widget, item, action)
        self.list_widget = list_widget
        self.item = item
        self.initUi()

    def initUi(self):
        self.layout = QHBoxLayout()
        self.ui = CycleItem()
        self.layout.addWidget(self.ui)

        self.ui.edit_button.setIcon(QIcon("Icons/" + Consts.EDIT_ICON))
        self.ui.delete_button.setIcon(QIcon("Icons/" + Consts.TRASHCAN_ICON))
        self.ui.edit_button.clicked.connect(self.editButton)
        self.ui.delete_button.clicked.connect(self.deleteButton)



class CustomDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = UI_AcceptDialog.Ui_Dialog()
        self.ui.setupUi(self)
