from PyQt5.QtWidgets import *
from ui.HomeLayoutUI import Ui_Form_home
from utils.common import SYS_STYLE_HOME
from view.pages.Live import LivePage
from view.pages.Face import FacePage
from view.pages.FaceLibrary import FaceLibraryPage

class HomeWindow(Ui_Form_home,QWidget):
    def __init__(self):
        super(HomeWindow, self).__init__()
        self.widget_map = {
            "page_live": 0,
            "page_face": 1,
            "page_face_library": 2,
            "page_face_task_management": 3
        }

        self.setupUi(self)
        self.initSlot()
        self.initUI()
        self.initPages()
        self.stackedWidget_face.setCurrentIndex(self.widget_map['page_face_library'])

    def initUI(self):
        self.setStyleSheet(SYS_STYLE_HOME)
        self.pushButton_live.setProperty('isActive',"active")

    def initPages(self):
        live = LivePage(self)
        face = FacePage(self)
        faceLibrary = FaceLibraryPage(self)
        self.gridLayout_live.addWidget(live)
        self.gridLayout_face.addWidget(face)
        self.gridLayout_library.addWidget(faceLibrary)

    def setPushbuttonStatus(self,index):
        print("page",index)


    def goLivePage(self):
        self.stackedWidget_face.setCurrentIndex(self.widget_map['page_live'])

    def goFaceManagementPage(self):
        self.stackedWidget_face.setCurrentIndex(self.widget_map['page_face'])

    def initSlot(self):
        pass

    def addCameraDialogShow(self):
        pass

    def init_camera(self):
        """初始化摄像头监控"""
        pass
        #Camera('rtsp://admin:admin123@172.16.29.100:554', self.label).Open()

    def initCameraList(self):
        self.listWidget.addItem("摄像头1")
        self.listWidget.addItem("摄像头2")

    def listItemClicked(self,Index):
        self.init_camera()
        QMessageBox.information(self,"QListWidget","您选择了："+self.listWidget.item(self.listWidget.row(Index)).text())