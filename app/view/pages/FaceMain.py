from PyQt5.QtWidgets import *
from ui.FaceMainUI import Ui_Form
from api.index import get_tasks_list,get_task_info_list,get_library_by_id,stopTask
import time,threading
from PyQt5.QtCore import pyqtSignal,QThread
from utils.common import msg_box
from utils.common import SYS_STYLE_COMMON

class FaceMainPage(Ui_Form,QWidget):
    update_table_list_ui = pyqtSignal(dict)
    def __init__(self, HomeLayout, parent=None):
        super(FaceMainPage, self).__init__(parent)
        self.setupUi(self)
        self.HomeLayout = HomeLayout
        print("人脸主页面----------------------------------")
        self.stopEvent = threading.Event()
        self.stopEvent.clear()
        self.dataFlag = True
        self.initSlot()
        self.initTable()
        self.updateData()

    def initUI(self):
        self.setStyleSheet(SYS_STYLE_COMMON)

    def handleDestroy(self):
        print("我被销毁了")

    def updateData(self):
        th = threading.Thread(target=self.initData)
        th.start()

    def initSlot(self):
        self.update_table_list_ui.connect(self.updateTableListUI)

    def initData(self):
        while self.dataFlag:
            try:
                self.taskIdList = []
                self.taskInfoList = []
                self.getTasksList()
                QApplication.processEvents()
                time.sleep(5)
            except Exception:
                self.dataFlag = False
                print("发生异常",threading.get_ident())

    def getTaskInfoList(self):
        taskId = self.taskIdList
        self.taskInfoList.clear()
        for index,id in enumerate(taskId):
            res = get_task_info_list(id)
            data = res.json()
            if(res.status_code==200 and data.get("code")==0):
                new_data = data.get('data')
                new_data["task_id"] = id
                self.taskInfoList.append(new_data)
        self.formatData(self.taskInfoList)

    def formatData(self,tasks):
        task_all_dic = {}
        for i, task in enumerate(tasks):
            status = task["status"]
            cameras = task["task"]["cameras"]
            libraries = task["task"]["libraries"]
            server = task["notify"]["server"]
            task_id = task['task_id']
            library_dict = {}
            cameras_dict = {}
            # 获取人脸库字典
            for lib in libraries:
                lib_id = lib['face_lib_id']
                similarity = lib['similarity_threshold']
                res = get_library_by_id(lib_id)
                data = res.json()
                if (res.status_code == 200):
                    lib_name = data["name"]
                    if (library_dict.get(lib_id) == None):
                        library_dict[lib_id] = {
                            "similarity": similarity,
                            "name": lib_name
                        }

            # 获取摄像头字典

            for cams in cameras:
                url = cams['url']
                lib_ids = cams['face_lib_ids']
                lib_names = []
                for lib_id in lib_ids:
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
                }
        self.update_table_list_ui.emit(task_all_dic)

    def initTable(self):
        tableWidget = self.tableWidget
        tableWidget.clear()
        tableWidget.setColumnCount(7)
        tableWidget.setHorizontalHeaderLabels(["序号","摄像头地址", "状态", "人脸库", "相似度","报警地址","操作"])
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
        print("tasks_dict", tasks_dict)
        for i,task_id in enumerate(tasks_dict):
            task = tasks_dict[task_id]
            server = task['server']
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
            widget = self.getItemWidget(cameras_list)
            tableWidget.setCellWidget(i, 1, widget)
            widget = self.getItemWidget(libs_list)
            tableWidget.setCellWidget(i, 3, widget)
            widget = self.getItemWidget(similarity_list)
            tableWidget.setCellWidget(i, 4, widget)
            widget = self.getItemWidget(running_list)
            tableWidget.setCellWidget(i, 2, widget)
            widget = QTableWidgetItem(server)
            tableWidget.setItem(i, 5, widget)
            widget = QWidget()
            h = QHBoxLayout()
            btn_del = QPushButton()
            btn_del.setText("删除")
            btn_del.setFixedSize(50,25)
            btn_del.setProperty("task_id",task_id)
            btn_del.clicked.connect(self.handleDeleteTask)
            btn_show = QPushButton()
            btn_show.setText("查看")
            btn_show.setFixedSize(50, 25)
            btn_show.setProperty("task_id", task_id)
            btn_show.clicked.connect(self.goTaskDetectPage)
            h.addWidget(btn_del)
            h.addWidget(btn_show)
            widget.setLayout(h)
            tableWidget.setCellWidget(i,6,widget)
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


    def getItemWidget(self,lists):
        widget = QWidget()
        v = QVBoxLayout()
        v.setSpacing(10)
        for index in lists:
            label = QLabel()
            item = lists[index]
            label.setText(str(item))
            v.addWidget(label)
        widget.setLayout(v)
        return widget

    def goTaskDetectPage(self):
        task_id = self.sender().property('task_id')
        self.HomeLayout.goFaceTaskNotify(task_id)

    def getStatusText(self,num):
        if(num==0):
            return "异常"
        else:
            return "运行中"

    def handleDeleteTask(self):
        task_id = self.sender().property("task_id")
        params = {
            "task_id":task_id
        }
        res = stopTask(params)
        data = res.json()
        if(res.status_code==200 and data.get("code")==0):
            msg_box(self,"操作成功")
            self.getTasksList()
        else:
            msg_box(self,data.get("msg"))

    def getTasksList(self):
        res = get_tasks_list()
        data = res.json()
        self.taskIdList.clear()
        if(res.status_code==200 and data.get('code')==0):
            self.taskIdList = data.get('data')
            self.getTaskInfoList()