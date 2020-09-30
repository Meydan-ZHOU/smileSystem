from PyQt5.QtWidgets import QWidget,QHBoxLayout,QVBoxLayout
from ui.ScrollWrapperUI import Ui_Form
from PyQt5.QtCore import pyqtSignal

from view.components.Card import Card


class ScrollWrapper(Ui_Form,QWidget):
    delete_data = pyqtSignal(dict)
    def __init__(self,DataList):
        super(ScrollWrapper,self).__init__()
        self.setupUi(self)
        self.DataList = DataList
        self.updating = True
        self.initUI()

    def chunk(self, l, chunk_size):
        return [l[x:x + chunk_size] for x in range(0, len(l), chunk_size)]


    def initUI(self):
        wrapper_w = self.width()
        print("wrapper_w", wrapper_w)
        if (wrapper_w > 1200):
            col = 8
        else:
            col = 6
        contents_w = wrapper_w
        # print("contents_w", contents_w)

        w = contents_w / col
        print("width", w)

        widget = QWidget()
        v = QVBoxLayout()
        lists = self.chunk(self.DataList, col)

        for i, rowData in enumerate(lists):
            h = QHBoxLayout()
            for j, data in enumerate(rowData):
                h2 = QHBoxLayout()
                card = Card(data, w)
                card.delete_card_data.connect(self.handleDelete)
                h2.addWidget(card)
                h.addLayout(h2, 2)
            h.addStretch(1)
            v.addLayout(h, 0)
            v.addStretch(2)
        widget.setLayout(v)
        self.scrollArea.setWidget(widget)



    def handleDelete(self,data):
        self.delete_data.emit(data)




