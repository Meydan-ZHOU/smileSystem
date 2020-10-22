import time,threading
from PyQt5.QtWidgets import QWidget,qApp,QAbstractItemView,QTableWidgetItem,QHBoxLayout,QPushButton,QHeaderView,QVBoxLayout,QLabel
from ui.FaceMainUI import Ui_Form
from PyQt5.QtCore import pyqtSignal

from api.index import get_tasks_list,get_task_info_list,stopTask
from utils.common import msg_box,btn_set_pointer_cursor

from sql.DBHelper import DBHelper

class FaceMainPage(Ui_Form,QWidget):
    update_table_list_ui = pyqtSignal(dict)
    def __init__(self, HomeLayout, parent=None):
        super(FaceMainPage, self).__init__(parent)
        self.setupUi(self)
        self.HomeLayout = HomeLayout
        self._tr = qApp.translate
        print("人脸主页面----------------------------------")
        self.dbHelper = DBHelper()
        self.dataFlag = True
        self.isGettingData = False
        self.initSlot()
        self.initUI()

    def getDatas(self):
        print("face main get datas")
        self.dataFlag = True
        self.initTable()
        self.updateData()

    def initUI(self):
        self.setObjectName("faceMain")

    def updateData(self):
        th = threading.Thread(target=self.getTaskDatas,name="getTasks")
        th.setDaemon(True)
        th.start()

    def getDataError(self):
        self.isGettingData = False
        self.dataFlag = False

    def initSlot(self):
        self.update_table_list_ui.connect(self.updateTableListUI)

    def goFaceMain(self):
        self.HomeLayout.goFaceMain()

    def goLibraryManagementPage(self):
        self.HomeLayout.goLibraryManagementPage()

    def goFaceTaskPage(self):
        self.HomeLayout.goFaceTaskPage()

    def getTaskDatas(self):
        while self.dataFlag:
            try:
                pageIndex = self.HomeLayout.stackedWidget.currentIndex()
                homePageIndex = self.HomeLayout.HomeLayout.stackedWidget.currentIndex()

                if(not pageIndex == 0 or not homePageIndex == 1):
                    self.getDataError()
                    print("不在任务请求页面哦")
                    return
                self.taskIdList = []
                self.taskInfoList = []
                self.getTasksList()
                self.isGettingData = True
                time.sleep(5)
            except Exception as e:
                self.getDataError()
                print("请求任务列表异常停止", e)

    def getTaskInfoList(self):
        taskId = self.taskIdList
        self.taskInfoList.clear()
        for index,id in enumerate(taskId):
            try:
                res = get_task_info_list(id)
                if res:
                    result = res.json()
                    if(res.status_code==200 and result.get("code")==0):
                        data = result.get('data')
                        data["task_id"] = id
                        self.taskInfoList.append(data)
            except ConnectionError as e:
                print(e)
                msg_box(self,self._tr('Form','server_connect_error'))

        self.formatData(self.taskInfoList)

    def formatData(self,tasks):
        task_all_dic = {}
        for i, task in enumerate(tasks):
            status = task["status"]
            cameras = task["task"]["cameras"]
            libraries = task["task"]["libraries"]
            server = task["notify"]["server"]
            time = int(task["runtime"]/1000000)
            task_id = task['task_id']
            library_dict = {}
            cameras_dict = {}
            # 获取人脸库字典
            for lib in libraries:
                lib_id = lib['face_lib_id']
                similarity = lib['similarity_threshold']
                db_back = self.dbHelper.select_single_library(lib_id)
                if len(db_back)>0:
                    lib_name,lib_id = db_back[0]
                    if (library_dict.get(lib_id) == None):
                        library_dict[lib_id] = {
                            "similarity": similarity,
                            "name": lib_name
                        }
                else:
                    print("该人脸库不存在", lib_id)

            # 获取摄像头字典

            for cams in cameras:
                url = cams['url']
                lib_ids = cams['face_lib_ids']
                lib_names = []
                for lib_id in lib_ids:
                    if not library_dict.get(lib_id)==None:
                        lib_name = library_dict[lib_id]['name']
                        lib_names.append(lib_name)
                if (cameras_dict.get(url) == None):
                    cameras_dict[url] = {
                        "lib_names": lib_names,
                    }

                for stus in status:
                    camera = stus['camera']
                    running = stus['running']
                    if (camera == url):
                        cameras_dict[url]["running"] = running

            if task_all_dic.get(task_id) == None:
                task_all_dic[task_id] = {
                    "library_dict": library_dict,
                    "cameras_dict": cameras_dict,
                    "server":server,
                    "time":time,
                }
        self.update_table_list_ui.emit(task_all_dic)

    def initTable(self):
        tableWidget = self.tableWidget
        tableWidget.clear()
        tableWidget.setColumnCount(8)
        tableWidget.setHorizontalHeaderLabels([self._tr('Form','index'),self._tr('Form','camera_url'), self._tr('Form','status'),self._tr('Form','runtime'), self._tr('Form','face_library'),self._tr('Form','similarity'),self._tr('Form','monitor_address'),self._tr('Form','operate')])
        font = tableWidget.horizontalHeader().font()
        font.setBold(True)
        tableWidget.horizontalHeader().setFont(font)
        tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        tableWidget.setAlternatingRowColors(True)
        self.resizeTable(tableWidget)

    def updateTableListUI(self,tasks_dict):
        print("len(tasks_dict)",len(tasks_dict))
        tableWidget = self.tableWidget
        tableWidget.clearContents()
        tableWidget.setRowCount(len(tasks_dict))
        for i,task_id in enumerate(tasks_dict):
            task = tasks_dict[task_id]
            server = task['server']
            time = task['time']
            library_dict = task['library_dict']
            cameras_dict = task['cameras_dict']
            cameras_list = {}
            libs_list = {}
            running_list = {}
            similarity_list = {}
            for index,lib_id in enumerate(library_dict):
                lib = library_dict[lib_id]
                if(similarity_list.get(index)==None):
                    similarity_list[index] = [lib.get('name'),lib.get('similarity')]

            for index,url in enumerate(cameras_dict):
                camera = cameras_dict[url]
                running = self.getStatusText(camera['running'])
                lib_names = camera['lib_names']
                running_list[index] = running
                libs_list[index] = lib_names
                cameras_list[index] = url

            widget = QTableWidgetItem(str(i+1))
            tableWidget.setItem(i, 0, widget)
            widget = QTableWidgetItem(str(time)+'S')
            tableWidget.setItem(i, 3, widget)
            widget = self.getItemWidget(cameras_list)
            tableWidget.setCellWidget(i, 1, widget)
            widget = self.getItemWidget(libs_list)
            tableWidget.setCellWidget(i, 4, widget)
            widget = self.getItemWidget(similarity_list)
            tableWidget.setCellWidget(i, 5, widget)
            widget = self.getItemWidget(running_list)
            tableWidget.setCellWidget(i, 2, widget)
            widget = QTableWidgetItem(server)
            tableWidget.setItem(i, 6, widget)
            widget = QWidget()
            h = QHBoxLayout()
            btn_del = QPushButton()
            btn_del.setText(self._tr('Form','delete'))
            btn_del.setProperty('class','danger')
            btn_del.setProperty("task_id",task_id)
            btn_del.clicked.connect(self.handleDeleteTask)
            btn_set_pointer_cursor(btn_del)
            btn_show = QPushButton()
            btn_show.setText(self._tr('Form','look'))
            btn_show.setProperty('class', 'default')
            btn_show.setProperty("task_id", task_id)
            btn_show.clicked.connect(self.goTaskDetectPage)
            btn_set_pointer_cursor(btn_show)
            h.addWidget(btn_del)
            h.addWidget(btn_show)
            widget.setLayout(h)
            widget.setMaximumWidth(200)
            tableWidget.setCellWidget(i,7,widget)
            self.resizeTable(tableWidget)

    def resizeTable(self,tableWidget):
        # tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        tableWidget.resizeRowsToContents()
        tableWidget.resizeColumnsToContents()
        tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        tableWidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        tableWidget.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
        tableWidget.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeToContents)
        tableWidget.horizontalHeader().setSectionResizeMode(5, QHeaderView.ResizeToContents)
        tableWidget.horizontalHeader().setSectionResizeMode(6, QHeaderView.ResizeToContents)
        tableWidget.horizontalHeader().setSectionResizeMode(7, QHeaderView.ResizeToContents)

    def getItemWidget(self,lists):
        widget = QWidget()
        v = QVBoxLayout()
        v.setSpacing(10)
        for index in lists:
            label = QLabel()
            item = lists[index]
            label.setText(str(item))
            if(item == self._tr('Form','abnormal')):
                label.setProperty('class','error')
            v.addWidget(label)
        widget.setLayout(v)
        return widget

    def goTaskDetectPage(self):
        task_id = self.sender().property('task_id')
        self.HomeLayout.goFaceTaskNotify(task_id)

    def getStatusText(self,num):
        if(num==0):
            return self._tr('Form','abnormal')
        else:
            return self._tr('Form','running')

    def handleDeleteTask(self):
        task_id = self.sender().property("task_id")
        params = {
            "task_id":task_id
        }
        try:
            res = stopTask(params)
            if res:
                data = res.json()
                if(res.status_code==200 and data.get("code")==0):
                    db_back = self.dbHelper.delete_notify(task_id)
                    if(db_back):
                        self.getTasksList()
                    else:
                        msg_box(self,self._tr('Form','operate_error'))
                else:
                    msg_box(self,data.get("msg"))
        except ConnectionError as e:
            print(e)
            msg_box(self,self._tr('Form','server_connect_error'))

    def getTasksList(self):
        try:
            res = get_tasks_list()
            if res:
                data = res.json()
                self.taskIdList.clear()
                if(res.status_code==200 and data.get('code')==0):
                    self.taskIdList = data.get('data')
                    self.getTaskInfoList()
        except ConnectionError as e:
            print(e)
            msg_box(self, self._tr('Form', 'server_connect_error'))