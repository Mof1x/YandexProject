# Form implementation generated from reading ui file 'Ui_ActionItem.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets

import Consts


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(605, 464)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.list_item_layout = QtWidgets.QVBoxLayout()
        self.list_item_layout.setObjectName("list_item_layout")
        self.delete_layout = QtWidgets.QHBoxLayout()
        self.delete_layout.setObjectName("delete_layout")
        self.widget = QtWidgets.QWidget(parent=Form)
        self.widget.setObjectName("widget")
        self.delete_layout.addWidget(self.widget)
        self.delete_button = QtWidgets.QPushButton(parent=Form)
        self.delete_button.setObjectName("delete_button")
        self.delete_layout.addWidget(self.delete_button)
        self.delete_layout.setStretch(0, 9)
        self.delete_layout.setStretch(1, 1)
        self.list_item_layout.addLayout(self.delete_layout)
        self.cycle_button = QtWidgets.QPushButton(parent=Form)
        self.cycle_button.setObjectName("cycle_button")
        self.list_item_layout.addWidget(self.cycle_button)
        self.action_layout = QtWidgets.QHBoxLayout()
        self.action_layout.setObjectName("action_layout")
        self.mouse_button = QtWidgets.QPushButton(parent=Form)
        self.mouse_button.setObjectName("mouse_button")
        self.action_layout.addWidget(self.mouse_button)
        self.keyboard_button = QtWidgets.QPushButton(parent=Form)
        self.keyboard_button.setObjectName("keyboard_button")
        self.action_layout.addWidget(self.keyboard_button)
        self.timer_button = QtWidgets.QPushButton(parent=Form)
        self.timer_button.setObjectName("timer_button")
        self.action_layout.addWidget(self.timer_button)
        self.list_item_layout.addLayout(self.action_layout)
        self.verticalLayout_2.addLayout(self.list_item_layout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.delete_button.setText(_translate("Form", ""))
        self.cycle_button.setText(_translate("Form", Consts.CYCLE))
        self.mouse_button.setText(_translate("Form", Consts.MOUSE))
        self.keyboard_button.setText(_translate("Form", Consts.KEYBOARD))
        self.timer_button.setText(_translate("Form", Consts.TIMER))
