from PyQt5.QtWidgets import QWidget,qApp
from PyQt5.QtCore import Qt
from ui.HeaderUI import Ui_Form
from view.components.dialog.AppInfoDialog import AppInfoDialog

from utils.common import displayOriginImage

class Header(Ui_Form,QWidget):
    def __init__(self, HomeWindow):
        super(Header, self).__init__()
        self.setupUi(self)
        self.HomeWindow = HomeWindow
        self._drag = False
        self.setNavStatus(0)
        self.initUI()
        self.initSlot()
        self.setMouseTracking(True)

    def setNavStatus(self,index):
        children = self.widget_nav.children()
        for child in children:
            if(child.inherits('QPushButton')):
                child.setProperty('class','default')
                if(child.objectName()=='pushButton_'+str(index)):
                    child.setProperty('class','active')
        self.myQSS()

    def enterEvent(self, event):
        self.setCursor(Qt.ArrowCursor)

    def mousePressEvent(self, event):
        HomeWindow = self.HomeWindow
        if(event.button()==Qt.LeftButton):
            self._drag = True
            #获取鼠标当前的坐标
            self.mouse_x = event.globalX()
            self.mouse_y = event.globalY()
            print("鼠标坐标",(self.mouse_x, self.mouse_y))

            self.origin_x = HomeWindow.x()
            self.origin_y = HomeWindow.y()
            print("窗口初始位置", (self.origin_x, self.origin_y))

    def mouseReleaseEvent(self, event):
        self._drag = False

    def mouseMoveEvent(self, event):
        HomeWindow = self.HomeWindow
        if(self._drag and not HomeWindow.isMaximized()):
            #计算鼠标移动的位移x,y
            move_x = event.globalX() - self.mouse_x
            move_y = event.globalY() - self.mouse_y

            #计算窗体更新后的的坐标：更新后的坐标 = 原本的坐标+鼠标的位移
            dest_x = self.origin_x + move_x
            dest_y = self.origin_y + move_y

            #移动窗体
            HomeWindow.move(dest_x,dest_y)

    def initUI(self):
        displayOriginImage(self.label, "static/images/logoEN.png",None,60)
        self.initIcon()
        self.myQSS()
        if self.HomeWindow.objectName()=='Form_login':
            self.widget_logo.hide()
            self.pushButton_max.hide()
            self.pushButton_min.hide()
            self.widget_nav.hide()
            self.pushButton_info.hide()

    def myQSS(self):
        qssStyle = '''
            QWidget#widget_header{
                background-color:transparent;
                color:#fff;
        
            }
            #widget_operates QPushButton{
                font-family:"Webdings";
                font-size:12px;
                width:20px;
                height:20px;
                line-height:20px;
                background-color:transparent;
                color:#fff;
                cursor:pointer;
                border-radius:3px;
            }   
            #widget_operates QPushButton:hover{
                background-color:#000;
            }     
        '''
        self.setStyleSheet(qssStyle)

    def initSlot(self):
        self.pushButton_close.clicked.connect(self.windowClose)
        self.pushButton_max.clicked.connect(self.windowMax)
        self.pushButton_min.clicked.connect(self.windowMin)
        self.pushButton_info.clicked.connect(self.appInfoDialogShow)

    def appInfoDialogShow(self):
        self.dialog = AppInfoDialog()
        self.dialog.show()

    def initIcon(self):
        self.pushButton_info.setText('i')
        self.pushButton_close.setText('r')
        self.pushButton_max.setText('1')
        self.pushButton_min.setText('0')

    def windowMax(self):
        text = self.pushButton_max.text()
        if(text == '1'):
            self.HomeWindow.showMaximized()
            self.pushButton_max.setText("2")
        else:
            self.HomeWindow.showNormal()
            self.pushButton_max.setText("1")


    def windowClose(self):
        qApp.instance().quit()

    def windowMin(self):
        self.HomeWindow.showMinimized()