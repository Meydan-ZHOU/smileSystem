import sys,threading
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon,QFont
from PyQt5.QtCore import Qt,QSettings,QCoreApplication,QTranslator,QVersionNumber,QT_VERSION_STR
from PyQt5 import QtCore
from view.LoginWindow import LoginWindow

from http.server import HTTPServer

from httpserver.httpserver import Resquest

def newBackServer():
    host = ('', 9002)
    server = HTTPServer(host, Resquest)
    print("Starting server, listen at %s:%s" % host)
    server.serve_forever()


if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    #设置字体大小，自适应分辨率
    # QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    # v_compare = QVersionNumber(5, 6, 0)
    # v_current, _ = QVersionNumber.fromString(QT_VERSION_STR)  # 获取当前Qt版本
    # if QVersionNumber.compare(v_current, v_compare) >= 0:
    #     QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)  # Qt从5.6.0开始，支持High-DPI
    #     app = QApplication(sys.argv)
    # else:

    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    font = QFont()
    pointsize = font.pointSize()
    print("pointsize",pointsize*90/72)
    font.setPointSize(pointsize*90/72)
    app.setFont(font)

    #设置语言
    QCoreApplication.setOrganizationName('Aupera')
    QCoreApplication.setApplicationName('My client')
    regSettings = QSettings(QCoreApplication.organizationName(),QCoreApplication.applicationName())

    language = regSettings.value('Language','EN')
    print("language---------",language)
    trans = QTranslator()  # 翻译器对象
    if language == 'EN':
        trans.load('./appLang_EN.qm')
        regSettings.setValue('Language', 'EN')
    else:
        trans.load('./appLang_CN.qm')
        regSettings.setValue('Language', 'CN')
    app.installTranslator(trans)

    #设置客户端图标
    app.setWindowIcon(QIcon("./static/images/aupera-logo.ico"))

    MainWindow = LoginWindow()
    # 无边框
    MainWindow.setWindowFlags(Qt.FramelessWindowHint)  # 隐藏边框
    # 鼠标跟踪
    MainWindow.setMouseTracking(True)
    MainWindow.show()

    #开启接收报警通知服务
    th = threading.Thread(target=newBackServer, name='backThread')
    th.setDaemon(True)
    th.start()

    sys.exit(app.exec_())
