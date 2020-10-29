# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HeaderUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_header(object):
    def setupUi(self, Form_header):
        Form_header.setObjectName("Form_header")
        Form_header.resize(1151, 66)
        Form_header.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.gridLayout = QtWidgets.QGridLayout(Form_header)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.widget_header = QtWidgets.QWidget(Form_header)
        self.widget_header.setStyleSheet("")
        self.widget_header.setObjectName("widget_header")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_header)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.widget_logo = QtWidgets.QWidget(self.widget_header)
        self.widget_logo.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_logo.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget_logo.setObjectName("widget_logo")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_logo)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.widget_logo)
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 2, 1, 1)
        self.horizontalLayout_4.addWidget(self.widget_logo)
        self.widget_left = QtWidgets.QWidget(self.widget_header)
        self.widget_left.setObjectName("widget_left")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_left)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.label_system_title = QtWidgets.QLabel(self.widget_left)
        self.label_system_title.setMaximumSize(QtCore.QSize(140, 16777215))
        self.label_system_title.setStyleSheet("font-size:20px;\n"
"font-weight:500;")
        self.label_system_title.setText("")
        self.label_system_title.setObjectName("label_system_title")
        self.horizontalLayout_3.addWidget(self.label_system_title)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.widget_nav = QtWidgets.QWidget(self.widget_left)
        self.widget_nav.setObjectName("widget_nav")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_nav)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_0 = QtWidgets.QPushButton(self.widget_nav)
        self.pushButton_0.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_0.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_0.setStyleSheet("")
        self.pushButton_0.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_0.setFlat(True)
        self.pushButton_0.setObjectName("pushButton_0")
        self.horizontalLayout.addWidget(self.pushButton_0)
        spacerItem4 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.pushButton_1 = QtWidgets.QPushButton(self.widget_nav)
        self.pushButton_1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_1.setStyleSheet("")
        self.pushButton_1.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_1.setFlat(True)
        self.pushButton_1.setObjectName("pushButton_1")
        self.horizontalLayout.addWidget(self.pushButton_1)
        spacerItem5 = QtWidgets.QSpacerItem(188, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.horizontalLayout_3.addWidget(self.widget_nav)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.widget_operates = QtWidgets.QWidget(self.widget_left)
        self.widget_operates.setObjectName("widget_operates")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_operates)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_info = QtWidgets.QPushButton(self.widget_operates)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_info.sizePolicy().hasHeightForWidth())
        self.pushButton_info.setSizePolicy(sizePolicy)
        self.pushButton_info.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_info.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_info.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_info.setStyleSheet("font-size:16px;\n"
"vertical-align:top;\n"
"line-height:30px;")
        self.pushButton_info.setText("")
        self.pushButton_info.setObjectName("pushButton_info")
        self.horizontalLayout_2.addWidget(self.pushButton_info)
        self.pushButton_min = QtWidgets.QPushButton(self.widget_operates)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_min.sizePolicy().hasHeightForWidth())
        self.pushButton_min.setSizePolicy(sizePolicy)
        self.pushButton_min.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_min.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_min.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_min.setStyleSheet("font-size:16px;\n"
"vertical-align:top;\n"
"line-height:30px;")
        self.pushButton_min.setText("")
        self.pushButton_min.setObjectName("pushButton_min")
        self.horizontalLayout_2.addWidget(self.pushButton_min)
        self.pushButton_max = QtWidgets.QPushButton(self.widget_operates)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_max.sizePolicy().hasHeightForWidth())
        self.pushButton_max.setSizePolicy(sizePolicy)
        self.pushButton_max.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_max.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_max.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_max.setStyleSheet("font-size:16px;\n"
"vertical-align:top;\n"
"line-height:30px;")
        self.pushButton_max.setObjectName("pushButton_max")
        self.horizontalLayout_2.addWidget(self.pushButton_max)
        self.pushButton_close = QtWidgets.QPushButton(self.widget_operates)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_close.sizePolicy().hasHeightForWidth())
        self.pushButton_close.setSizePolicy(sizePolicy)
        self.pushButton_close.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_close.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_close.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_close.setStyleSheet("font-size:16px;\n"
"vertical-align:top;\n"
"line-height:30px;")
        self.pushButton_close.setObjectName("pushButton_close")
        self.horizontalLayout_2.addWidget(self.pushButton_close)
        self.horizontalLayout_3.addWidget(self.widget_operates)
        self.horizontalLayout_4.addWidget(self.widget_left)
        self.gridLayout.addWidget(self.widget_header, 0, 0, 1, 1)

        self.retranslateUi(Form_header)
        QtCore.QMetaObject.connectSlotsByName(Form_header)

    def retranslateUi(self, Form_header):
        _translate = QtCore.QCoreApplication.translate
        Form_header.setWindowTitle(_translate("Form_header", "Form"))
        self.pushButton_0.setText(_translate("Form_header", "camera_preview"))
        self.pushButton_1.setText(_translate("Form_header", "face_recognize"))
        self.pushButton_info.setProperty("class", _translate("Form_header", "toolButton"))
        self.pushButton_min.setProperty("class", _translate("Form_header", "toolButton"))
        self.pushButton_max.setText(_translate("Form_header", "o"))
        self.pushButton_max.setProperty("class", _translate("Form_header", "toolButton"))
        self.pushButton_close.setText(_translate("Form_header", "x"))
        self.pushButton_close.setProperty("class", _translate("Form_header", "toolButton"))
