import sys

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QStackedWidget

import Consts
import MainWindow, BindsWindow, AddBindsWindow

from PyQt6.QtCore import QCoreApplication

if __name__ == '__main__':
    sys.path.append('../')
    sys.path.append('..')
    QCoreApplication.setOrganizationName(Consts.ORGANIZATION_NAME)
    QCoreApplication.setApplicationName(Consts.APPLICATION_NAME)
    app = QApplication(sys.argv)
    widget = QStackedWidget()
    mainWindow = MainWindow.MainWindow(widget)
    bindsWindow = BindsWindow.BindsWindow(widget)
    addBindsWindow = AddBindsWindow.AddBindsWindow(widget)
    widget.addWidget(mainWindow)
    widget.addWidget(bindsWindow)
    widget.addWidget(addBindsWindow)
    widget.setWindowIcon(QIcon(Consts.APPLICATION_ICON))
    widget.setMinimumSize(400, 400)
    widget.show()
    sys.exit(app.exec())