from PyQt5.QtWidgets import QWidget,QListWidgetItem,QHBoxLayout,QLabel,QPushButton
from PyQt5.QtCore import QSize
from ui.LiveUI import Ui_Form
from view.pages.dialog.AddCameraDialog import AddCameraDialog
from view.components.Video import Video

from utils.common import msg_box

from sql.DBHelper import DBHelper


class LivePage(Ui_Form,QWidget):
    def __init__(self, parent=None):
        super(LivePage, self).__init__(parent)
        self.setupUi(self)
        self.initUI()
        self.cameraList = []
        self.dbHelper = DBHelper()
        self.createTable()
        self.getAllCameraList()
        print("我是 live")


    def createTable(self):
        self.dbHelper.create_camera_table()

    def initUI(self):
        self.setObjectName("liveW")
        self.init_camera()

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

            #删除按钮
            btn = QPushButton()
            btn.setText("编辑")
            btn.setFixedSize(50, 25)
            btn.setProperty("data",camera)
            btn.clicked.connect(self.handleEditCamera)

            h.addWidget(label_name)
            h.addWidget(btn)
            h.setStretch(0,1)
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
            msg_box(self, "操作成功")
        else:
            msg_box(self, "操作失败")
        self.getAllCameraList()

    def handleDeleteCamera(self,ip):
        db_back = self.dbHelper.delete_camera(ip)
        if(db_back):
            msg_box(self,"操作成功")
        else:
            msg_box(self,"操作失败")
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
            msg_box(self, "操作成功")
        else:
            msg_box(self, "操作失败")
        self.getAllCameraList()

    def init_camera(self):
        """初始化摄像头监控"""
        print(self.widget_video_show.width())
        self.video = Video()
        self.horizontalLayout_video.addWidget(self.video)

    def handleCameraChanged(self,item):
        url = item.data(0)[5]
        name = item.data(0)[0]
        print(self.video)
        self.video.Open(url,name)