from PyQt5.QtWidgets import QMessageBox

class CommonHelper:
    @staticmethod
    def readQSS(style):
        with open(style,'r') as f:
            return f.read()

def msg_box(widget,str):
    QMessageBox.warning(widget, "提示",str, QMessageBox.Yes | QMessageBox.No)


SYS_STYLE_LOGIN = CommonHelper.readQSS("./static/style/login.qss")
SYS_STYLE_HOME = CommonHelper.readQSS("./static/style/home.qss")