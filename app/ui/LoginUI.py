# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(467, 350)
        MainWindow.setMinimumSize(QtCore.QSize(2, 0))
        MainWindow.setToolTipDuration(1)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setAutoFillBackground(True)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(100, 40, 251, 261))
        self.widget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.widget.setAutoFillBackground(True)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setContentsMargins(-1, -1, 0, -1)
        self.formLayout.setHorizontalSpacing(8)
        self.formLayout.setVerticalSpacing(22)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setAutoFillBackground(False)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.passwordInput = QtWidgets.QLineEdit(self.widget)
        self.passwordInput.setAutoFillBackground(False)
        self.passwordInput.setText("")
        self.passwordInput.setObjectName("passwordInput")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.passwordInput)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setAutoRepeat(False)
        self.pushButton.setObjectName("pushButton")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.pushButton)
        self.usernameInput = QtWidgets.QLineEdit(self.widget)
        self.usernameInput.setAutoFillBackground(False)
        self.usernameInput.setObjectName("usernameInput")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.usernameInput)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "用户名"))
        self.label_2.setText(_translate("MainWindow", "密码"))
        self.pushButton.setText(_translate("MainWindow", "登录"))
