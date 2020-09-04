from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize
from ui.FaceLibrary import Ui_Form
from view.pages.dialog.AddLibraryDialog import AddLibraryDialog
from view.pages.dialog.NewFaceDialog import NewFaceDialog
from api.index import get_librarys,add_library,add_face
from utils.common import msg_box


class FaceLibraryPage(Ui_Form,QWidget):
    def __init__(self, HomeLayout, parent=None):
        super(FaceLibraryPage, self).__init__(parent)
        self.setupUi(self)
        self.HomeLayout = HomeLayout
        self.libraryList = None
        self.currentLibrary = None
        self.getLibraryList()


    def goFacePage(self):
        print("去人脸识别页面")

    def getItemWidget(self, data):
        print(data)
        face_lib_name = data['face_lib_name']
        # 总widget
        widget = QWidget()
        # 总的横向布局
        layout_main = QHBoxLayout()
        # 摄像头名字
        camera_text = QLabel(face_lib_name)
        # 摄像头编辑按钮
        layout_main.addWidget(camera_text)
        widget.setLayout(layout_main)

        return widget

    def addFaceLibraryBoxShow(self):
        self.dialog = AddLibraryDialog()
        self.dialog.submit_add_library.connect(self.submitAddLibrary)
        self.dialog.show()

    def submitAddLibrary(self,libraryName):
        params = {
            "face_lib_name":libraryName
        }
        res = add_library(params)
        if(res.status_code == 200):
            msg_box(self,"操作成功")
            self.getLibraryList()

    def getLibraryList(self):
        res =get_librarys()
        if res.status_code == 200:
            self.libraryList = res.json()
            self.initLibraryListUI(self.libraryList)

    def initLibraryListUI(self,libraryList):
        self.listWidget.clear()
        for library in libraryList:
            item = QListWidgetItem()  # 创建QListWidgetItem对象
            item.setData(0, library)
            item.setSizeHint(QSize(100, 50))
            widget = self.getItemWidget(library)
            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item, widget)

    def newFaceBoxShow(self):
        self.newFaceDialog = NewFaceDialog()
        self.newFaceDialog.submit_add_face.connect(lambda data: self.submitAddFace(data))
        self.newFaceDialog.show()

    def submitAddFace(self,data):
        params = {
            "face_name":data['name'],
            "face_lib_id": "Lib_1599217108823386",
            "face_photo": {
                "type": 1,
                "data": data['dataImage']
            },
            "extras":{
                "age": data['age'],
                "sex": data['sex']
            }
        }
        print(params)
        res = add_face(params)
        data = res.json()
        if(res.status_code==200 and data.get('code')==0):
            msg_box(self,"操作成功")
        else:
            msg_box(self, data.get('msg'))


    def handleRefreshFace(self):
        pass

    def handleLibraryChanged(self,item):
        self.currentLibrary = item.data(0)
        print(self.currentLibrary)

