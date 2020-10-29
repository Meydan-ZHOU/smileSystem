from PyQt5.QtWidgets import QDialog,qApp
from PyQt5.QtCore import Qt
from ui.AppInfoDialog import Ui_Dialog
from api.index import getAppInfo

from PyQt5.QtCore import QSettings,QCoreApplication

from config.config import config_write,config_read
from utils.common import msg_box

class AppInfoDialog(Ui_Dialog, QDialog):
    def __init__(self):
        super(AppInfoDialog, self).__init__()
        self.setupUi(self)
        self.setFixedSize(550,450)
        self._tr = qApp.translate
        self.initSlot()
        self.initUI()
        self.host = None
        self.getServerHost()
        self.getAppInformation()
        self.setWindowFlags(Qt.WindowStaysOnTopHint)


    def initUI(self):
        regSettings = QSettings(QCoreApplication.organizationName(), QCoreApplication.applicationName())
        language = regSettings.value('Language', 'EN')
        if(language =='EN'):
            self.radioButton_en.setChecked(True)
        else:
            self.radioButton_cn.setChecked(True)

    def initSlot(self):
        pass

    def languageToggle(self,flag):
        regSettings = QSettings(QCoreApplication.organizationName(), QCoreApplication.applicationName())
        if(True==flag):
            regSettings.setValue('Language','CN')
        else:
            regSettings.setValue('Language', 'EN')



    def handleSubmit(self):
        host = self.lineEdit_server_ip.text()
        if(host==''):
            msg_box(self,self._tr('Form','device_empty'))
            return
        else:
            self.accept()
            config_write(host)
            msg_box(self, self._tr('Form','reboot_client'))
            qApp.closeAllWindows()

    def handleCancel(self):
        self.reject()

    def getServerHost(self):
        self.host = config_read()
        self.lineEdit_server_ip.setText(self.host)

    def getAppInformation(self):
        try:
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
        except Exception:
            pass
