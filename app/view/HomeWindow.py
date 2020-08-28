from PyQt5.QtWidgets import *
from ui.HomeUI import Ui_MainWindow
from view.Camera import Camera
from view.AddCameraDialog import AddCameraDialog
import requests
from view.Header1111 import FramelessWindow, TitleBar


class HomeWindow(Ui_MainWindow,QMainWindow):
    def __init__(self):
        super(HomeWindow, self).__init__()
        self.setupUi(self)
        self.dialog = AddCameraDialog()
        self.initSlot()
        self.initCameraList()
        self.initUI()

    def initUI(self):
        self.setFixedSize(self.width(), self.height())

    def initSlot(self):
        self.listWidget.itemClicked.connect(self.listItemClicked)
        self.nav1.clicked.connect(self.page1Show)
        self.nav2.clicked.connect(self.page2Show)
        self.pushButton.clicked.connect(self.addCameraDialogShow)

    def addCameraDialogShow(self):
        self.dialog.show()

    def init_camera(self):
        """初始化摄像头监控"""
        Camera('rtsp://admin:admin123@172.16.29.100:554', self.label).Open()

    def initCameraList(self):
        self.listWidget.addItem("摄像头1")
        self.listWidget.addItem("摄像头2")

    def listItemClicked(self,Index):
        self.init_camera()
        QMessageBox.information(self,"QListWidget","您选择了："+self.listWidget.item(self.listWidget.row(Index)).text())

    def page1Show(self):
        self.stackedWidget.setCurrentIndex(0)

    def page2Show(self):
        self.stackedWidget.setCurrentIndex(1)