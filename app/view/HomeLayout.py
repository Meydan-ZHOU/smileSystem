from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt
from ui.HomeLayoutUI import Ui_Form_home
from utils.common import SYS_STYLE_COMMON
from view.pages.Live import LivePage
from view.pages.Face import FacePage
from view.components.Header import Header

class HomeWindow(Ui_Form_home,QWidget):
    def __init__(self):
        super(HomeWindow, self).__init__()
        self.setupUi(self)
        # 无边框
        self.setWindowFlags(Qt.FramelessWindowHint)  # 隐藏边框
        # 鼠标跟踪
        self.setMouseTracking(True)
        self.initUI()
        self.goLivePage()

    def initUI(self):
        self.setWindowTitle("人脸识别系统")
        self.setStyleSheet(SYS_STYLE_COMMON)
        self.initHeader()

    def initHeader(self):
        self.header = Header(self)
        self.header.pushButton_live.clicked.connect(self.goLivePage)
        self.header.pushButton_face.clicked.connect(self.goFacePage)
        self.horizontalLayout_top.addWidget(self.header)


    def goLivePage(self):
        live = LivePage(self)
        self.header.currentActive = 'live'
        self.header.setNavStatus()
        self.layoutPage(live)

    def goFacePage(self):
        face = FacePage(self)
        self.header.currentActive = 'face'
        self.header.setNavStatus()
        self.layoutPage(face)

    def layoutPage(self, page):
        self.clearGridLayout()
        self.gridLayout_main.addWidget(page, 0, 0, 1, 1)

    def clearGridLayout(self):
        count = self.gridLayout_main.count()
        for i in range(count):
            self.gridLayout_main.takeAt(i).widget().deleteLater()
