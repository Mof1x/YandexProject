from PyQt6.QtGui import QIcon

import Consts
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel

from UI import Ui_ActionItem

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

    def deleteButton(self):
        self.list_widget.takeItem(self.list_widget.indexFromItem(self.item).row())
        self.ui.list_item_layout.update()

    def goToMouseDialog(self):
        self.w1 = MouseDialog.MouseDialog(Consts.SETTINGS_EMERGENCY_STOP, Consts.DEFAULT_EMERGENCY_STOP)
        if self.w1.exec():
            self.action = self.w1.get()
            self.list_widget.removeItemWidget(self.item)
            row = QWidget()
            row.action = self.action
            l = QHBoxLayout()
            l.addWidget(QLabel(self.action.__class__.__name__))
            row.setLayout(l)
            self.list_widget.setItemWidget(self.item, row)
            print("Success!")

        else:
            print("Cancel!")

    def get(self):
        return self.action
