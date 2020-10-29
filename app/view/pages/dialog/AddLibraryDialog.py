from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSignal,Qt
from ui.AddLibraryDialogUI import Ui_Dialog


class AddLibraryDialog(Ui_Dialog, QDialog):
    submit_add_library = pyqtSignal(str)
    def __init__(self):
        super(AddLibraryDialog, self).__init__()
        self.setupUi(self)
        self.initSlot()
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

    def initSlot(self):
        pass

    def handleSubmit(self):
        library_name = self.lineEdit_library_name.text()
        if library_name== '':
            return
        self.accept()
        self.submit_add_library.emit(library_name)

    def handleCancel(self):
        self.reject()
