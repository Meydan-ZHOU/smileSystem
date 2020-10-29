from PyQt5.QtWidgets import QDialog,qApp
from PyQt5.QtCore import pyqtSignal,Qt
from ui.AddCameraDialogUI import Ui_Dialog


class AddCameraDialog(Ui_Dialog, QDialog):
    submit_button_click = pyqtSignal(dict)
    delete_button_click = pyqtSignal(str)
    def __init__(self,Data=None):
        super(AddCameraDialog, self).__init__()
        self.setupUi(self)
        self.setFixedSize(550,400)
        self._tr = qApp.translate
        self.Data = Data
        self.initSlot()
        self.initUI()
        self.initData()
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

    def initUI(self):
        if(self.Data == None):
            self.setWindowTitle(self._tr('Form','newCamera'))
            self.pushButton_cancel.setText(self._tr('Form','cancel'))
        else:
            self.setWindowTitle(self._tr('Form','editCamera'))
            self.pushButton_cancel.setText(self._tr('Form','delete'))

    def initData(self):
        data = self.Data
        if(data==None):
            return
        name, ip, sn, username, password, url = data
        self.lineEdit_name.setText(name)
        self.lineEdit_ip.setText(ip)
        self.lineEdit_ip.setDisabled(True)
        self.lineEdit_sn.setText(sn)
        self.lineEdit_sn.setDisabled(True)
        self.lineEdit_username.setText(username)
        self.lineEdit_password.setText(password)
        self.lineEdit_url.setText(url)

    def initSlot(self):
        self.pushButton_submit.clicked.connect(self.handleSubmit)
        self.pushButton_cancel.clicked.connect(self.handleCancel)

    def handleSubmit(self):
        camera = {
            "name":self.lineEdit_name.text(),
            "ip":self.lineEdit_ip.text(),
            "sn":self.lineEdit_sn.text(),
            "username":self.lineEdit_username.text(),
            "password":self.lineEdit_password.text(),
            "url":self.lineEdit_url.text(),
        }
        self.submit_button_click.emit(camera)
        self.accept()

    def handleCancel(self):
        if (self.Data == None):
            self.reject()
            return
        ip = self.lineEdit_ip.text()
        self.delete_button_click.emit(ip)
        self.reject()
