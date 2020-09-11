from PyQt5.QtWidgets import *
from ui.HomeLayoutUI import Ui_Form_home
from utils.common import SYS_STYLE_HOME,newGridLayout
from view.pages.Live import LivePage
from view.pages.Face import FacePage

class HomeWindow(Ui_Form_home,QWidget):
    def __init__(self):
        super(HomeWindow, self).__init__()
        self.setupUi(self)
        self.initUI()
        self.goFacePage()

    def initUI(self):
        self.setStyleSheet(SYS_STYLE_HOME)

    def goLivePage(self):
        live = LivePage(self)
        self.layoutPage(live)

    def goFacePage(self):
        face = FacePage(self)
        self.layoutPage(face)

    def layoutPage(self, page):
        self.clearGridLayout()
        self.gridLayout_main.addWidget(page, 0, 0, 1, 1)

    def clearGridLayout(self):
        count = self.gridLayout_main.count()
        for i in range(count):
            self.gridLayout_main.takeAt(i).widget().deleteLater()
