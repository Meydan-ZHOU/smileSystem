import time, threading,json
from PyQt5.QtWidgets import QWidget,QApplication,qApp
from ui.TaskNotifyUI import Ui_Form
from PyQt5.QtCore import pyqtSignal,QDate

from view.components.ScrollWrapper import ScrollWrapper
from view.components.Pagination import Pagination

from sql.DBHelper import DBHelper

class FaceTaskNotifyPage(Ui_Form,QWidget):
    update_notify_list_ui = pyqtSignal(list)
    def __init__(self, HomeLayout, parent=None):
        super(FaceTaskNotifyPage, self).__init__(parent)
        self.setupUi(self)
        self.HomeLayout = HomeLayout
        print("任务通知页面----------------------------------")
        self.dataFlag = True
        self.current_task_id = ''
        self.isLoading = False
        self.dbHelper = DBHelper()
        self.initSlot()
        self.initData()
        self.initUI()

    def getDatas(self):
        self.initData()
        self.getLibraryList()
        self.getCameraList()
        self.getAllNewest()

    def resizeEvent(self, event):
        width = self.size().width()
        if(width>1200):
            self.pageSize = 16
        else:
            self.pageSize = 10

        self.queryData()

    def initData(self):
        self.name = ''
        self.currentTime = 0
        self.totalCount = 0
        self.pageSize = 10
        self.currentPage = 1
        self.cameraList = []
        self.currentCamera = '全部'
        self.camera_name = ''
        self.libraryList = []
        self.library_name = ''
        self.currentLibrary = '全部'

    def initUI(self):
        self.setObjectName('faceNotify')
        self.dateTimeEdit.setDate(QDate.currentDate())
        self.dateTimeEdit.setMinimumDate(QDate.currentDate().addDays(-365))
        self.dateTimeEdit.setMaximumDate(QDate.currentDate().addDays(365))
        self.dateTimeEdit.setCalendarPopup(True)

    def initSlot(self):
        self.dateTimeEdit.dateTimeChanged.connect(self.onDateTimeChanged)
        self.update_notify_list_ui.connect(self.updateNotifyListUI)
        self.pushButton_update.clicked.connect(self.getAllNewest)
        self.pushButton_search.clicked.connect(self.queryData)

    def onDateTimeChanged(self,dataTime):
        self.currentTime = dataTime.toSecsSinceEpoch()

    def getCameraList(self):
        db_back = self.dbHelper.select_all_camera()
        if (db_back):
            self.cameraList = db_back
        else:
            self.cameraList = []
        self.updateCameraComboboxUI()

    def updateCameraComboboxUI(self):
        self.comboBox_camera.clearEditText()
        comboBox = self.comboBox_camera
        cameras = self.cameraList
        comboBox.addItem('全部')
        comboBox.setItemData(0, '全部')
        for index, camera in enumerate(cameras):
            name, ip,sn,username,password,url = camera
            comboBox.addItem(name)
            comboBox.setItemData(index+1, name)
        comboBox.setCurrentIndex(0)
        self.cameraChange(0)
        comboBox.currentIndexChanged.connect(self.cameraChange)

    def cameraChange(self, i):
        self.currentCamera = self.comboBox_camera.itemData(i)

    def getLibraryList(self):
        db_back = self.dbHelper.select_all_library()
        if (db_back):
            self.libraryList = db_back
        else:
            self.libraryList = []
        self.updateLibraryComboboxUI()

    def updateLibraryComboboxUI(self):
        self.comboBox_library.clearEditText()
        comboBox = self.comboBox_library
        library = self.libraryList
        comboBox.addItem('全部')
        comboBox.setItemData(0,'全部')
        for index, lib in enumerate(library):
            lib_name, lib_id = lib
            comboBox.addItem(lib_name)
            comboBox.setItemData(index+1, lib_name)
        comboBox.setCurrentIndex(0)
        self.libraryChange(0)
        comboBox.currentIndexChanged.connect(self.libraryChange)

    def libraryChange(self, i):
        self.currentLibrary = self.comboBox_library.itemData(i)

    def getNotifyTotalCount(self,params):
        self.totalCount = self.dbHelper.query_notify_table_count(params)

    def updatePaginationUI(self):
        count = self.horizontalLayout_pagination.count()
        for i in range(count):
            self.horizontalLayout_pagination.takeAt(i).widget().deleteLater()

        pagination = Pagination(self.totalCount,self.pageSize,self.currentPage)
        pagination.current_page_change.connect(self.handleCurrentPageChange)
        self.horizontalLayout_pagination.addWidget(pagination)

    def handleCurrentPageChange(self,page):
        self.currentPage = page
        self.getNotifyList()

    def queryData(self):
        self.name = self.lineEdit_name.text()
        if (self.currentCamera == '全部'):
            self.camera_name = ''
        else:
            self.camera_name = self.currentCamera

        if (self.currentLibrary == '全部'):
            self.library_name = ''
        else:
            self.library_name = self.currentLibrary
        self.getNotifyList()

    def timestamp_to_str(self,timestamp=None, format='%Y-%m-%d %H:%M:%S'):
        if timestamp:
            time_tuple = time.localtime(timestamp)  # 把时间戳转换成时间元祖
            result = time.strftime(format, time_tuple)  # 把时间元祖转换成格式化好的时间
            return result
        else:
            return time.strptime(format)

    def getAllNewest(self):
        self.lineEdit_name.setText('')
        self.queryData()

    def getNotifyList(self):
        if(self.current_task_id == '' or True==self.isLoading):
            return
        self.notifyList = []
        self.isLoading = True
        params = {
            'name':self.name,
            'camera':self.camera_name,
            'library':self.library_name,
            'size':self.pageSize,
            'time':self.currentTime,
            'start':(self.currentPage-1)*self.pageSize
        }
        self.getNotifyTotalCount(params)
        print(params)
        db_back = self.dbHelper.select_task_all_notify(self.current_task_id,params)
        if(db_back):
            self.notifyList = db_back
        else:
            self.notifyList = []

        self.updatePaginationUI()
        self.update_notify_list_ui.emit(self.notifyList)

    def clearHorizontalLayout(self):
        count = self.horizontalLayout.count()
        for i in range(count):
            self.horizontalLayout.takeAt(i).widget().deleteLater()

    def updateNotifyListUI(self,list):
        dataList = []
        self.clearHorizontalLayout()
        for index,notify in enumerate(list):
            time,task_id,camera_url,face_id,face_lib_id,similarity,extras,face_image,register_image,face_lib_name,camera_name,face_name,capture_image = notify
            time_str = self.timestamp_to_str(int(time))
            information = json.loads(extras.replace("'","\""))
            similarity_str = str(round(float(similarity)*100,0))+'%'
            age = information['age']
            name = information['face_name']
            sex = information['sex']
            tel = information['tel']
            # 人物的简历
            options = {
                "image1":face_image ,
                "image2": register_image,
                "operates": False,
                "data": {
                    "face_id": face_id,
                    "lib_id": face_lib_id,
                    'notify':(time_str,similarity_str,face_image,register_image,camera_name,face_lib_name,capture_image,face_name,camera_url)
                },
                "info": [
                    ('相似度：', similarity_str),
                    ('姓名：', name),
                    ('人脸库：', face_lib_name),
                    ('摄像头：', camera_name),
                    ('时间：', time_str),
                ]
            }
            dataList.append(options)
        scrollArea = ScrollWrapper(dataList,5)
        scrollArea.detail_data.connect(self.handleNotifyDetail)
        self.isLoading = False
        self.horizontalLayout.addWidget(scrollArea)


    def handleNotifyDetail(self,data):
        self.HomeLayout.goFaceNotifyDetailPage(data)