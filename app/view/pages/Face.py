from PyQt5.QtWidgets import QWidget,qApp,QStackedWidget
from ui.FaceUI import Ui_Form_face
from view.pages.FaceLibrary import FaceLibraryPage
from view.pages.FaceTask import FaceTaskPage
from view.pages.FaceMain import FaceMainPage
from view.pages.FaceTaskNotify import FaceTaskNotifyPage
from view.pages.FaceNotifyDetail import FaceNotifyDetailPage

from utils.common import SYS_STYLE_COMMON

class FacePage(Ui_Form_face,QWidget):
    def __init__(self, HomeLayout, parent=None):
        super(FacePage, self).__init__(parent)
        self.setupUi(self)
        self._tr = qApp.translate
        self.HomeLayout = HomeLayout
        print("我是face")
        self.beforeStackedIndex = 0
        self.initUI()
        self.initStackedWidget()
        self.initSlot()

    def initUI(self):
        self.setObjectName("faceW")
        self.pushButton_second_back.setText(self._tr("Form", "task_monitor"))
        self.secondPushbuttonHide()
        self.setStyleSheet(SYS_STYLE_COMMON)
        self.pushButton_face_back_2.hide()
        self.label.hide()

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

        if(objectName == 'faceNotifyDetail' or objectName == 'faceNotify'):
            self.pushButton_face_back_2.setText(self._tr("Form", "task_list"))
        else:
            self.pushButton_face_back_2.setText(self._tr("Form", "face_recognize"))

        if (objectName == 'faceMain'):
            self.pushButton_face_back_2.hide()
            self.label.hide()
        else:
            self.pushButton_face_back_2.show()
            self.label.show()

    def setStackedPageIndex(self, index):
        self.stackedWidget.setCurrentIndex(index)

    def goFaceMain(self):
        self.pushButton.setText(self._tr("Form", "task_list"))
        self.setStackedPageIndex(0)
        self.beforeStackedIndex = 0
        if(False == self.main.isGettingData):
            self.main.getDatas()
        else:
            print("正在请求task数据尼")

    def goLibraryManagementPage(self):
        self.pushButton.setText(self._tr("Form", "face_manage"))
        self.setStackedPageIndex(1)
        self.beforeStackedIndex = 1
        self.library.getDatas()

    def goFaceTaskPage(self):
        self.pushButton.setText(self._tr("Form", "new_task"))
        self.setStackedPageIndex(2)
        self.beforeStackedIndex = 2
        self.task.getDatas()

    def goFaceTaskNotifyWidget(self):
        self.pushButton.setText(self._tr("Form", "task_monitor"))
        self.setStackedPageIndex(3)
        self.beforeStackedIndex = 3

    def goFaceTaskNotify(self,task_id):
        self.goFaceTaskNotifyWidget()
        self.taskNotify.current_task_id = task_id
        self.taskNotify.getDatas()

    def goFaceNotifyDetailPage(self,data):
        self.pushButton.setText(self._tr("Form", "monitor_detail"))
        self.setStackedPageIndex(4)
        self.beforeStackedIndex = 4
        self.secondPushbuttonShow()
        self.notifyDetail.notify = data['notify']
        self.notifyDetail.getDatas()


    def secondPushbuttonShow(self):
        self.pushButton_second_back.show()
        self.label_3.show()

    def secondPushbuttonHide(self):
        self.pushButton_second_back.hide()
        self.label_3.hide()