# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LiveUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1000, 729)
        Form.setStyleSheet("color:#a4a5a8;")
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_left = QtWidgets.QWidget(Form)
        self.widget_left.setMinimumSize(QtCore.QSize(200, 0))
        self.widget_left.setMaximumSize(QtCore.QSize(200, 16777215))
        self.widget_left.setStyleSheet("#widget_left{\n"
"    background-color:#191d2d;\n"
"    border:1px solid #2e3557;\n"
"}\n"
"")
        self.widget_left.setObjectName("widget_left")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_left)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_onvif = QtWidgets.QPushButton(self.widget_left)
        self.pushButton_onvif.setObjectName("pushButton_onvif")
        self.verticalLayout.addWidget(self.pushButton_onvif)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_title = QtWidgets.QLabel(self.widget_left)
        self.label_title.setObjectName("label_title")
        self.horizontalLayout.addWidget(self.label_title)
        self.pushButton_add_camera = QtWidgets.QPushButton(self.widget_left)
        self.pushButton_add_camera.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_add_camera.setMaximumSize(QtCore.QSize(20, 20))
        self.pushButton_add_camera.setToolTip("")
        self.pushButton_add_camera.setFlat(False)
        self.pushButton_add_camera.setObjectName("pushButton_add_camera")
        self.horizontalLayout.addWidget(self.pushButton_add_camera)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.listWidget = QtWidgets.QListWidget(self.widget_left)
        self.listWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.listWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.listWidget.setStyleSheet("background:transparent;\n"
"border:none;")
        self.listWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.listWidget.setFlow(QtWidgets.QListView.TopToBottom)
        self.listWidget.setViewMode(QtWidgets.QListView.ListMode)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.widget_left)
        self.widget_video_show = QtWidgets.QWidget(Form)
        self.widget_video_show.setStyleSheet("border:1px solid #2e3557;")
        self.widget_video_show.setObjectName("widget_video_show")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget_video_show)
        self.gridLayout_3.setContentsMargins(5, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_video_show = QtWidgets.QLabel(self.widget_video_show)
        self.label_video_show.setToolTip("")
        self.label_video_show.setToolTipDuration(1)
        self.label_video_show.setAlignment(QtCore.Qt.AlignCenter)
        self.label_video_show.setObjectName("label_video_show")
        self.gridLayout_3.addWidget(self.label_video_show, 0, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.widget_video_show)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.pushButton_add_camera.clicked.connect(Form.addCameraDialogShow)
        self.listWidget.itemClicked['QListWidgetItem*'].connect(Form.handleCameraChanged)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_onvif.setText(_translate("Form", "ONVIF搜索设备"))
        self.label_title.setText(_translate("Form", "摄像头列表"))
        self.pushButton_add_camera.setText(_translate("Form", "+"))
        self.listWidget.setSortingEnabled(True)
        self.label_video_show.setText(_translate("Form", "请点击左侧摄像头播放视频流"))
