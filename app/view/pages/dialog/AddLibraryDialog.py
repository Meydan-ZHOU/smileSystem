from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal
from ui.AddLibraryDialogUI import Ui_Dialog


class AddLibraryDialog(Ui_Dialog, QDialog):
    submit_add_library = pyqtSignal(str)
    def __init__(self):
        super(AddLibraryDialog, self).__init__()
        self.setupUi(self)
        self.initSlot()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("添加人脸库")

    def initSlot(self):
        self.buttonBox.accepted.disconnect(self.accept)
        self.buttonBox.accepted.connect(self.handleSubmit)
        self.buttonBox.rejected.connect(self.handleCancel)

    def handleSubmit(self):
        library_name = self.lineEdit_library_name.text()
        if library_name== '':
            QMessageBox.warning(self,"提示","人脸库名不能为空！")
            return
        self.accept()
        self.submit_add_library.emit(library_name)

    def handleCancel(self):
        print("取消操作")
