import math
from PyQt5.QtWidgets import QWidget,QHBoxLayout,QPushButton,QLabel,QMessageBox,QLineEdit
from PyQt5.QtCore import pyqtSignal

from utils.common import btn_set_pointer_cursor

class Pagination(QWidget):
    current_page_change = pyqtSignal(int)
    def __init__(self,total,size,current_page):
        super(Pagination,self).__init__()
        self.total = total
        self.size = size
        self.current_page = current_page
        self.initUI(total,size,current_page)


    def initUI(self,total,size,current_page):
        self.totalPage = math.ceil(total/size)
        h = QHBoxLayout(self)
        self.totalLabel = QLabel('共 ' + str(total) + ' 条')
        homePageBtn = QPushButton("首页")
        prePageBtn = QPushButton("上一页")
        self.curPageLabel = QLabel(str(current_page))
        self.totalPageLabel = QLabel('/ ' + str(self.totalPage))
        nextPageBtn = QPushButton("下一页")
        finalPageBtn = QPushButton("尾页")
        skipLable_0 = QLabel("跳到")
        self.skipPage = QLineEdit()
        self.skipPage.setMaximumWidth(40)
        skipLabel_1 = QLabel("页")
        confirmSkip = QPushButton("确定")

        btn_set_pointer_cursor(homePageBtn)
        btn_set_pointer_cursor(prePageBtn)
        btn_set_pointer_cursor(nextPageBtn)
        btn_set_pointer_cursor(finalPageBtn)
        btn_set_pointer_cursor(confirmSkip)

        homePageBtn.clicked.connect(self._home_page)
        prePageBtn.clicked.connect(self._pre_page)
        nextPageBtn.clicked.connect(self._next_page)
        finalPageBtn.clicked.connect(self._final_page)
        confirmSkip.clicked.connect(self.__confirm_skip)

        h.addStretch(1)
        h.addWidget(self.totalLabel)
        h.addWidget(homePageBtn)
        h.addWidget(prePageBtn)
        h.addWidget(self.curPageLabel)
        h.addWidget(self.totalPageLabel)
        h.addWidget(nextPageBtn)
        h.addWidget(finalPageBtn)
        h.addWidget(skipLable_0)
        h.addWidget(self.skipPage)
        h.addWidget(skipLabel_1)
        h.addWidget(confirmSkip)


    def _home_page(self):
        self.control_signal('home')

    def _pre_page(self):
        self.control_signal('pre')

    def _next_page(self):
        self.control_signal('next')

    def _final_page(self):
        self.control_signal('final')

    def __confirm_skip(self):
        self.control_signal('skip')

    def control_signal(self,type):
        if 'home'==type:
            self.current_page = 1
        elif 'pre'==type:
            if 1==self.current_page:
                QMessageBox.information(self,'提示','已经是第一页了',QMessageBox.Yes)
                return
            self.current_page = self.current_page-1

        elif 'next'==type:
            if(self.totalPage==self.current_page):
                QMessageBox.information(self, "提示", "已经是最后一页了", QMessageBox.Yes)
                return
            self.current_page = self.current_page + 1
        elif 'final'==type:
            self.current_page = self.totalPage

        elif 'skip'==type:
            skipStr = self.skipPage.text()
            if(skipStr==''):
                return
            num = int(skipStr)
            print(num)
            if self.totalPage < num or num < 0:
                QMessageBox.information(self, "提示", "跳转页码超出范围", QMessageBox.Yes)
                return
            self.current_page = num

        self.curPageLabel.setText(str(self.current_page))
        self.current_page_change.emit(self.current_page)
