import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon
from view.Header1111 import FramelessWindow, TitleBar
#系统入口登录页面
from view.LoginWindow import LoginWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("static/images/aupera-logo.ico"))
    MainWindow = LoginWindow()
    print("我是app.py")
    MainWindow.setWindowTitle("笑脸识别系统")

    MainWindow.setFixedSize(MainWindow.width(), MainWindow.height())
    MainWindow.show()
    sys.exit(app.exec_())