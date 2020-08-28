from PyQt5.QtWidgets import *
from ui.DialogUI import Ui_Dialog


class AddCameraDialog(Ui_Dialog, QDialog):
    def __init__(self):
        super(AddCameraDialog, self).__init__()
        self.setupUi(self)
        self.initSlot()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("添加摄像头")

    def initSlot(self):
        self.buttonBox.accepted.connect(self.handleSubmit)
        self.buttonBox.rejected.connect(self.handleCancel)

    def handleSubmit(self):
        print("提交操作")

    def handleCancel(self):
        print("取消操作")
