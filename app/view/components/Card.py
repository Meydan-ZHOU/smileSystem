from PyQt5.QtWidgets import QWidget,QLabel,QStackedWidget
from ui.CardUI import Ui_Form
from PyQt5.QtCore import Qt,pyqtSignal
from utils.common import displayOriginImage

class Card(Ui_Form,QWidget):
    delete_card_data = pyqtSignal(dict)
    detail_card_data = pyqtSignal(dict)
    def __init__(self,Datas,width):
        super(Card,self).__init__()
        self.setupUi(self)
        self.setMinimumWidth(width)
        self.setMaximumWidth(width)
        self.initDatas(Datas)
        self.initUI()
        self.initSlot()
        self.myQSS()

    def initDatas(self,datas):
        self.image1 = datas['image1']
        self.image2 = datas['image2']
        self.operates = datas['operates']
        self.data = datas['data']
        self.info = datas['info']

    def mouseDoubleClickEvent(self,event):
        if (event.button() == Qt.LeftButton):
            self.detail_card_data.emit(self.data)

    def initSlot(self):
        self.toolButton_delete.clicked.connect(self.handleDelete)

    def handleDelete(self):
        self.delete_card_data.emit(self.data)

    def initUI(self):
        width = self.width()
        if(self.operates==False):
            self.widget_operates.hide()

        if (self.image2 == False):
            self.label_image2.hide()
            displayOriginImage(self.label_image1, self.image1, width)
        else:
            self.widget_info.setMaximumHeight(350)
            self.label_image1.setMaximumHeight(300)
            self.label_image2.setMaximumHeight(300)
            displayOriginImage(self.label_image1, self.image1, width/2,150)
            displayOriginImage(self.label_image2, self.image2, width/2,150)

        for index,(name,value) in enumerate(self.info):
            label1 = QLabel(str(name))
            label2 = QLabel(' : '+str(value))
            label1.setAlignment(Qt.AlignTop)
            label2.setWordWrap(True)
            self.formLayout.insertRow(index,label1,label2)

    def myQSS(self):
        qssStyle = '''
                #widget_wrapper{
                    background-color:#191d2d;
                }
                QLabel{
                    font-size:14px;
                }
                #label_image1{
                    background-color:#191d2d;
                    color:#fff;
    
                }
                #toolButton_delete{
                    line-height:20px;
                    vertical-align:middle;
                }
                #toolButton_delete:hover{
                    color:red;
                    font-weight:600;
                    cursor:pointer
                }
                #widget_wrapper:hover{
                    background-color:#000;
                }
            '''
        self.setStyleSheet(qssStyle)



