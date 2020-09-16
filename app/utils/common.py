from PyQt5.QtWidgets import QMessageBox,QGridLayout

class CommonHelper:
    @staticmethod
    def readQSS(style):
        with open(style,'r') as f:
            return f.read()

def msg_box(widget,str):
    QMessageBox.warning(widget, "提示",str, QMessageBox.Yes | QMessageBox.No)

def newGridLayout(pageWrapper,page):
    grid = QGridLayout()
    count = grid.count()
    for i in range(count):
        grid.takeAt(i).widget().deleteLater()
    grid.addWidget(page,0,0,1,1)
    pageWrapper.setLayout(grid)
    print("pageWrapper CHILDREN", pageWrapper.children())



SYS_STYLE_LOGIN = CommonHelper.readQSS("./static/style/login.qss")
SYS_STYLE_HOME = CommonHelper.readQSS("./static/style/home.qss")
SYS_STYLE_COMMON = CommonHelper.readQSS("./static/style/common.qss")

CAMERA_LIST = [
            {
                "name": "摄像头1",
                "ip": "172.16.134.134",
                "url": "rtsp://admin:admin123@172.16.134.134:554"
            },
            {
                "name": "摄像头2",
                "ip": "172.16.233.100",
                "url": "rtsp://admin:admin123@172.16.233.100:554"
            },
            {
                "name": "摄像头3",
                "ip": "172.16.29.100",
                "url": "rtsp://admin:admin123@172.16.29.100:554"
            },
            {
                "name": "摄像头4",
                "ip": "172.16.15.32",
                "url": "rtsp://172.16.15.32:554/wenrui-test"
            },
        ]