from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize
from ui.FaceLibrary import Ui_Form
from PyQt5.QtGui import QPixmap

from view.pages.dialog.AddLibraryDialog import AddLibraryDialog
from view.pages.dialog.NewFaceDialog import NewFaceDialog
from view.components.LabelFrame import LabelFrame

from api.index import get_librarys, add_library, add_face, getAllFaces,del_faces,delete_library
from utils.common import msg_box
from utils.common import SYS_STYLE_COMMON

from sql.DBHelper import DBHelper

class FaceLibraryPage(Ui_Form,QWidget):
    def __init__(self, HomeLayout, parent=None):
        super(FaceLibraryPage, self).__init__(parent)
        self.setupUi(self)
        self.HomeLayout = HomeLayout
        self.libraryList = None
        self.currentLibrary = None
        self.dbHelper = DBHelper()
        self.createTable()
        self.getLibraryList()
        print("人脸库管理页面----------------------------------")

    def initUI(self):
        self.setStyleSheet(SYS_STYLE_COMMON)

    def createTable(self):
        self.dbHelper.create_face_table()
        self.dbHelper.create_library_table()

    def goFacePage(self):
        self.HomeLayout.stackedWidget_face.setCurrentIndex(self.HomeLayout.widget_map['page_face'])

    def getAllFacesList(self):
        if self.currentLibrary.get('face_lib_id') == None:
            return
        res = getAllFaces(self.currentLibrary.get('face_lib_id'))
        data = res.json()
        if(res.status_code==200 and type(data)==list):
            self.getFaceListUI(data)
        else:
            msg_box(self,data.get('msg'))

    def submitAddLibrary(self,libraryName):
        params = {
            "face_lib_name":libraryName
        }
        res = add_library(params)
        data = res.json()
        if(res.status_code == 200 and data.get('code')==0):
            db_data = {
                "face_lib_name":libraryName,
                'face_lib_id':data.get('data').get('face_lib_id')
            }
            db_back = self.dbHelper.insert_library(db_data)
            if(db_back):
                msg_box(self, "操作成功")
            else:
                msg_box(self, "操作失败")

            self.getLibraryList()
        else:
            msg_box(self,data.get('msg'))

    def getLibraryList(self):
        db_back = self.dbHelper.select_all_library()
        print("db_back", db_back)

        if(db_back):
            self.libraryList = db_back
            self.currentLibrary = self.libraryList[0]
            #self.getAllFacesList()
            self.initLibraryListUI(self.libraryList)
        else:
            self.libraryList = []
            self.currentLibrary = None

    def submitAddFace(self, data):
        data['face_lib_name'] = self.currentLibrary.get('face_lib_name')
        data['face_lib_id'] = self.currentLibrary.get('face_lib_id')
        params = {
            "face_name": data['name'],
            "face_lib_id": data['face_lib_id'],
            "face_photo": {
                "type": 1,
                "data": data['dataImage']
            },
            "extras":{
                "age": data['age'],
                "sex": data['sex'],
                "tel": data['tel']
            }
        }

        res = add_face(params)
        result = res.json()
        if(res.status_code==200 and result.get('code')==0):
            data['face_id'] = result.get('data').get('face_id')
            msg_box(self, "操作成功")
            self.getAllFacesList()
            self.dBHelper.insert_library_face(data)
        else:
            msg_box(self, result.get('msg'))

    def handleRefreshFace(self):
        res = getAllFaces(self.currentLibrary.get("face_lib_id"))
        data = res.json()
        print(type(data) == list)
        if (res.status_code == 200 and type(data)==list):
            msg_box(self,"操作成功")
            self.getFaceListUI(data)
        else:
            msg_box(self, data.get('msg'))

    def handleLibraryChanged(self,item):
        self.currentLibrary = item.data(0)
        self.getAllFacesList()
        print("currentLibrary", self.currentLibrary)

    def getFaceListUI(self,data):
        self.listWidget_face.clear()
        for index,face in enumerate(data):
            extra = face.get('extra')
            name = extra.get('face_name')
            age = extra.get('age')
            tel = extra.get('tel')
            item = QListWidgetItem()  # 创建QListWidgetItem对象
            item.setData(0, face)
            widget = QWidget()
            h = QHBoxLayout()
            label_image = QLabel()
            label_image.setFixedSize(200,200)
            jpg = QPixmap("static/images/faceIcon.png").scaled(label_image.width(),label_image.height())
            label_image.setPixmap(jpg)
            h.addWidget(label_image)
            #人物的简历
            form = QFormLayout()
            label_name = QLabel()
            label_age = QLabel()
            label_tel = QLabel()
            label_index = QLabel()
            label_index.setText(str(index))
            label_name.setText(name)
            label_age.setText(str(age))
            label_tel.setText(tel)
            form.addRow("索引:",label_index)
            form.addRow("姓名:",label_name)
            form.addRow("年龄:",label_age)
            form.addRow("电话:",label_tel)
            h.addLayout(form)
            btn_delete = QPushButton()
            btn_delete.setFixedSize(100, 30)
            btn_delete.setProperty("data", face)
            btn_delete.setText("删除")
            btn_delete.clicked.connect(self.submitDeleteFace)
            h.addWidget(btn_delete)
            widget.setLayout(h)
            item.setSizeHint(QSize(500,150))
            self.listWidget_face.addItem(item)
            self.listWidget_face.setItemWidget(item,widget)

    def submitDeleteFace(self):
        face = self.sender().property("data")
        print("delete face", face)
        id = face.get('face_id')
        params = {
            "face_lib_id":self.currentLibrary.get('face_lib_id'),
            "face_ids":[id]
        }
        res = del_faces(params)
        data = res.json()
        if(res.status_code==200 and data.get('code')==0):
            msg_box(self,"操作成功")
            self.getAllFacesList()
        else:
            msg_box(self,data.get("msg"))

    def addFaceLibraryBoxShow(self):
        self.dialog = AddLibraryDialog()
        self.dialog.submit_add_library.connect(self.submitAddLibrary)
        self.dialog.show()

    def newFaceBoxShow(self):
        self.newFaceDialog = NewFaceDialog()
        self.newFaceDialog.submit_add_face.connect(lambda data: self.submitAddFace(data))
        self.newFaceDialog.show()

    def initLibraryListUI(self, libraryList):
        self.listWidget.clear()
        for name,id in libraryList:
            item = QListWidgetItem()  # 创建QListWidgetItem对象
            item.setSizeHint(QSize(100, 50))
            # 总widget
            widget = QWidget()
            # 总的横向布局
            layout_main = QHBoxLayout()
            # 摄像头名字
            camera_text = QLabel(name)
            btn = QPushButton()
            btn.setText("删除")
            btn.setFixedSize(50,25)
            btn.setProperty("face_lib_id",id)
            btn.clicked.connect(self.handleDeleteLibrary)
            # 摄像头编辑按钮
            layout_main.addWidget(camera_text)
            layout_main.addWidget(btn)
            widget.setLayout(layout_main)
            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item, widget)

    def handleDeleteLibrary(self):
        id = self.sender().property("face_lib_id")
        params = {
            "face_lib_ids":[id]
        }
        res = delete_library(params)
        data = res.json()
        if(res.status_code==200 and data.get("code")==0):

            db_back = self.dbHelper.del_library(id)
            print("db_back",db_back)
            if(db_back):
                msg_box(self, "操作成功")
                self.getLibraryList()
            else:
                msg_box(self, "操作失败")
        else:
            msg_box(self,data.get("msg"))


