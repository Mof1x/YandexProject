from PyQt6.QtWidgets import QListWidget, QListWidgetItem, QPushButton, QSizePolicy

import Consts
import AddActionItem


class ListWidget(QListWidget):
    def __init__(self, parent=None):
        super(ListWidget, self).__init__(parent)
        self.initUi()

    def initUi(self):
        item = QListWidgetItem(self)
        add_button = QPushButton(Consts.ADD_ACTION)
        add_button.clicked.connect(self.addBind)
        self.setItemWidget(item, add_button)
        item.setSizeHint(add_button.minimumSizeHint())
        self.setVerticalScrollMode(QListWidget.ScrollMode.ScrollPerPixel)
        self.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)


    def addBind(self):
        item = self.currentItem()
        self.removeItemWidget(item)
        widget = AddActionItem.AddActionItem(self, item)
        item.setSizeHint(widget.minimumSizeHint())
        self.setItemWidget(item, widget)
        widget = QPushButton(Consts.ADD_ACTION)
        item = QListWidgetItem(self)
        item.setSizeHint(widget.minimumSizeHint())

        self.addItem(item)
        self.setItemWidget(item, widget)
        widget.clicked.connect(self.addBind)
