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
        self.initUI()
        self.HomeLayout = HomeLayout
        print("我是face")
        self.goFaceMain()

    def initUI(self):
        self.setObjectName("faceW")
        self.setStyleSheet(SYS_STYLE_COMMON)

    def goFaceMain(self):
        self.label.setText("任务列表")
        main = FaceMainPage(self)
        self.layoutPage(main)

    def goFaceTaskNotify(self,task_id):
        self.label.setText("任务监控")
        taskNotify = FaceTaskNotifyPage(self,task_id)
        self.layoutPage(taskNotify)

    def goLibraryManagementPage(self):
        self.label.setText("人脸库管理")
        library = FaceLibraryPage(self)
        self.layoutPage(library)

    def goFaceTaskPage(self):
        self.label.setText("新建任务")
        task = FaceTaskPage(self)
        self.layoutPage(task)

    def goFaceNotifyDetailPage(self,data):
        self.label.setText("报警详情")
        notifyDetail = FaceNotifyDetailPage(self,data)
        self.layoutPage(notifyDetail)

    def layoutPage(self,page):
        self.clearGridLayout()
        self.gridLayout_main.addWidget(page, 0, 0, 1, 1)

    def clearGridLayout(self):
        count = self.gridLayout_main.count()
        for i in range(count):
            self.gridLayout_main.takeAt(i).widget().deleteLater()



