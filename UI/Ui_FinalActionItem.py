# Form implementation generated from reading ui file 'Ui_FinalActionItem.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(661, 193)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.list_item_layout = QtWidgets.QHBoxLayout()
        self.list_item_layout.setObjectName("list_item_layout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.nameAction_label = QtWidgets.QLabel(parent=Form)
        self.nameAction_label.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.nameAction_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.nameAction_label.setObjectName("nameAction_label")
        self.verticalLayout.addWidget(self.nameAction_label)
        self.action_label = QtWidgets.QLabel(parent=Form)
        self.action_label.setObjectName("action_label")
        self.verticalLayout.addWidget(self.action_label)
        self.list_item_layout.addLayout(self.verticalLayout)
        self.edit_button = QtWidgets.QPushButton(parent=Form)
        self.edit_button.setObjectName("edit_button")
        self.list_item_layout.addWidget(self.edit_button)
        self.delete_button = QtWidgets.QPushButton(parent=Form)
        self.delete_button.setObjectName("delete_button")
        self.list_item_layout.addWidget(self.delete_button)
        self.list_item_layout.setStretch(0, 8)
        self.list_item_layout.setStretch(1, 1)
        self.list_item_layout.setStretch(2, 1)
        self.horizontalLayout_2.addLayout(self.list_item_layout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.nameAction_label.setText(_translate("Form", "TextLabel"))
        self.action_label.setText(_translate("Form", "TextLabel!"))
        self.edit_button.setText(_translate("Form", ""))
        self.delete_button.setText(_translate("Form", ""))
