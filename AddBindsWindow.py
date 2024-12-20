import Actions
import Bind
import Consts
import SettingDialog
import ActionItem

from PyQt6.QtCore import QSettings
from PyQt6.QtGui import QIcon, QShortcut, QKeySequence
from PyQt6.QtWidgets import QPushButton, QListWidgetItem
from PyQt6.QtWidgets import QMainWindow

from ListWidget import ListWidget
from UI import Ui_AddBindsWindow


class AddBindsWindow(QMainWindow):

    def __init__(self, widget):
        super().__init__()
        self.widget = widget
        self.initUI()

    def initUI(self):
        self.settings = QSettings()
        self.ui = Ui_AddBindsWindow.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.line_edit.setPlaceholderText(Consts.LABEL)
        self.ui.hotkey_button.setIcon(QIcon("Icons/" + Consts.SETTINGS_ICON))

        self.list_widget = ListWidget(self)
        self.ui.parent_layout.addWidget(self.list_widget)

        self.ui.back_button.clicked.connect(self.goToMain)
        self.ui.apply_button.clicked.connect(self.apply)
        self.ui.hotkey_button.clicked.connect(self.goToSettings)

    def goToMain(self):
        self.widget.setCurrentIndex(self.widget.currentIndex() - 2)

    def apply(self):
        if self.ui.line_edit.text() in self.settings.value(Consts.BINDS, Consts.DEFAULT_BINDS).keys():
            print("неверное имя")
        else:
            actions = self.list_widget.getActions()
            v = self.settings.value(Consts.BINDS, Consts.DEFAULT_BINDS)
            v[self.ui.line_edit.text()] = Bind.Bind(self.ui.line_edit.text(),
                                                    self.ui.hotkey_label.text()[len(Consts.HOTKEY) + 1:], actions)
            self.settings.setValue(Consts.BINDS, v)
            self.widget.setCurrentIndex(self.widget.currentIndex() - 2)



    def goToSettings(self):
        self.w1 = SettingDialog.Settings(Consts.SETTINGS_HOTKEY, Consts.DEFAULT_HOTKEY)
        if self.w1.exec():
            print("Success!")
            line = self.w1.get()
            self.ui.hotkey_label.setText(
                Consts.HOTKEY + " " + line)
        else:
            print("Cancel!")
