from PyQt5.QtWidgets import *
from ui.FaceMainUI import Ui_Form
from api.index import get_tasks_list,get_task_info_list,get_library_by_id,stopTask
import time,threading
from PyQt5.QtCore import pyqtSignal
from utils.common import msg_box
import json

class FaceMainPage(Ui_Form,QWidget):
    update_table_list_ui = pyqtSignal(dict)
    def __init__(self, HomeLayout, parent=None):
        super(FaceMainPage, self).__init__(parent)
        self.setupUi(self)
        self.HomeLayout = HomeLayout
        print("人脸主页面----------------------------------")
        self.initSlot()
        self.initData()

    def initSlot(self):
        self.update_table_list_ui.connect(self.updateTableListUI)

    def initData(self):
        self.taskIdList = []
        self.taskInfoList = []
        self.initTable()
        th = threading.Thread(target=self.getTasksList)
        th.start()
        th.join()

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
        print("len(self.taskInfoList)", len(self.taskInfoList))
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
                    "server":server
                }
        print("task_all_dic", task_all_dic)
        self.update_table_list_ui.emit(task_all_dic)

    def initTable(self):
        tableWidget = self.tableWidget
        tableWidget.clear()
        tableWidget.setColumnCount(6)
        tableWidget.setHorizontalHeaderLabels(["摄像头地址", "人脸库", "相似度", "状态","报警地址","操作"])
        font = tableWidget.horizontalHeader().font()
        font.setBold(True)
        tableWidget.horizontalHeader().setFont(font)
        tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        tableWidget.resizeRowsToContents()
        tableWidget.resizeColumnsToContents()

    def updateTableListUI(self,tasks_dict):
        print("len(tasks_dict)",len(tasks_dict))
        tableWidget = self.tableWidget
        tableWidget.clearContents()
        tableWidget.setRowCount(len(tasks_dict))
        for i,task_id in enumerate(tasks_dict):
            task = tasks_dict[task_id]
            cameras_dict = task['cameras_dict']
            cameras_list = {}
            libs_list = {}
            running_list = {}
            for index,url in enumerate(cameras_dict):
                camera = cameras_dict[url]
                running = self.getStatusText(camera['running'])
                lib_names = camera['lib_names']
                running_list[index] = running
                libs_list[index] = lib_names
                cameras_list[index] = url


            widget = self.getListWidget(cameras_list)
            tableWidget.setCellWidget(i, 0, widget)
            widget = self.getListWidget(libs_list)
            tableWidget.setCellWidget(i, 1, widget)
            widget = self.getListWidget(libs_list)
            tableWidget.setCellWidget(i, 2, widget)
            widget = self.getListWidget(running_list)
            tableWidget.setCellWidget(i, 3, widget)
            btn_del = QPushButton()
            btn_del.setText("删除")
            btn_del.setFixedSize(80,25)
            btn_del.setProperty("task_id",task_id)
            btn_del.clicked.connect(self.handleDeleteTask)
            tableWidget.setCellWidget(i,5,btn_del)

        task_all_dic = {}

        #     for cams in cameras:
        #         libs_arr = []
        #         cameras_arr = []
        #         running_arr = []
        #         lib_id_arr = cams["face_lib_ids"]
        #         for lib_id in lib_id_arr:
        #             res = get_library_by_id(lib_id)
        #             data = res.json()
        #             if(res.status_code==200):
        #                 lib_name = data.get("name")
        #                 libs_arr.append(lib_name)
        #                 for lib in libraries:
        #                     similarity_arr = []
        #                     if(lib["face_lib_id"]==lib_id):
        #                         similarity_arr.append(lib_name)
        #                         similarity_arr.append(lib["similarity_threshold"])
        #                         if(similarity_all_str.find(str(similarity_arr))==-1):
        #                             similarity_all_str = similarity_all_str + str(similarity_arr)
        #
        #         for stats in status:
        #             if(stats["camera"]==cams["url"]):
        #                 running = stats["running"]
        #                 if running ==1:
        #                     run_text="运行中"
        #                 else:
        #                     run_text = "异常"
        #                 cameras_arr.append(cams["url"])
        #                 running_arr.append(run_text)
        #
        #         libs_all_str = libs_all_str + str(libs_arr)
        #         cameras_all_str = cameras_all_str + str(cameras_arr)
        #         running_all_str = running_all_str + str(running_arr)
        #
        #     newItem = QTableWidgetItem(cameras_all_str)
        #     tableWidget.setItem(i, 0, newItem)
        #     newItem = QTableWidgetItem(str(libs_all_str))
        #     tableWidget.setItem(i, 1, newItem)
        #     newItem = QTableWidgetItem(server)
        #     tableWidget.setItem(i, 2, newItem)
        #     label = QLabel(running_all_str)
        #     tableWidget.setCellWidget(i, 3, label)
        #     newItem = QTableWidgetItem(similarity_all_str)
        #     tableWidget.setItem(i, 4, newItem)
        #

    def getListWidget(self,lists):
        listWidget = QListWidget()
        listWidget.clear()
        print("lists", lists)
        for index in lists:
            item = lists[index]
            print("index",item)
            listWidget.addItem(str(item))

        return listWidget


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