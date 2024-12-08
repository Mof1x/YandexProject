from PyQt6.QtWidgets import QDialog

from UI import Ui_AcceptDialog


class CustomDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_AcceptDialog.Ui_Dialog()
        self.ui.setupUi(self)

    def keyPressEvent(self, event):
        pass