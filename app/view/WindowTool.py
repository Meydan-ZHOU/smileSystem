from PyQt5.QtCore import Qt
from ui.WindowHeader import Ui_MainWindow

class WindowTool(Ui_MainWindow):
    def __init__(self):
        super(WindowTool, self).__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        # 无边框
        self.setWindowFlags(Qt.FramelessWindowHint)  # 隐藏边框
        # 鼠标跟踪
        self.setMouseTracking(True)
        # 设置背景透明
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.initIcon()

    def initIcon(self):
        self.pushButton_3.setText('r')
        self.pushButton_2.setText('1')
        self.pushButton.setText('0')