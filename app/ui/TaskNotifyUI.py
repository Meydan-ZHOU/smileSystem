# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TaskNotifyUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1011, 791)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_tool = QtWidgets.QWidget(self.widget)
        self.widget_tool.setMinimumSize(QtCore.QSize(0, 40))
        self.widget_tool.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widget_tool.setObjectName("widget_tool")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_tool)
        self.horizontalLayout_3.setSpacing(8)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.widget_tool)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.lineEdit_name = QtWidgets.QLineEdit(self.widget_tool)
        self.lineEdit_name.setMinimumSize(QtCore.QSize(80, 0))
        self.lineEdit_name.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.horizontalLayout_3.addWidget(self.lineEdit_name)
        self.label_4 = QtWidgets.QLabel(self.widget_tool)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.widget_tool)
        self.dateTimeEdit.setCalendarPopup(True)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.horizontalLayout_3.addWidget(self.dateTimeEdit)
        self.label_2 = QtWidgets.QLabel(self.widget_tool)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.comboBox_camera = QtWidgets.QComboBox(self.widget_tool)
        self.comboBox_camera.setObjectName("comboBox_camera")
        self.horizontalLayout_3.addWidget(self.comboBox_camera)
        self.label_3 = QtWidgets.QLabel(self.widget_tool)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.comboBox_library = QtWidgets.QComboBox(self.widget_tool)
        self.comboBox_library.setObjectName("comboBox_library")
        self.horizontalLayout_3.addWidget(self.comboBox_library)
        self.pushButton_search = QtWidgets.QPushButton(self.widget_tool)
        self.pushButton_search.setMinimumSize(QtCore.QSize(80, 0))
        self.pushButton_search.setMaximumSize(QtCore.QSize(80, 16777215))
        self.pushButton_search.setProperty("sizeBtn", "")
        self.pushButton_search.setObjectName("pushButton_search")
        self.horizontalLayout_3.addWidget(self.pushButton_search)
        self.pushButton_update = QtWidgets.QPushButton(self.widget_tool)
        self.pushButton_update.setMinimumSize(QtCore.QSize(80, 0))
        self.pushButton_update.setMaximumSize(QtCore.QSize(80, 16777215))
        self.pushButton_update.setProperty("sizeBtn", "")
        self.pushButton_update.setObjectName("pushButton_update")
        self.horizontalLayout_3.addWidget(self.pushButton_update)
        spacerItem1 = QtWidgets.QSpacerItem(676, 19, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.widget_tool)
        self.widget_main = QtWidgets.QWidget(self.widget)
        self.widget_main.setObjectName("widget_main")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_main)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_notify = QtWidgets.QWidget(self.widget_main)
        self.widget_notify.setObjectName("widget_notify")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_notify)
        self.horizontalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addWidget(self.widget_notify)
        self.verticalLayout.addWidget(self.widget_main)
        self.widget_pagination = QtWidgets.QWidget(self.widget)
        self.widget_pagination.setMinimumSize(QtCore.QSize(0, 40))
        self.widget_pagination.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widget_pagination.setObjectName("widget_pagination")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_pagination)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_pagination = QtWidgets.QHBoxLayout()
        self.horizontalLayout_pagination.setObjectName("horizontalLayout_pagination")
        self.horizontalLayout_6.addLayout(self.horizontalLayout_pagination)
        self.verticalLayout.addWidget(self.widget_pagination)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "姓名"))
        self.label_4.setText(_translate("Form", "时间"))
        self.label_2.setText(_translate("Form", "摄像头"))
        self.label_3.setText(_translate("Form", "人脸库"))
        self.pushButton_search.setText(_translate("Form", "搜索"))
        self.pushButton_search.setProperty("class", _translate("Form", "default"))
        self.pushButton_update.setText(_translate("Form", "获取最新"))
        self.pushButton_update.setProperty("class", _translate("Form", "primary"))
