import sys,threading
from PyQt5.QtWidgets import QApplication,QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt,QSettings,QCoreApplication,QTranslator
from PyQt5 import QtCore
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
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    #设置语言
    QCoreApplication.setOrganizationName('Aupera')
    QCoreApplication.setApplicationName('My client')
    regSettings = QSettings(QCoreApplication.organizationName(),QCoreApplication.applicationName())
    language = regSettings.value('Language','EN')
    app.trans = QTranslator() #翻译器对象
    print("language____________",language)
    if language == 'EN':
        app.trans.load('./appLang_EN.qm')
        regSettings.setValue('Language', 'EN')
    else:
        app.trans.load('./appLang_CN.qm')
        regSettings.setValue('Language', 'CN')

    app.installTranslator(app.trans)

    app.setWindowIcon(QIcon("./static/images/aupera-logo.ico"))
    MainWindow = LoginWindow()
    # 无边框
    MainWindow.setWindowFlags(Qt.FramelessWindowHint)  # 隐藏边框

    # 鼠标跟踪
    MainWindow.setMouseTracking(True)
    MainWindow.show()

    th = threading.Thread(target=newBackServer, name='backThread')
    th.setDaemon(True)
    th.start()

    sys.exit(app.exec_())
