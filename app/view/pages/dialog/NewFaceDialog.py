from PyQt5.QtWidgets import *
from ui.NewFaceUI import Ui_Dialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSignal
from utils.common import msg_box,displayOriginImage
from api.index import detectImage
import base64


class NewFaceDialog(Ui_Dialog, QDialog):
    submit_add_face = pyqtSignal(dict)
    def __init__(self,libraryList):
        super(NewFaceDialog, self).__init__()
        self.setupUi(self)
        self.libraryList = libraryList
        self.initData()
        self.updateLibraryComboboxUI()
        self.initSlot()
        self.initUI()

    def initData(self):
        self.current_library = None
        self.origin_image = None
        self.base64_image = None

    def initSlot(self):
        pass

    def initUI(self):
        self.setWindowTitle("添加人脸")
        displayOriginImage(self.label_image, "static/images/faceIcon.png",None,300)
        self.label_image.setScaledContents(True)

    def updateLibraryComboboxUI(self):
        self.comboBox_library.clearEditText()
        comboBox = self.comboBox_library
        library = self.libraryList
        for index, lib in enumerate(library):
            lib_name, lib_id = lib
            comboBox.addItem(lib_name)
            comboBox.setItemData(index, lib)
        comboBox.setCurrentIndex(0)
        self.libraryChange(0)
        comboBox.currentIndexChanged.connect(self.libraryChange)

    def libraryChange(self,i):
        self.current_library = self.comboBox_library.itemData(i)

    def initSlot(self):
        self.buttonBox.accepted.disconnect(self.accept)
        self.buttonBox.accepted.connect(self.handleSubmit)
        self.buttonBox.rejected.connect(self.handleCancel)

    def openImage(self):
        try:
            imgName, imgType ,= QFileDialog.getOpenFileName(self, "打开图片", "", 'Image Files(*.png *.jpg *.bmp)')
            jpg = QPixmap(imgName)
            print("imgName",imgName)
            if(imgName==''):
                return
            fp = open(imgName, "rb")
            data = fp.read()
            displayOriginImage(self.label_image,jpg,None,300)
            self.origin_image = data
            self.base64_image = str(base64.b64encode(data),"utf-8")
            self.handleDetectImage(self.base64_image)
        except (ConnectionError):
            print("上传图片中断错误")
            return

    def handleSubmit(self):
        name = self.lineEdit_name.text()
        age = self.lineEdit_age.text()
        tel = self.lineEdit_tel.text()
        if(self.radioButton_female.isChecked()==True):
            sex = "女"
        else:
            sex = "男"

        if(name==''):
            msg_box(self,"姓名不能为空")
            return
        if(self.base64_image==None):
            msg_box(self,"请上传合格的头像")
            return

        params = {
            "library":self.current_library,
            "name": name,
            "age": age,
            "sex": sex,
            "tel": tel,
            "origin_image": self.origin_image,
            "dataImage": self.base64_image,
        }

        if(self.Error==False):
            self.accept()
            self.submit_add_face.emit(params)
        else:
            msg_box(self,"操作有误！")

    def handleDetectImage(self,data):
        params = {
            "type":1,
            "data":data
        }
        try:
            res = detectImage(params)
            dataR = res.json()
            if(res.status_code==200 and dataR.get('code')==0):
                self.label_tip.setText("图片合格")
                self.Error = False
            else:
                self.label_tip.setText("图片不合格")
                self.base64_image = None
                self.Error = True
        except  ConnectionError as e:
            print(e)
            msg_box(self,"服务器连接异常")

    def handleCancel(self):
        print("取消操作")
