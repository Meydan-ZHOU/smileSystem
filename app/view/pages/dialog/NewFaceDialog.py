from PyQt5.QtWidgets import *
from ui.NewFaceUI import Ui_Dialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, pyqtSignal
from utils.common import msg_box
from api.index import detectImage
import base64


class NewFaceDialog(Ui_Dialog, QDialog):
    submit_add_face = pyqtSignal(dict)
    def __init__(self):
        super(NewFaceDialog, self).__init__()
        self.setupUi(self)
        self.initSlot()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("添加人脸")
        jpg = QPixmap("static/images/faceIcon.png")
        self.label_image.setScaledContents(True)
        self.label_image.setPixmap(jpg)

    def initSlot(self):
        self.buttonBox.accepted.connect(self.handleSubmit)
        self.buttonBox.rejected.connect(self.handleCancel)

    def openImage(self):
        imgName, imgType ,= QFileDialog.getOpenFileName(self, "打开图片", "", 'Image Files(*.png *.jpg *.bmp)')
        jpg = QPixmap(imgName).scaled(self.label_image.width(), self.label_image.height())
        fp = open(imgName, "rb")
        data = fp.read()
        self.label_image.setPixmap(jpg)
        self.base64_image = str(base64.b64encode(data),"utf-8")
        self.handleDetectImage(self.base64_image)

    def handleSubmit(self):
        name = self.lineEdit_name.text()
        age = self.lineEdit_age.text()
        sex = self.lineEdit_sex.text()
        tel = self.lineEdit_tel.text()
        params = {
            "name": name,
            "dataImage": self.base64_image,
            "age": age,
            "sex": sex,
            "tel": tel
        }

        if(self.Error==False):
            self.submit_add_face.emit(params)

    def handleDetectImage(self,data):
        params = {
            "type":1,
            "data":data
        }
        res = detectImage(params)
        dataR = res.json()
        if(res.status_code==200 and dataR.get('code')==0):
            self.label_tip.setText("图片合格")
            self.Error = False
        else:
            self.label_tip.setText("图片不合格")
            self.Error = True

    def handleCancel(self):
        print("取消操作")
