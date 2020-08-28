from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

StyleSheet = """
#Login{
    display:block;
    background:#191d2d;
    color:#fff;
}
"""

class LoginUI(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(500, 300)
        Login.setStyleSheet(StyleSheet)
        grid = QGridLayout(Login)
        grid.setObjectName("gridLayout")
        form = QFormLayout(Login)

        self.username_label = QLabel(Login)
        self.username_label.setObjectName("username_label")
        self.username_lineEdit = QLineEdit(Login)
        self.username_lineEdit.setObjectName("username_lineEdit")

        self.password_label = QLabel(Login)
        self.password_label.setObjectName("password_label")
        self.password_lineEdit = QLineEdit(Login)
        self.password_lineEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        self.password_lineEdit.setObjectName("password_lineEdit")

        self.login_pushButton = QPushButton(Login)
        self.login_pushButton.setObjectName("login_pushButton")

        form.addRow(self.username_label, self.username_lineEdit)
        form.addRow(self.password_label, self.password_lineEdit)

        h = QHBoxLayout(Login)
        h.addWidget(self.login_pushButton)

        self.setLayout(form)
        self.retranslateUI(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUI(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate('Login', "笑脸识别系统"))
        self.username_label.setText(_translate("Login", "用户:"))
        self.username_lineEdit.setText(_translate("Login", "admin"))
        self.password_label.setText(_translate("Login", "密码:"))
        self.password_lineEdit.setText(_translate("Login", "admin"))
        self.login_pushButton.setText(_translate("Login", "登录"))

