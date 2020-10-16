import sys,threading
from PyQt5.QtWidgets import QApplication,QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
#系统入口登录页面
from view.HomeLayout import HomeWindow
from view.LoginWindow import LoginWindow

from http.server import HTTPServer

from httpserver.httpserver import Resquest

def newBackServer():
    host = ('', 9002)
    server = HTTPServer(host, Resquest)
    print("Starting server, listen at: %s:%s" % host)
    server.serve_forever()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./static/images/aupera-logo.ico"))
    MainWindow = LoginWindow()
    MainWindow.setWindowTitle("人脸识别系统")
    # 无边框
    MainWindow.setWindowFlags(Qt.FramelessWindowHint)  # 隐藏边框
    # 鼠标跟踪
    MainWindow.setMouseTracking(True)
    MainWindow.show()

    th = threading.Thread(target=newBackServer, name='backThread')
    th.setDaemon(True)
    th.start()

    sys.exit(app.exec_())
