from threading import Thread

from PyQt6.QtGui import QShortcut, QKeySequence

import Consts

from PyQt6.QtCore import QSettings
from PyQt6.QtWidgets import QListWidgetItem, QApplication
from PyQt6.QtWidgets import QMainWindow

from UI import Ui_BindsWindow
import BindItem


class BindsWindow(QMainWindow):

    def __init__(self, widget):
        super().__init__()
        self.widget = widget
        self.settings = QSettings()

        self.initUI()

    def initUI(self):
        self.ui = Ui_BindsWindow.Ui_MainWindow()
        self.ui.setupUi(self)

        for key, bind in self.settings.value(Consts.BINDS, Consts.DEFAULT_BINDS).items():
            item = QListWidgetItem(self.ui.list_widget)
            self.ui.list_widget.addItem(item)
            row = BindItem.BindItem(self.ui.list_widget, item, key, bind)
            item.setSizeHint(row.minimumSizeHint())
            self.ui.list_widget.setItemWidget(item, row)

        self.ui.back_button.clicked.connect(self.goToMain)

    def goToMain(self):
        self.widget.setCurrentIndex(self.widget.currentIndex() - 1)

    def closeEvent(self, event):
        QApplication.closeAllWindows()
        QApplication.quit()
        event.accept()
