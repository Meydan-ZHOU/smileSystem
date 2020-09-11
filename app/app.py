import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon
#系统入口登录页面
from view.HomeLayout import HomeWindow
from http.server import HTTPServer

from httpserver.httpserver import Resquest

from httpserver.httpclient import HttpClient


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("static/images/aupera-logo.ico"))
    MainWindow = HomeWindow()
    MainWindow.setWindowTitle("人脸识别系统")
    MainWindow.show()
    #HttpClient.do_get("http://172.16.15.88:58888")

    #host = ('', 9002)
    #server = HTTPServer(host, Resquest)
    #print("Starting server, listen at: %s:%s" % host)
    #server.serve_forever()

    sys.exit(app.exec_())