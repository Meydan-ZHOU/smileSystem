from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGridLayout
StyleSheet = """
#Form{
    display:block;
    width:500px;
    background:#191d2d;
    color:#fff;
}
QLabel{
    color:#fff;
}
"""

class MainUI(object):
    def setupUi(self,Form):
        Form.setObjectName("Form")
        self.resize(800, 400)
        Form.setStyleSheet(StyleSheet)
        grid = QtWidgets.QGridLayout(Form)
        grid.setObjectName("gridLayout")

        form = QtWidgets.QFormLayout(Form)
        self.username_label = QtWidgets.QLabel(Form)
        self.username_label.setObjectName("username_label")
        self.username_lineEdit = QtWidgets.QLineEdit(Form)
        self.username_lineEdit.setObjectName("username_lineEdit")

        form.addRow(self.username_label, self.username_lineEdit)

        grid.addLayout(form,0,0)
        grid.setContentsMargins(50,80,50,50)
        self.setLayout(grid)


        self.retranslateUi(Form)


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.username_label.setText(_translate("Form", "用户:"))

