from tkinter import PanedWindow

from PyQt6.QtWidgets import QListWidget, QListWidgetItem, QPushButton, QSizePolicy

import Consts
import ActionItem


class ListWidget(QListWidget):
    def __init__(self, parent=None):
        super(ListWidget, self).__init__(parent)
        self.initUi()

    def initUi(self):
        item = QListWidgetItem(self)
        self.addItem(item)
        add_button = QPushButton(Consts.ADD_ACTION)
        add_button.clicked.connect(self.addBind)
        self.setItemWidget(item, add_button)
        item.setSizeHint(add_button.minimumSizeHint())
        self.setVerticalScrollMode(QListWidget.ScrollMode.ScrollPerPixel)
        self.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)


    def addBind(self):
        self.takeItem(self.currentIndex().row())

        item = QListWidgetItem(self)
        widget = ActionItem.AddActionItem(self, item)
        self.addItem(item)
        item.setSizeHint(widget.minimumSizeHint())
        self.setItemWidget(item, widget)

        item = QListWidgetItem(self)
        widget = QPushButton(Consts.ADD_ACTION)
        self.addItem(item)
        item.setSizeHint(widget.minimumSizeHint())
        self.setItemWidget(item, widget)
        widget.clicked.connect(self.addBind)


    def getActions(self):
        arr = []
        for i in range(self.count() - 1):
            item = self.item(i)
            widget = self.itemWidget(item)
            arr.append(widget.getAction())
        return arr
