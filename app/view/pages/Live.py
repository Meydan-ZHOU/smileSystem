from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize
from ui.LiveUI import Ui_Form
from view.pages.dialog.AddCameraDialog import AddCameraDialog
from view.components.Camera import Camera


class LivePage(Ui_Form,QWidget):
    def __init__(self, parent=None):
        super(LivePage, self).__init__(parent)
        self.setupUi(self)
        self.initUI()
        self.cameraList = [
            {
                "name": "摄像头1",
                "ip": "172.16.134.134",
                "url": "rtsp://admin:admin123@172.16.134.134:554"
            },
            {
                "name": "摄像头2",
                "ip": "172.16.233.100",
                "url": "rtsp://admin:admin123@172.16.233.100:554"
            },
            {
                "name": "摄像头3",
                "ip": "172.16.29.100",
                "url": "rtsp://admin:admin123@172.16.29.100:554"
            },
        ]
        self.initCameraListUI()

    def initSlot(self):
        pass

    def initUI(self):
        self.dialog = AddCameraDialog()

    def getItemWidget(self,data):
        ip = data['ip']
        #总widget
        widget = QWidget()
        #总的横向布局
        layout_main = QHBoxLayout()
        #摄像头名字
        camera_text = QLabel(ip)
        #摄像头编辑按钮
        layout_main.addWidget(camera_text)
        widget.setLayout(layout_main)

        return widget

    def initCameraListUI(self):
        for camera in self.cameraList:
            item = QListWidgetItem() #创建QListWidgetItem对象
            item.setData(0,camera)
            item.setSizeHint(QSize(200, 50))
            widget = self.getItemWidget(camera)
            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item, widget)

    def editCamera(self,data):
        print(data)

    def addCameraDialogShow(self):
        self.dialog.raise_()
        self.dialog.show()
        print("添加摄像头啦")

    def init_camera(self,url):
        """初始化摄像头监控"""
        Camera(url, self.label_video_show).Open()

    def handleCameraChanged(self,item):
        url = item.data(0)['url']
        self.init_camera(url)
