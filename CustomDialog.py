from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QDialog

import Consts
from UI import Ui_AcceptDialog


class CustomDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_AcceptDialog.Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon("Icons/" + Consts.APPLICATION_ICON))

    def keyPressEvent(self, event):
        pass