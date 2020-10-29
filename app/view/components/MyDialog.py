from PyQt5.QtWidgets import QWidget,QApplication,qApp
from PyQt5.QtCore import Qt
from ui.MyDialogUI import Ui_Form

class MyDialog(Ui_Form,QWidget):
    def __init__(self):
        super(MyDialog, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.initUI()

    def initUI(self):
        desktop = qApp.desktop().screenGeometry()
        width = desktop.width()
        height = desktop.height()
        self.setWindowOpacity(0.9)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAutoFillBackground(True)
        self.label_mask.resize(width,height)
