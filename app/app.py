import sys,threading
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon
#系统入口登录页面
from view.HomeLayout import HomeWindow

from http.server import HTTPServer

from httpserver.httpserver import Resquest

def newBackServer():
    host = ('', 9002)
    server = HTTPServer(host, Resquest)
    print("Starting server, listen at: %s:%s" % host)
    server.serve_forever()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("static/images/aupera-logo.ico"))
    MainWindow = HomeWindow()
    MainWindow.setWindowTitle("人脸识别系统")
    MainWindow.show()

    th = threading.Thread(target=newBackServer, name='backThread')
    th.start()

    sys.exit(app.exec_())