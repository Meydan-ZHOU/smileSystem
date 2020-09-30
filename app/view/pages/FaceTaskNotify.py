import time, threading,json
from PyQt5.QtWidgets import QWidget,QApplication,qApp
from ui.TaskNotifyUI import Ui_Form
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QPixmap

from view.components.ScrollWrapper import ScrollWrapper

from sql.DBHelper import DBHelper

class FaceTaskNotifyPage(Ui_Form,QWidget):
    update_notify_list_ui = pyqtSignal(list)
    def __init__(self, HomeLayout,task_id, parent=None):
        super(FaceTaskNotifyPage, self).__init__(parent)
        self.setupUi(self)
        self.HomeLayout = HomeLayout
        print("任务通知页面----------------------------------")
        self.dataFlag = True
        self.current_task_id = task_id
        self.dbHelper = DBHelper()
        self.initUI()
        self.initSlot()
        self.name = ''
        self.queryData()

    def resizeEvent(self,event):
        print("isresize")
        #self.queryData()

    def initSlot(self):
        self.update_notify_list_ui.connect(self.updateNotifyListUI)
        self.pushButton_update.clicked.connect(self.getAllNewest)
        self.pushButton_search.clicked.connect(self.queryData)

    def initUI(self):
        pass
        #self.setStyleSheet(SYS_STYLE_COMMON)

    def isLoading(self, flag):
        pass
        # if (flag == True):
        #     self.widget_notify.close()
        #     path = "static/images/loading.gif"
        #     jpg = QPixmap(path)
        #     self.label_loading.setPixmap(jpg)
        #     self.label_loading.setScaledContents(True)
        #     self.label_loading.show()
        # else:
        #     self.widget_notify.show()
        #     self.label_loading.close()

    def queryData(self):
        self.name = self.lineEdit_name.text()
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
        self.isLoading(True)
        self.notifyList = []
        params = {
            'name':self.name
        }
        db_back = self.dbHelper.select_task_all_notify(self.current_task_id,params)
        print("notify db_back", db_back)
        if(db_back):
            self.notifyList = db_back
        else:
            self.notifyList = []

        self.update_notify_list_ui.emit(self.notifyList)

    def clearHorizontalLayout(self):
        count = self.horizontalLayout.count()
        for i in range(count):
            self.horizontalLayout.takeAt(i).widget().deleteLater()

    def updateNotifyListUI(self,list):
        dataList = []
        self.clearHorizontalLayout()
        for index,notify in enumerate(list):
            time,task_id,camera_url,face_id,face_lib_id,similarity,extras,face_image,register_image,face_lib_name,camera_name,face_name = notify
            time_str = self.timestamp_to_str(int(time))
            information = json.loads(extras.replace("'","\""))
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
                },
                "info": [
                    ('相似度：', str(round(float(similarity)*100,0))+'%'),
                    ('姓名：', name),
                    ('人脸库：', face_lib_name),
                    ('摄像头：', camera_name),
                    ('时间：', time_str),
                ]
            }
            dataList.append(options)
        scrollArea = ScrollWrapper(dataList)
        print("widget_notify", self.size())
        self.horizontalLayout.addWidget(scrollArea)
        self.isLoading(False)