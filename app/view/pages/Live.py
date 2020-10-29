from PyQt5.QtWidgets import QWidget,QListWidgetItem,QHBoxLayout,QLabel,QPushButton,qApp
from PyQt5.QtCore import QSize,Qt
from PyQt5.QtGui import QIcon
from ui.LiveUI import Ui_Form_live
from view.pages.dialog.AddCameraDialog import AddCameraDialog
from view.components.Video import Video
from view.components.MyDialog import MyDialog

from utils.common import msg_box,btn_set_pointer_cursor

from sql.DBHelper import DBHelper

from utils.CameraOnvif import ws_discovery

import qtawesome

class LivePage(Ui_Form_live,QWidget):
    def __init__(self, parent=None):
        super(LivePage, self).__init__(parent)
        self.setupUi(self)
        self._tr = qApp.translate
        self.initUI()
        self.initSlot()
        self.dbHelper = DBHelper()
        self.createTable()
        print("我是 live")

    def getDatas(self):
        self.cameraList = []
        self.videoList = []
        self.getAllCameraList()

    def createTable(self):
        self.dbHelper.create_camera_table()

    def initUI(self):
        self.setObjectName("liveW")
        self.pushButton_add_camera.setIcon(qtawesome.icon('fa.plus',color='#a4a5a8'))
        self.pushButton_onvif.setIcon(qtawesome.icon('fa.search',color='#a4a5a8'))
        self.initVideo()

    def initSlot(self):
        self.pushButton_onvif.clicked.connect(self.discoveryCameraOnvif)

    def discoveryCameraOnvif(self):
        pass
        #cameraList = ws_discovery()
        #print(cameraList)


    def updateCameraListUI(self):
        self.listWidget.clear()
        for camera in self.cameraList:
            name,ip,sn,username,password,url = camera
            item = QListWidgetItem() #创建QListWidgetItem对象
            item.setData(0,camera)
            item.setSizeHint(QSize(200, 50))
            # 总widget
            widget = QWidget()
            # 总的横向布局
            h = QHBoxLayout()
            # 摄像头名字
            label_name = QLabel()
            label_name.setText(name)

            btnIcon = QPushButton()
            btnIcon.setIcon(QIcon('static/images/camera.png'))
            btnIcon.setFixedSize(30,30)
            #删除按钮
            btn = QPushButton()
            btn.setIcon(qtawesome.icon('fa.cog',color='#a4a5a8'))
            btn.setProperty("data",camera)
            btn.setProperty('class','default')
            btn.setFixedSize(30,30)
            btn.clicked.connect(self.handleEditCamera)
            btn_set_pointer_cursor(btn)

            h.addWidget(btnIcon)
            h.addWidget(label_name)
            h.addWidget(btn)
            widget.setLayout(h)
            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item, widget)

    def handleEditCamera(self):
        data = self.sender().property('data')
        self.dialog = AddCameraDialog(data)
        self.dialog.submit_button_click.connect(lambda data: self.updateCamera(data))
        self.dialog.delete_button_click.connect(lambda data: self.handleDeleteCamera(data))
        self.dialog.show()

    def updateCamera(self,data):
        db_back = self.dbHelper.update_camera(data)
        if (db_back):
            pass
        else:
            msg_box(self, self._tr('Form', 'video_open_error'))
        self.getAllCameraList()

    def handleDeleteCamera(self,ip):
        db_back = self.dbHelper.delete_camera(ip)
        if(db_back):
            pass
        else:
            msg_box(self, self._tr('Form', 'video_open_error'))
        self.getAllCameraList()

    def addCameraDialogShow(self):
        self.dialog = AddCameraDialog()
        self.dialog.submit_button_click.connect(lambda data:self.submitAddCamera(data))
        self.dialog.show()

    def getAllCameraList(self):
        db_back = self.dbHelper.select_all_camera()
        self.cameraList = db_back
        self.updateCameraListUI()

    def submitAddCamera(self,camera):
        db_back = self.dbHelper.insert_camera(camera)
        if(db_back):
           pass
        else:
            msg_box(self,self._tr('Form','video_open_error'))
        self.getAllCameraList()

    def initVideo(self):
        count = self.horizontalLayout_video.count()
        for i in range(count):
            self.horizontalLayout_video.takeAt(i).widget().deleteLater()
        """初始化摄像头监控"""

        self.video = Video()
        self.horizontalLayout_video.addWidget(self.video)

    def handleCameraChanged(self,item):
        print("camera changed")
        url = item.data(0)[5]
        name = item.data(0)[0]
        self.video.Open(url,name)