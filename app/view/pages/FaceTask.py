from PyQt5.QtWidgets import *
from ui.FaceTaskUI import Ui_Form
from api.index import get_librarys,newTask
from PyQt5.QtCore import QSize,Qt
from view.components.Camera import Camera
import time
from utils.common import CAMERA_LIST
from utils.common import msg_box
from utils.common import SYS_STYLE_COMMON

import socket

class FaceTaskPage(Ui_Form,QWidget):
    def __init__(self, HomeLayout, parent=None):
        super(FaceTaskPage, self).__init__(parent)
        self.setupUi(self)
        self.HomeLayout = HomeLayout
        print("新建人脸任务------------------------------------------------")
        self.hostIp = self.getHostIP()
        self.initData()
        self.getLibraryList()
        self.destroyed.connect(self.handleDestroy)

    def initUI(self):
        self.setStyleSheet(SYS_STYLE_COMMON)

    def getHostIP(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('8.8.8.8', 80))
            ip = s.getsockname()[0]
        finally:
            s.close()

        return ip

    def handleDestroy(self):
        print("新建任务被销毁了")

    def initData(self):
        self.cameraList = CAMERA_LIST
        self.libraryList = []
        self.currentLibrary = {}
        self.libraryCamera = {}

    def libraryHasCamera(self,camera_url):
        cameras = self.libraryCamera[self.currentLibrary['face_lib_id']]['cameras']
        for item in cameras:
            if(item == camera_url):
                return True
            else:
                return False
        return False

    def initCameraListUI(self):
        self.listWidget_camera.clear()
        for camera in self.cameraList:
            item = QListWidgetItem()  # 创建QListWidgetItem对象
            item.setData(0, camera)
            item.setSizeHint(QSize(150, 50))
            # 总widget
            widget = QWidget()
            # 总的横向布局
            layout_main = QHBoxLayout()
            cb = QCheckBox()
            status = self.libraryHasCamera(camera['url'])
            print(status)
            cb.setChecked(status)
            cb.setProperty("data",camera)
            cb.stateChanged.connect(self.cameraCheckedChanged)
            label = QLabel()
            label.setText(camera['ip'])
            layout_main.setAlignment(Qt.AlignLeft|Qt.AlignHCenter)
            btn = QToolButton()
            btn.setText("播放")
            btn.setProperty("data",camera)
            btn.clicked.connect(self.handleCameraClicked)
            # 摄像头编辑按钮
            layout_main.addWidget(cb)
            layout_main.addWidget(label)
            layout_main.addWidget(btn)
            widget.setLayout(layout_main)
            self.listWidget_camera.addItem(item)
            self.listWidget_camera.setItemWidget(item, widget)

    def removeAllList(self):
        count = self.listWidget_camera.children()

    def cameraCheckedChanged(self):
        camera = self.sender().property('data')
        current_lib_id = self.currentLibrary.get('face_lib_id')
        if(self.sender().checkState()==0):
            self.libraryCamera[current_lib_id]['cameras'].remove(camera['url'])
        else:
            self.libraryCamera[current_lib_id]['cameras'].add(camera['url'])


    def getLibraryList(self):
        res = get_librarys()
        if res.status_code == 200:
            self.libraryList = res.json()
            if(type(self.libraryList)==list):
                self.currentLibrary = self.libraryList[0]
                self.initComboboxUI(self.libraryList)
                self.initCameraListUI()
        else:
            self.libraryList = []
            self.currentLibrary = {}

    def initComboboxUI(self,data):
        comboBox = self.comboBox_face_libray
        for index,obj in enumerate(data):
            comboBox.addItem(obj.get('face_lib_name'))
            comboBox.setItemData(index,obj)
            self.libraryCamera[obj.get('face_lib_id')] = {
                "cameras": set(),
                "similarity":float(self.doubleSpinBox_similarity.text())
            }
        comboBox.setCurrentIndex(0)
        comboBox.currentIndexChanged.connect(self.faceLibraryChanged)

    def faceLibraryChanged(self,i):
        self.currentLibrary = self.comboBox_face_libray.itemData(i)
        self.initCameraListUI()
        self.initOtherSettting()

    def goFacePage(self):
        self.HomeLayout.stackedWidget_face.setCurrentIndex(self.HomeLayout.widget_map['page_face'])

    def init_camera(self,url):
        """初始化摄像头监控"""
        Camera(url, self.label_camera).Open()

    def handleCameraClicked(self):
        url = self.sender().property('data')['url']
        self.init_camera(url)

    def smilarityChanged(self):
        library = self.libraryCamera[self.currentLibrary['face_lib_id']]
        similaity = float(self.doubleSpinBox_similarity.text())
        library['similarity'] = similaity

    def initOtherSettting(self):
        library = self.libraryCamera[self.currentLibrary['face_lib_id']]
        similaity = library['similarity']
        self.doubleSpinBox_similarity.setValue(similaity)

    def handleSubmit(self):
        print("submit",self.libraryCamera)
        cams = {}
        libs_arr = []
        libraryCamera = self.libraryCamera
        for library_id in libraryCamera:
            library = libraryCamera[library_id]
            cameras = library['cameras']
            obj = {
                "face_lib_id":library_id,
                "similarity_threshold":library['similarity']
            }
            if(len(cameras)>0):
                libs_arr.append(obj)
            for camera in cameras:
                if(cams.get(camera)==None):
                    cams[camera] = []
                    cams[camera].append(library_id)
                else:
                    cams[camera].append(library_id)

        camera_arr = []
        for url in cams:
            libs = cams[url]
            item = {
                "url":url,
                "face_lib_ids":libs
            }
            camera_arr.append(item)

        params = {
            "task":{
                "cameras":camera_arr,
                "libraries":libs_arr
            },
            "notify": {
                "server": "http://"+self.hostIp+":9002"
            }
        }

        res = newTask(params)
        data = res.json()
        if(res.status_code==200 and data.get('code')==0):
            msg_box(self,"操作成功")
            self.HomeLayout.goFaceMain()
        else:
            msg_box(self,data.get("msg"))

    def handleCancel(self):
        self.getLibraryList()
        print(self.libraryCamera)