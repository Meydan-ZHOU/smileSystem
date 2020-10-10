from PyQt5.QtWidgets import QMessageBox,QGridLayout
from PyQt5.QtGui import QPixmap
import os,sys
dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))

class CommonHelper:
    @staticmethod
    def readQSS(style):
        with open(style,'r') as f:
            return f.read()

def msg_box(widget,str):
    QMessageBox.warning(widget, "提示",str, QMessageBox.Yes | QMessageBox.No)

def displayOriginImage(label,imagePath,width=None,height=None,isMaxedHeight = True,maxHeight=150):
    jpg1 = QPixmap(imagePath)
    h=0
    w=0
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


    if(h>maxHeight and isMaxedHeight == True):
        h=maxHeight

    if (not width == None and not height == None):
        w= width
        h= height

    label.setFixedWidth(w)
    label.setFixedHeight(h)
    label.setPixmap(jpg1)
    label.setScaledContents(True)


SYS_STYLE_LOGIN = CommonHelper.readQSS("./static/style/login.qss")
SYS_STYLE_COMMON = CommonHelper.readQSS("./static/style/common.qss")
