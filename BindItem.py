import keyboard
from PyQt6.QtCore import QSettings, QThreadPool
from PyQt6.QtGui import QIcon, QShortcut, QKeySequence

import Consts
from PyQt6.QtWidgets import QWidget

from Bind import Worker
from CustomDialog import CustomDialog
from UI import Ui_BindItem


class BindItem(QWidget):
    def __init__(self, list_widget, item, name, bind):
        super().__init__()

        self.list_widget = list_widget
        self.item = item
        self.name = name
        self.bind = bind
        self.value = bind.actions
        self.hotkey = bind.hotkey
        self.settings = QSettings()
        self.threadpool = QThreadPool()
        self.initUi()

    def initUi(self):
        self.ui = Ui_BindItem.Ui_Form()
        self.ui.setupUi(self)

        self.ui.delete_button.setIcon(QIcon("Icons/" + Consts.TRASHCAN_ICON))

        self.ui.name_label.setText(self.name)
        self.ui.hotkey_label.setText(self.hotkey)

        self.ui.delete_button.clicked.connect(self.deleteButton)
        self.ui.check_box.clicked.connect(self.onOff)

    def deleteButton(self):
        dialog = CustomDialog()
        if dialog.exec():
            hotkeys = self.settings.value(Consts.BINDS, Consts.DEFAULT_BINDS)
            hotkeys.pop(self.name)
            self.settings.setValue(Consts.BINDS, hotkeys)
            self.list_widget.takeItem(self.list_widget.indexFromItem(self.item).row())

    def onOff(self):
        if self.ui.check_box.isChecked():
            keyboard.add_hotkey(self.hotkey.lower(), self.playBind)
        else:
            # self.shortcut.disconnect()
            keyboard.remove_hotkey(self.hotkey.lower())

    def playBind(self):
        worker = Worker(self.bind)
        self.threadpool.start(worker)
