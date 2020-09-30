from PyQt5.QtWidgets import *
from ui.AppInfoDialog import Ui_Dialog
from api.index import getAppInfo

from config.config import config_write,config_read
from utils.common import msg_box

class AppInfoDialog(Ui_Dialog, QDialog):
    def __init__(self):
        super(AppInfoDialog, self).__init__()
        self.setupUi(self)
        self.initSlot()
        self.initUI()
        self.host = None
        self.getServerHost()
        self.getAppInformation()


    def initUI(self):
        self.setWindowTitle("软件信息")

    def initSlot(self):
        self.buttonBox.accepted.disconnect(self.accept)
        self.buttonBox.accepted.connect(self.handleSubmit)

    def handleSubmit(self):
        host = self.lineEdit_server_ip.text()
        if(host==''):
            msg_box(self,'服务器地址不能为空')
            return
        else:
            self.accept()
            config_write(host)

    def getServerHost(self):
        self.host = config_read()
        self.lineEdit_server_ip.setText(self.host)

    def getAppInformation(self):
        res = getAppInfo()
        if(res):
            result = res.json()
            if(res.status_code==200 and result.get('code')==0):
                data = result.get("data")
                self.lineEdit.setText(data['axstream_version'])
                self.lineEdit_2.setText(data['face_identification_version'])
                self.lineEdit_3.setText(data['person_manager_version'])
            else:
                msg_box(self,result.get('msg'))
