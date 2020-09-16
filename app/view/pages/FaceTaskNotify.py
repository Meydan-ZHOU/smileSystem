from PyQt5.QtWidgets import *
from ui.TaskNotifyUI import Ui_Form

from utils.common import SYS_STYLE_COMMON

class FaceTaskNotifyPage(Ui_Form,QWidget):
    def __init__(self, HomeLayout,task_id, parent=None):
        super(FaceTaskNotifyPage, self).__init__(parent)
        self.setupUi(self)
        self.HomeLayout = HomeLayout
        self.current_task_id = task_id
        print("self.current_task_id", task_id)
        self.initUI()

    def initUI(self):
        self.setStyleSheet(SYS_STYLE_COMMON)

