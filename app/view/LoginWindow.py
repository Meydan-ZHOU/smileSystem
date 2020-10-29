from PyQt5.QtWidgets import QWidget,QDesktopWidget
from PyQt5.QtGui import QIcon
from ui.LoginUI import Ui_Form_login
from view.HomeLayout import HomeWindow
from utils.common import SYS_STYLE_COMMON
from view.components.Header import Header


class LoginWindow(Ui_Form_login,QWidget):
    def __init__(self, parent=None):
        super(LoginWindow, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(480,480)
        self.Username = "admin"
        self.Password = "12345678"
        self.setAutoFillBackground(True)
        self.main_window = None
        self.initUI()
        self.initSlot()
        print("我是登录页面")

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        self.move((screen.width() - self.width()) / 2,
                  (screen.height() - self.height()) / 2)

    def initUI(self):
        self.setStyleSheet(SYS_STYLE_COMMON)
        self.pushButton_username.setIcon(QIcon("static/images/username.png"))
        self.pushButton_password.setIcon(QIcon("static/images/password.png"))
        self.initHeader()

    def initHeader(self):
        header = Header(self)
        self.horizontalLayout.addWidget(header)

    def initSlot(self):
        self.login_btn.clicked.connect(self.doLogin)

    def doLogin(self):
        self.main_window = HomeWindow()
        self.main_window.show()
        self.close()



