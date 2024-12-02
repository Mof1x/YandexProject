import Bind
import Consts
import SettingDialog
import AddActionItem

from PyQt6.QtCore import QSettings
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QPushButton, QListWidgetItem
from PyQt6.QtWidgets import QMainWindow

from UI import Ui_AddBindsWindow


class AddBindsWindow(QMainWindow):

    def __init__(self, widget):
        super().__init__()

        self.widget = widget

        self.initUI()
        self.show()

    def initUI(self):
        self.settings = QSettings()
        self.ui = Ui_AddBindsWindow.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.line_edit.setPlaceholderText(Consts.LABEL)
        self.ui.hotkey_button.setIcon(QIcon("Icons/" + Consts.SETTINGS_ICON))

        item = QListWidgetItem(self.ui.list_widget)
        add_button = QPushButton(Consts.ADD_ACTION)
        add_button.clicked.connect(self.addBind)
        row = AddActionItem.AddActionItem(self.ui.list_widget, item)
        item.setSizeHint(row.minimumSizeHint())
        self.ui.list_widget.setItemWidget(item, add_button)

        self.ui.back_button.clicked.connect(self.goToMain)
        self.ui.apply_button.clicked.connect(self.apply)
        self.ui.hotkey_button.clicked.connect(self.goToSettings)

    def goToMain(self):
        self.widget.setCurrentIndex(self.widget.currentIndex() - 2)

    def addBind(self):
        self.ui.list_widget.takeItem(self.ui.list_widget.currentIndex().row())

        item = QListWidgetItem(self.ui.list_widget)
        self.ui.list_widget.addItem(item)
        row = AddActionItem.AddActionItem(self.ui.list_widget, item)
        item.setSizeHint(row.minimumSizeHint())
        self.ui.list_widget.setItemWidget(item, row)

        item = QListWidgetItem(self.ui.list_widget)
        add_button = QPushButton(Consts.ADD_ACTION)
        item.setSizeHint(row.minimumSizeHint())
        self.ui.list_widget.setItemWidget(item, add_button)
        add_button.clicked.connect(self.addBind)

    def apply(self):
        arr = []
        if self.ui.line_edit.text() in self.settings.value(Consts.BINDS, Consts.DEFAULT_BINDS).keys():
            print("неверное имя")
        else:
            for i in range(self.ui.list_widget.count() - 1):
                item = self.ui.list_widget.item(i)
                widget = self.ui.list_widget.itemWidget(item)
                arr.append(widget.action)
            v = self.settings.value(Consts.BINDS, Consts.DEFAULT_BINDS)
            v[self.ui.line_edit.text()] = Bind.Bind(self.ui.line_edit.text(),
                                                    self.ui.hotkey_label.text()[len(Consts.HOTKEY) + 1:], arr)
            self.settings.setValue(Consts.BINDS, v)

    def goToSettings(self):
        self.w1 = SettingDialog.Settings(Consts.SETTINGS_HOTKEY, Consts.DEFAULT_HOTKEY)
        if self.w1.exec():
            print("Success!")
            line = self.w1.get()
            self.ui.hotkey_label.setText(
                Consts.HOTKEY + " " + line)
        else:
            print("Cancel!")
