from PyQt5.QtWidgets import QWidget,QStackedWidget,QApplication,QDesktopWidget,qApp
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
        self.initSize(0.75)
        self.initUI()
        self.initHeader()
        self.initStackedWidget()
        self.initSlot()

    def resizeEvent(self,event):
        self.setAppSize()

    def initSize(self,rate):
        desktop = QApplication.desktop().screenGeometry()
        self.winWidth = desktop.width() * rate
        self.winHeight = desktop.height() * rate
        print("screen width is %d height is %d",
              (self.winWidth, self.winHeight))
        self.resize(self.winWidth, self.winHeight)

        fg = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        fg.moveCenter(cp)
        self.move(fg.topLeft())


    def initUI(self):
        self.setStyleSheet(SYS_STYLE_COMMON)
        self.setAppSize()

    def setAppSize(self):
        qApp.width = self.width()
        qApp.height = self.height()

    def initHeader(self):
        self.header = Header(self)
        self.horizontalLayout_top.addWidget(self.header)

    def initSlot(self):
        self.header.pushButton_0.clicked.connect(self.goLivePage)
        self.header.pushButton_1.clicked.connect(self.goFacePage)
        self.stackedWidget.currentChanged.connect(self.currentStackedIndexChanged)

    def initStackedWidget(self):
        self.stackedWidget = QStackedWidget()
        self.live = LivePage(self)
        self.face = FacePage(self)
        self.stackedWidget.addWidget(self.live)
        self.stackedWidget.addWidget(self.face)
        self.live.getDatas()
        self.goLivePage()
        self.gridLayout_main.addWidget(self.stackedWidget)

    def setStackedPageIndex(self,index):
        self.stackedWidget.setCurrentIndex(index)
        self.header.setNavStatus(index)

    def goLivePage(self):
        self.setStackedPageIndex(0)

    def goFacePage(self):
        self.setStackedPageIndex(1)

    def currentStackedIndexChanged(self,index):
        currentWidget = self.stackedWidget.currentWidget()
        objectName = currentWidget.objectName()

        if objectName == 'liveW':
            currentWidget.getDatas()
        elif objectName == 'faceW':
            self.live.video.Close()
            currentWidget.goFaceMain()

