# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MyDialogUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(972, 671)
        Form.setAutoFillBackground(True)
        self.label_mask = QtWidgets.QLabel(Form)
        self.label_mask.setGeometry(QtCore.QRect(10, -10, 961, 631))
        self.label_mask.setStyleSheet("background-color:rgba(0,0,0,0.5)")
        self.label_mask.setText("")
        self.label_mask.setObjectName("label_mask")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(190, 110, 581, 331))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_title = QtWidgets.QWidget(self.widget)
        self.widget_title.setMaximumSize(QtCore.QSize(16777215, 30))
        self.widget_title.setObjectName("widget_title")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_title)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_title = QtWidgets.QLabel(self.widget_title)
        self.label_title.setText("")
        self.label_title.setObjectName("label_title")
        self.horizontalLayout.addWidget(self.label_title)
        spacerItem = QtWidgets.QSpacerItem(558, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.widget_title)
        self.pushButton.setMaximumSize(QtCore.QSize(20, 20))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addWidget(self.widget_title)
        self.widget_content = QtWidgets.QWidget(self.widget)
        self.widget_content.setObjectName("widget_content")
        self.verticalLayout.addWidget(self.widget_content)
        self.widget_operates = QtWidgets.QWidget(self.widget)
        self.widget_operates.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widget_operates.setObjectName("widget_operates")
        self.pushButton_submit = QtWidgets.QPushButton(self.widget_operates)
        self.pushButton_submit.setGeometry(QtCore.QRect(380, 10, 75, 23))
        self.pushButton_submit.setObjectName("pushButton_submit")
        self.pushButton_cancel = QtWidgets.QPushButton(self.widget_operates)
        self.pushButton_cancel.setGeometry(QtCore.QRect(480, 10, 75, 23))
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.verticalLayout.addWidget(self.widget_operates)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "x"))
        self.pushButton_submit.setText(_translate("Form", "submit"))
        self.pushButton_cancel.setText(_translate("Form", "cancel"))
