# Form implementation generated from reading ui file 'Ui_CycleActionItem.ui'
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
        Form.resize(400, 300)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.list_item_layout = QtWidgets.QVBoxLayout()
        self.list_item_layout.setObjectName("list_item_layout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.name_action_label = QtWidgets.QLabel(parent=Form)
        self.name_action_label.setObjectName("name_action_label")
        self.horizontalLayout.addWidget(self.name_action_label)
        self.edit_button = QtWidgets.QPushButton(parent=Form)
        self.edit_button.setText("")
        self.edit_button.setObjectName("edit_button")
        self.horizontalLayout.addWidget(self.edit_button)
        self.delete_button = QtWidgets.QPushButton(parent=Form)
        self.delete_button.setText("")
        self.delete_button.setObjectName("delete_button")
        self.horizontalLayout.addWidget(self.delete_button)
        self.horizontalLayout.setStretch(0, 8)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)
        self.list_item_layout.addLayout(self.horizontalLayout)
        self.count_layout = QtWidgets.QHBoxLayout()
        self.count_layout.setContentsMargins(10, 10, 10, 10)
        self.count_layout.setSpacing(25)
        self.count_layout.setObjectName("count_layout")
        self.always_button = QtWidgets.QRadioButton(parent=Form)
        self.always_button.setObjectName("always_button")
        self.count_layout.addWidget(self.always_button)
        self.count_button = QtWidgets.QRadioButton(parent=Form)
        self.count_button.setObjectName("count_button")
        self.count_layout.addWidget(self.count_button)
        self.count_edit = QtWidgets.QSpinBox(parent=Form)
        self.count_edit.setObjectName("count_edit")
        self.count_edit.setMinimum(1)
        self.count_edit.setValue(1)
        self.count_layout.addWidget(self.count_edit)
        self.count_layout.setStretch(0, 5)
        self.count_layout.setStretch(1, 2)
        self.count_layout.setStretch(2, 3)
        self.list_item_layout.addLayout(self.count_layout)
        self.list_item_layout.setStretch(0, 1)
        self.verticalLayout_2.addLayout(self.list_item_layout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.always_button.setText(_translate("Form", Consts.ALWAYS))
        self.count_button.setText(_translate("Form", Consts.REPEAT))
