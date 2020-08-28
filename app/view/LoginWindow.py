import sys
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget,QMainWindow
from ui.LoginUI import Ui_MainWindow
from view.HomeWindow import HomeWindow
from utils.common import SYS_STYLE

class LoginWindow(Ui_MainWindow,QMainWindow):
    def __init__(self, parent=None):
        super(LoginWindow, self).__init__(parent)
        self.resize(200, 200)
        self.setupUi(self)
        self.Username = "admin"
        self.Password = "12345678"
        self.setAutoFillBackground(True)
        self.main_window = None
        self.initUI()
        self.initSlot()

    def initUI(self):
        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
        self.setStyleSheet(SYS_STYLE)

    def initSlot(self):
        self.pushButton.clicked.connect(self.doLogin)

    def doLogin(self):
        self.main_window = HomeWindow()
        print(self.main_window)
        self.main_window.show()
        self.close()




