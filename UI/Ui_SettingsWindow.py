# Form implementation generated from reading ui file 'Ui_SettingsWindow.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        Dialog.resize(100, 100)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Ignored, QtWidgets.QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.setObjectName("layout")
        self.label_layout = QtWidgets.QFormLayout()
        self.label_layout.setLabelAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_layout.setObjectName("label_layout")
        self.label = QtWidgets.QLabel(parent=Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Ignored, QtWidgets.QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.label_layout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        self.layout.addLayout(self.label_layout)
        self.button_layout = QtWidgets.QHBoxLayout()
        self.button_layout.setObjectName("button_layout")
        self.change_button = QtWidgets.QPushButton(parent=Dialog)
        self.change_button.setObjectName("change_button")
        self.button_layout.addWidget(self.change_button)
        self.apply_button = QtWidgets.QPushButton(parent=Dialog)
        self.apply_button.setObjectName("apply_button")
        self.button_layout.addWidget(self.apply_button)
        self.layout.addLayout(self.button_layout)
        self.verticalLayout_2.addLayout(self.layout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "TextLabel"))
        self.change_button.setText(_translate("Dialog", "PushButton"))
        self.apply_button.setText(_translate("Dialog", "PushButton"))