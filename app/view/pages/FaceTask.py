import socket

from PyQt5.QtWidgets import QWidget,QListWidgetItem,QHBoxLayout,QCheckBox,QLabel,QToolButton,qApp
from ui.FaceTaskUI import Ui_Form_new_task
from PyQt5.QtCore import QSize,Qt

from view.components.Video import Video

from api.index import newTask
from utils.common import msg_box,btn_set_pointer_cursor

from sql.DBHelper import DBHelper

import qtawesome

class FaceTaskPage(Ui_Form_new_task,QWidget):
    def __init__(self, HomeLayout, parent=None):
        super(FaceTaskPage, self).__init__(parent)
        self.setupUi(self)
        self._tr = qApp.translate
        self.HomeLayout = HomeLayout
        print("新建人脸任务------------------------------------------------")
        self.dbHelper = DBHelper()
        self.hostIp = self.getHostIP()
        self.initUI()

    def getDatas(self):
        self.initData()
        self.getLibraryList()
        self.getAllCameraList()

    def initUI(self):
        self.setObjectName("faceTask")
        self.init_camera()

    def getHostIP(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('8.8.8.8', 80))
            ip = s.getsockname()[0]
        finally:
            s.close()
        return ip

    def getAllCameraList(self):
        self.cameraList = []
        db_back = self.dbHelper.select_all_camera()
        self.cameraList = db_back
        self.updateCameraListUI()

    def initData(self):
        self.comboBox_face_libray.clear()
        self.cameraList = []
        self.libraryList = []
        self.currentLibrary = None
        self.libraryCamera = {}

    def libraryHasCamera(self,camera_url):
        if(self.currentLibrary==None):
            return False
        lib_name,lib_id = self.currentLibrary
        cameras = self.libraryCamera[lib_id]['cameras']
        for item in cameras:
            if(item == camera_url):
                return True
            else:
                return False
        return False

    def updateCameraListUI(self):
        self.listWidget_camera.clear()
        for camera in self.cameraList:
            name, ip, sn, username, password, url = camera
            item = QListWidgetItem()  # 创建QListWidgetItem对象
            item.setData(0, camera)
            item.setSizeHint(QSize(150, 50))
            # 总widget
            widget = QWidget()
            # 总的横向布局
            h = QHBoxLayout()
            cb = QCheckBox()
            btn_set_pointer_cursor(cb)
            status = self.libraryHasCamera(url)
            cb.setChecked(status)
            cb.setProperty("url",url)
            cb.stateChanged.connect(self.cameraCheckedChanged)
            label = QLabel()
            label.setText(name)
            h.setAlignment(Qt.AlignLeft|Qt.AlignHCenter)
            btn = QToolButton()
            btn.setIcon(qtawesome.icon('fa.play-circle',color='#a4a5a8'))
            btn.setStyleSheet("background-color:transparent;")
            btn.setProperty("data",(url,name))
            btn.clicked.connect(self.handleCameraClicked)
            btn_set_pointer_cursor(btn)
            # 摄像头编辑按钮
            h.addWidget(cb)
            h.addWidget(label)
            h.addWidget(btn)
            h.setStretch(1,2)
            widget.setLayout(h)
            self.listWidget_camera.addItem(item)
            self.listWidget_camera.setItemWidget(item, widget)

    def cameraCheckedChanged(self):
        if self.currentLibrary==None:
            return
        lib_name, lib_id = self.currentLibrary
        url = self.sender().property('url')
        if(self.sender().checkState()==0):
            self.libraryCamera[lib_id]['cameras'].remove(url)
        else:
            self.libraryCamera[lib_id]['cameras'].add(url)

        print(self.libraryCamera)

    def getLibraryList(self):
        self.libraryList = []
        self.currentLibrary = None
        db_back = self.dbHelper.select_all_library()
        print("db_back",db_back)
        if (db_back):
            self.libraryList = db_back
            if len(self.libraryList) > 0:
                self.currentLibrary = self.libraryList[0]
            else:
                self.currentLibrary = None
        else:
            self.libraryList = []
            self.currentLibrary = None

        print("self.currentLibrary-----", self.currentLibrary)
        self.updateLibraryComboboxUI(self.libraryList)
        self.updateCameraListUI()


    def updateLibraryComboboxUI(self,library):
        self.comboBox_face_libray.clearEditText()
        comboBox = self.comboBox_face_libray
        print("updateLibraryComboboxUI lib", library)
        for index,lib in enumerate(library):
            lib_name,lib_id = lib
            comboBox.addItem(lib_name)
            comboBox.setItemData(index,lib)
            if self.libraryCamera.get(lib_id)==None:
                self.libraryCamera[lib_id] = {
                    "cameras": set(),
                    "similarity": float(self.doubleSpinBox_similarity.text())
                }
        comboBox.setCurrentIndex(0)
        comboBox.currentIndexChanged.connect(self.faceLibraryChanged)

    def faceLibraryChanged(self,i):
        if(i<0 or self.comboBox_face_libray.itemData(i) == None):
            return
        self.currentLibrary = self.comboBox_face_libray.itemData(i)
        print(i, 'self.currentLibrary',self.currentLibrary)
        self.updateCameraListUI()
        self.initOtherSettting()

    def goFacePage(self):
        self.HomeLayout.stackedWidget_face.setCurrentIndex(self.HomeLayout.widget_map['page_face'])

    def init_camera(self):
        """初始化摄像头监控"""
        self.video = Video()
        self.horizontalLayout_video.addWidget(self.video)

    def handleCameraClicked(self):
        url,name = self.sender().property('data')
        self.video.Open(url,name)

    def smilarityChanged(self):
        if(self.currentLibrary==None):
            return
        lib_name, lib_id = self.currentLibrary
        library = self.libraryCamera[lib_id]
        similarity = float(self.doubleSpinBox_similarity.text())
        library['similarity'] = similarity

    def initOtherSettting(self):
        if (self.currentLibrary == None):
            return
        lib_name, lib_id = self.currentLibrary
        library = self.libraryCamera[lib_id]
        similarity = library['similarity']
        self.doubleSpinBox_similarity.setValue(similarity)

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



        if(len(camera_arr)==0):
            msg_box(self,self._tr('Form','camera_empty'))
            return

        if (len(libs_arr) == 0):
            msg_box(self, self._tr('Form', 'library_empty'))
            return

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
        if res:
            data = res.json()
            if(res.status_code==200 and data.get('code')==0):
                self.HomeLayout.goFaceMain()
            else:
                msg_box(self,data.get("msg"))

    def handleCancel(self):
        self.getLibraryList()