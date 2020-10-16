from PyQt5.QtWidgets import *
from ui.FaceUI import Ui_Form
from view.pages.FaceLibrary import FaceLibraryPage
from view.pages.FaceTask import FaceTaskPage
from view.pages.FaceMain import FaceMainPage
from view.pages.FaceTaskNotify import FaceTaskNotifyPage
from view.pages.FaceNotifyDetail import FaceNotifyDetailPage

from utils.common import SYS_STYLE_COMMON

class FacePage(Ui_Form,QWidget):
    def __init__(self, HomeLayout, parent=None):
        super(FacePage, self).__init__(parent)
        self.setupUi(self)
        self.HomeLayout = HomeLayout
        print("我是face")
        self.beforeStackedIndex = 0
        self.initUI()
        self.initStackedWidget()
        self.initSlot()

    def initUI(self):
        self.setObjectName("faceW")
        self.pushButton_second_back.setText("任务监控")
        self.secondPushbuttonHide()
        self.line_2.hide()
        self.setStyleSheet(SYS_STYLE_COMMON)

    def initSlot(self):
        self.pushButton_second_back.clicked.connect(self.goFaceTaskNotifyWidget)
        self.stackedWidget.currentChanged.connect(self.currentStackedIndexChanged)

    def initStackedWidget(self):
        self.stackedWidget = QStackedWidget()
        self.main = FaceMainPage(self)
        self.library = FaceLibraryPage(self)
        self.task = FaceTaskPage(self)
        self.taskNotify = FaceTaskNotifyPage(self)
        self.notifyDetail = FaceNotifyDetailPage(self)
        self.stackedWidget.addWidget(self.main)
        self.stackedWidget.addWidget(self.library)
        self.stackedWidget.addWidget(self.task)
        self.stackedWidget.addWidget(self.taskNotify)
        self.stackedWidget.addWidget(self.notifyDetail)
        self.gridLayout_main.addWidget(self.stackedWidget)

    def currentStackedIndexChanged(self,index):
        currentWidget = self.stackedWidget.currentWidget()
        objectName = currentWidget.objectName()
        print("face layout changed---", self.beforeStackedIndex,'========',index, '----------', objectName)

        if(not objectName == 'faceNotifyDetail'):
            self.secondPushbuttonHide()

        if(not objectName == 'faceTask' and self.beforeStackedIndex==2):
            self.task.video.Close()

    def setStackedPageIndex(self, index):
        self.stackedWidget.setCurrentIndex(index)

    def goFaceMain(self):
        self.label_2.setText("任务列表")
        self.setStackedPageIndex(0)
        self.beforeStackedIndex = 0
        if(False == self.main.isGettingData):
            self.main.getDatas()
        else:
            print("正在请求task数据尼")

    def goLibraryManagementPage(self):
        self.label_2.setText("人脸库管理")
        self.setStackedPageIndex(1)
        self.beforeStackedIndex = 1
        self.library.getDatas()

    def goFaceTaskPage(self):
        self.label_2.setText("新增任务")
        self.setStackedPageIndex(2)
        self.beforeStackedIndex = 2
        self.task.getDatas()

    def goFaceTaskNotifyWidget(self):
        self.label_2.setText("任务监控")
        self.setStackedPageIndex(3)
        self.beforeStackedIndex = 3

    def goFaceTaskNotify(self,task_id):
        self.goFaceTaskNotifyWidget()
        self.taskNotify.current_task_id = task_id
        self.taskNotify.getDatas()

    def goFaceNotifyDetailPage(self,data):
        self.label_2.setText("报警详情")
        self.setStackedPageIndex(4)
        self.beforeStackedIndex = 4
        self.secondPushbuttonShow()
        self.notifyDetail.notify = data['notify']
        self.notifyDetail.getDatas()


    def secondPushbuttonShow(self):
        self.pushButton_second_back.show()
        self.line_2.show()

    def secondPushbuttonHide(self):
        self.pushButton_second_back.hide()
        self.line_2.hide()