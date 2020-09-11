from PyQt5.QtWidgets import *
from ui.FaceUI import Ui_Form
from utils.common import newGridLayout
from view.pages.FaceLibrary import FaceLibraryPage
from view.pages.FaceTask import FaceTaskPage
from view.pages.FaceMain import FaceMainPage

class FacePage(Ui_Form,QWidget):
    def __init__(self, HomeLayout, parent=None):
        super(FacePage, self).__init__(parent)
        self.setupUi(self)
        self.HomeLayout = HomeLayout
        print("我是face")
        self.goFaceMain()

    def initUI(self):
        self.setObjectName("faceW")

    def goFaceMain(self):
        self.label.setText("任务列表")
        main = FaceMainPage(self)
        self.layoutPage(main)

    def goLibraryManagementPage(self):
        self.label.setText("人脸库管理")
        library = FaceLibraryPage(self)
        self.layoutPage(library)

    def goFaceTaskPage(self):
        self.label.setText("新建任务")
        task = FaceTaskPage(self)
        self.layoutPage(task)

    def layoutPage(self,page):
        self.clearGridLayout()
        self.gridLayout_main.addWidget(page, 0, 0, 1, 1)

    def clearGridLayout(self):
        count = self.gridLayout_main.count()
        for i in range(count):
            self.gridLayout_main.takeAt(i).widget().deleteLater()



