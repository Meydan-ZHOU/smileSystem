# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VideoUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_video(object):
    def setupUi(self, Form_video):
        Form_video.setObjectName("Form_video")
        Form_video.resize(1110, 678)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form_video)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Form_video)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setToolTip("")
        self.label.setLineWidth(0)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout.addWidget(self.widget)
        self.widget_tools = QtWidgets.QWidget(Form_video)
        self.widget_tools.setMinimumSize(QtCore.QSize(0, 40))
        self.widget_tools.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widget_tools.setStyleSheet("")
        self.widget_tools.setObjectName("widget_tools")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_tools)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_camera_name = QtWidgets.QLabel(self.widget_tools)
        self.label_camera_name.setText("")
        self.label_camera_name.setObjectName("label_camera_name")
        self.horizontalLayout_2.addWidget(self.label_camera_name)
        spacerItem1 = QtWidgets.QSpacerItem(1007, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.pushButton_close = QtWidgets.QPushButton(self.widget_tools)
        self.pushButton_close.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_close.setMaximumSize(QtCore.QSize(20, 20))
        self.pushButton_close.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_close.setStyleSheet("")
        self.pushButton_close.setObjectName("pushButton_close")
        self.horizontalLayout_2.addWidget(self.pushButton_close)
        spacerItem2 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addWidget(self.widget_tools)

        self.retranslateUi(Form_video)
        QtCore.QMetaObject.connectSlotsByName(Form_video)

    def retranslateUi(self, Form_video):
        _translate = QtCore.QCoreApplication.translate
        Form_video.setWindowTitle(_translate("Form_video", "Form"))
        self.label.setText(_translate("Form_video", "please_click_left"))
        self.pushButton_close.setText(_translate("Form_video", "X"))
