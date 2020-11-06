from PyQt5.QtWidgets import QDialog,qApp,QFileDialog
from ui.NewFaceUI import Ui_Dialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSignal,Qt
from utils.common import msg_box,displayOriginImage
from api.index import detectImage
import base64


class NewFaceDialog(Ui_Dialog, QDialog):
    submit_add_face = pyqtSignal(dict)
    def __init__(self,libraryList,currentLibrary):
        super(NewFaceDialog, self).__init__()
        self.setupUi(self)
        self.setFixedSize(450,600)
        self._tr = qApp.translate
        self.libraryList = libraryList
        self.currentLibrary = currentLibrary
        self.initData()
        self.updateLibraryComboboxUI()
        self.initSlot()
        self.initUI()
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

    def initData(self):
        self.current_library = None
        self.origin_image = None
        self.base64_image = None

    def initSlot(self):
        pass

    def initUI(self):
        displayOriginImage(self.label_image, "static/images/faceIcon.png",None,300)
        self.label_image.setScaledContents(True)

    def updateLibraryComboboxUI(self):
        self.comboBox_library.clearEditText()
        comboBox = self.comboBox_library
        library = self.libraryList
        curIndex = 0
        cur_lib_name,cur_lib_id = self.currentLibrary
        for index, lib in enumerate(library):
            lib_name, lib_id = lib
            comboBox.addItem(lib_name)
            comboBox.setItemData(index, lib)
            if(cur_lib_id == lib_id):
                curIndex = index
        comboBox.setCurrentIndex(curIndex)
        self.libraryChange(curIndex)
        comboBox.currentIndexChanged.connect(self.libraryChange)

    def libraryChange(self,i):
        self.current_library = self.comboBox_library.itemData(i)

    def initSlot(self):
        pass

    def openImage(self):
        try:
            imgName, imgType ,= QFileDialog.getOpenFileName(self, self._tr('Form','choose_image'), "", 'Image Files(*.png *.jpg *.bmp)')
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
            return

    def handleSubmit(self):
        name = self.lineEdit_name.text()
        age = self.lineEdit_age.text()
        tel = self.lineEdit_tel.text()
        if(self.radioButton_female.isChecked()==True):
            sex = self._tr("Dialog", "female")
        else:
            sex = self._tr("Dialog", "male")

        if(name==''):
            msg_box(self,self._tr('Form','please_enter_name'))
            return
        if(self.base64_image==None):
            msg_box(self,self._tr('Form','please_upload_right_photo'))
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
            msg_box(self,self._tr('Form','operate_error'))

    def handleDetectImage(self,data):
        params = {
            "type":1,
            "data":data
        }
        try:
            res = detectImage(params)
            dataR = res.json()
            if(res.status_code==200 and dataR.get('code')==0):
                self.label_tip.setText(self._tr('Form','photo_right'))
                self.Error = False
            else:
                self.label_tip.setText(self._tr('Form','photo_error'))
                self.base64_image = None
                self.Error = True
        except  ConnectionError as e:
            print(e)
            msg_box(self,self._tr('Form','server_connect_error'))

    def handleCancel(self):
        self.reject()
