from PyQt5.QtWidgets import QMessageBox,qApp
from PyQt5.QtGui import QPixmap,QCursor
from PyQt5.QtCore import Qt
import os, sys, socket
dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))

_tr = qApp.translate

class CommonHelper:
    @staticmethod
    def readQSS(style):
        with open(style,'r') as f:
            return f.read()

def btn_set_pointer_cursor(btn):
    btn.setCursor(QCursor(Qt.PointingHandCursor))


def msg_box(widget,str):
    QMessageBox.information(widget, _tr('Form','tips') ,str)

def displayOriginImage(label,imagePath,width=None,height=None):
    jpg1 = QPixmap(imagePath)
    w = 0
    h = 0
    if(not width==None):
        w = width
        rate = jpg1.width() / w
        if rate>0:
            h = jpg1.height() / rate

    if (not height == None):
        jpg1 = QPixmap(imagePath)
        h = height
        rate = jpg1.height() / h
        if rate > 0:
            w = jpg1.width() / rate


    if (not width == None and not height == None):
        w= width
        h= height

    if(h/w>1.33):
        h=w*1.33

    label.setFixedWidth(w)
    label.setFixedHeight(h)
    label.setPixmap(jpg1)
    label.setScaledContents(True)


def get_host_ip():
    try:
        s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip


SYS_STYLE_COMMON = CommonHelper.readQSS("./static/style/common.qss")
