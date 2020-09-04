from PyQt5.QtWidgets import QWidget
from ui.LoginUI import Ui_Form_login
from view.HomeLayout import HomeWindow
from utils.common import SYS_STYLE_LOGIN
from PyQt5.QtGui import QPainter, QPixmap


class LoginWindow(Ui_Form_login,QWidget):
    def __init__(self, parent=None):
        super(LoginWindow, self).__init__(parent)
        self.setupUi(self)
        self.resize(450, 350)
        self.Username = "admin"
        self.Password = "12345678"
        self.setAutoFillBackground(True)
        self.main_window = None
        self.initUI()
        self.initSlot()

    def initUI(self):
        self.setStyleSheet(SYS_STYLE_LOGIN)

    def setBackgroundImage(self):
        painter = QPainter(self)
        pixmap = QPixmap("../static/images/bg.png")
        painter.drawPixmap(self.rect(), pixmap)

    def initSlot(self):
        self.login_btn.clicked.connect(self.doLogin)

    def doLogin(self):
        self.main_window = HomeWindow()
        print(self.main_window)
        self.main_window.show()
        self.close()



