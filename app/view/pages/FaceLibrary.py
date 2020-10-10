from PyQt5.QtWidgets import QWidget,QListWidgetItem,QHBoxLayout,QLabel,QPushButton
from PyQt5.QtCore import QSize
from ui.FaceLibrary import Ui_Form

from view.pages.dialog.AddLibraryDialog import AddLibraryDialog
from view.pages.dialog.NewFaceDialog import NewFaceDialog

from api.index import add_library,add_face, del_faces, delete_library
from utils.common import msg_box

from view.components.ScrollWrapper import ScrollWrapper
from view.components.Pagination import Pagination

from sql.DBHelper import DBHelper

class FaceLibraryPage(Ui_Form,QWidget):
    def __init__(self, HomeLayout, parent=None):
        super(FaceLibraryPage, self).__init__(parent)
        self.setupUi(self)
        self.HomeLayout = HomeLayout
        print("人脸库管理页面----------------------------------")
        self.libraryList = None
        self.faceList = None
        self.currentLibrary = None
        self.initUI()
        self.dbHelper = DBHelper()
        self.totalCount = 0
        self.pageSize = 12
        self.currentPage = 1
        self.createTable()
        self.getLibraryList()

    def resizeEvent(self, event):
        width = self.size().width()
        print("width", width)
        if (width > 1200):
            self.pageSize = 16
        else:
            self.pageSize = 12

        self.getAllFacesList()

    def initUI(self):
        self.pushButton.setProperty('class', 'addButton')

    def getFaceTotalCount(self):
        self.totalCount = self.dbHelper.query_face_table_count()

    def updatePaginationUI(self):
        count = self.horizontalLayout_pagination.count()
        for i in range(count):
            self.horizontalLayout_pagination.takeAt(i).widget().deleteLater()

        pagination = Pagination(self.totalCount, self.pageSize, self.currentPage)
        pagination.current_page_change.connect(self.handleCurrentPageChange)
        self.horizontalLayout_pagination.addWidget(pagination)

    def handleCurrentPageChange(self,page):
        self.currentPage = page
        self.getAllFacesList()

    def createTable(self):
        self.dbHelper.create_face_table()
        self.dbHelper.create_library_table()

    def goFacePage(self):
        self.HomeLayout.stackedWidget_face.setCurrentIndex(self.HomeLayout.widget_map['page_face'])

    def getAllFacesList(self):
        self.getFaceTotalCount()
        print("self.currentLibrary", self.currentLibrary)
        if self.currentLibrary == None:
            self.faceList = []
        else:
            lib_name, lib_id = self.currentLibrary
            params = {
                'id':lib_id,
                'size': self.pageSize,
                'start': (self.currentPage - 1) * self.pageSize
            }
            self.faceList = self.dbHelper.select_all_face(params)
            print(self.faceList)

        self.updatePaginationUI()
        self.updateFaceListUI(self.faceList)

    def submitAddLibrary(self,libraryName):
        params = {
            "face_lib_name":libraryName
        }
        res = add_library(params)
        if res:
            result = res.json()
            if(res.status_code == 200 and result.get('code')==0):
                db_data = {
                    "face_lib_name":libraryName,
                    'face_lib_id':result.get('data').get('face_lib_id')
                }
                db_back = self.dbHelper.insert_library(db_data)
                if(db_back):
                    msg_box(self, "操作成功")
                else:
                    msg_box(self, "操作失败")

                self.getLibraryList()
            else:
                msg_box(self,result.get('msg'))

    def submitAddFace(self, data):
        lib_name, lib_id = data['library']
        params = {
            "face_name": data['name'],
            "face_lib_id": lib_id,
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
        if res:
            result = res.json()
            if(res.status_code==200 and result.get('code')==0):
                data['face_id'] = result.get('data').get('face_id')
                msg_box(self, "操作成功")
                db_back = self.dbHelper.insert_library_face(data)
                if(db_back):
                    self.getAllFacesList()
            else:
                msg_box(self, result.get('msg'))

    def handleRefreshFace(self):
        self.getAllFacesList()

    def handleLibraryChanged(self,item):
        self.currentLibrary = item.data(0)
        self.getAllFacesList()

    def updateFaceListUI(self,list):
        self.clearHorizontalLayout()
        dataList = []
        for index,face in enumerate(list):
            lib_name,lib_id,face_id,name,image_path,age,sex,tel = face
            #人物的简历
            options = {
                "image1":image_path,
                "image2":False,
                "operates":True,
                "data":{
                    "face_id":face_id,
                    "lib_id":lib_id,
                    "lib_name":lib_name,
                    "name":name,
                },
                "info":[
                    ('姓名：',name),
                    ('电话：',tel),
                ]
            }
            dataList.append(options)
        print("self.horizontalLayout.count()",self.horizontalLayout.count())
        scrollArea = ScrollWrapper(dataList)
        scrollArea.delete_data.connect(self.submitDeleteFace)
        self.horizontalLayout.addWidget(scrollArea)

    def clearHorizontalLayout(self):
        count = self.horizontalLayout.count()
        for i in range(count):
            self.horizontalLayout.takeAt(i).widget().deleteLater()

    def submitDeleteFace(self,data):
        lib_id = data['lib_id']
        face_id = data['face_id']
        name = data['name']
        lib_name = data['lib_name']
        params = {
            "face_lib_id":lib_id,
            "face_ids":[face_id]
        }
        res = del_faces(params)
        if res:
            result= res.json()
            if(res.status_code==200 and result.get('code')==0):
                db_back = self.dbHelper.delete_face(face_id,name,lib_name)
                if(db_back):
                    msg_box(self,"操作成功")
                    self.getAllFacesList()
                else:
                    msg_box(self,"操作失败")
            else:
                msg_box(self,result.get("msg"))

    def addFaceLibraryBoxShow(self):
        self.dialog = AddLibraryDialog()
        self.dialog.submit_add_library.connect(self.submitAddLibrary)
        self.dialog.show()

    def newFaceBoxShow(self):
        if(len(self.libraryList)==0):
            msg_box(self,"请先创建人脸库")
            return
        self.newFaceDialog = NewFaceDialog(self.libraryList)
        self.newFaceDialog.submit_add_face.connect(lambda data: self.submitAddFace(data))
        self.newFaceDialog.show()

    def updateLibraryListUI(self, libraryList):
        self.listWidget.clear()
        for name,id in libraryList:
            item = QListWidgetItem()  # 创建QListWidgetItem对象
            item.setData(0,(name,id))
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
            btn.setProperty("data",(id,name))
            btn.clicked.connect(self.handleDeleteLibrary)
            # 摄像头编辑按钮
            layout_main.addWidget(camera_text)
            layout_main.addWidget(btn)
            widget.setLayout(layout_main)
            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item, widget)

    def handleDeleteLibrary(self):
        library = self.sender().property("data")
        id,name = library
        params = {
            "face_lib_ids":[id]
        }
        res = delete_library(params)
        if res:
            result = res.json()
            if(res.status_code==200 and result.get("code")==0):
                db_back = self.dbHelper.delete_library(id,name)
                if(db_back):
                    msg_box(self, "操作成功")
                    self.getLibraryList()
                else:
                    msg_box(self, "操作失败")
            else:
                msg_box(self,result.get("msg"))

    def getLibraryList(self):
        db_back = self.dbHelper.select_all_library()
        if(db_back):
            self.libraryList = db_back
            if len(self.libraryList) > 0:
                self.currentLibrary = self.libraryList[0]
            else:
                self.currentLibrary = None
        else:
            self.libraryList = []
            self.currentLibrary = None

        self.getAllFacesList()
        self.updateLibraryListUI(self.libraryList)