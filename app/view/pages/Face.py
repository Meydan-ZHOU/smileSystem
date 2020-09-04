from PyQt5.QtWidgets import QWidget
from ui.FaceUI import Ui_Form
from httpserver.httpclient import HttpClient


class FacePage(Ui_Form,QWidget):
    def __init__(self, HomeLayout, parent=None):
        super(FacePage, self).__init__(parent)
        self.setupUi(self)
        self.HomeLayout = HomeLayout
        self.http = HttpClient()
        #self.getTasksList()

    def goFaceLibrayManagementPage(self):
        self.HomeLayout.stackedWidget_face.setCurrentIndex(self.HomeLayout.widget_map['page_face_library'])

    def goFaceTaskPage(self):
        self.HomeLayout.stackedWidget_face.setCurrentIndex(self.HomeLayout.widget_map['page_face_task_management'])

    def getTasksList(self):
        self.http.do_get("/task/stream/query/all")


