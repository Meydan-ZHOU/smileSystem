# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FaceTaskUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_new_task(object):
    def setupUi(self, Form_new_task):
        Form_new_task.setObjectName("Form_new_task")
        Form_new_task.resize(1099, 683)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(Form_new_task)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget_2 = QtWidgets.QWidget(Form_new_task)
        self.widget_2.setStyleSheet("")
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget_8 = QtWidgets.QWidget(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy)
        self.widget_8.setMinimumSize(QtCore.QSize(0, 50))
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_8)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_7 = QtWidgets.QLabel(self.widget_8)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.comboBox_face_libray = QtWidgets.QComboBox(self.widget_8)
        self.comboBox_face_libray.setMinimumSize(QtCore.QSize(100, 0))
        self.comboBox_face_libray.setObjectName("comboBox_face_libray")
        self.horizontalLayout_3.addWidget(self.comboBox_face_libray)
        spacerItem = QtWidgets.QSpacerItem(778, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout_4.addWidget(self.widget_8)
        self.widget = QtWidgets.QWidget(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_3 = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setMinimumSize(QtCore.QSize(250, 0))
        self.widget_3.setMaximumSize(QtCore.QSize(275, 16777215))
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget_3)
        self.label_2.setMinimumSize(QtCore.QSize(0, 30))
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.listWidget_camera = QtWidgets.QListWidget(self.widget_3)
        self.listWidget_camera.setMinimumSize(QtCore.QSize(0, 0))
        self.listWidget_camera.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.listWidget_camera.setObjectName("listWidget_camera")
        self.verticalLayout.addWidget(self.listWidget_camera)
        self.gridLayout_4.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget_4.setObjectName("widget_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget_4)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(0, 30))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.widget_task_video = QtWidgets.QWidget(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_task_video.sizePolicy().hasHeightForWidth())
        self.widget_task_video.setSizePolicy(sizePolicy)
        self.widget_task_video.setMinimumSize(QtCore.QSize(587, 0))
        self.widget_task_video.setObjectName("widget_task_video")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_task_video)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_video = QtWidgets.QHBoxLayout()
        self.horizontalLayout_video.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_video.setSpacing(0)
        self.horizontalLayout_video.setObjectName("horizontalLayout_video")
        self.horizontalLayout.addLayout(self.horizontalLayout_video)
        self.verticalLayout_2.addWidget(self.widget_task_video)
        self.gridLayout_5.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.widget_4)
        self.widget_5 = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        self.widget_5.setMinimumSize(QtCore.QSize(250, 0))
        self.widget_5.setMaximumSize(QtCore.QSize(275, 16777215))
        self.widget_5.setObjectName("widget_5")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.widget_5)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.widget_5)
        self.label_4.setMinimumSize(QtCore.QSize(0, 30))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.widget_setting = QtWidgets.QWidget(self.widget_5)
        self.widget_setting.setObjectName("widget_setting")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.widget_setting)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(6, 20, 6, -1)
        self.formLayout.setHorizontalSpacing(10)
        self.formLayout.setObjectName("formLayout")
        self.label_5 = QtWidgets.QLabel(self.widget_setting)
        self.label_5.setMinimumSize(QtCore.QSize(30, 0))
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.doubleSpinBox_similarity = QtWidgets.QDoubleSpinBox(self.widget_setting)
        self.doubleSpinBox_similarity.setMaximum(1.0)
        self.doubleSpinBox_similarity.setSingleStep(0.1)
        self.doubleSpinBox_similarity.setProperty("value", 0.6)
        self.doubleSpinBox_similarity.setObjectName("doubleSpinBox_similarity")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBox_similarity)
        self.gridLayout_7.addLayout(self.formLayout, 0, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.widget_setting)
        self.gridLayout_6.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.widget_5)
        self.verticalLayout_4.addWidget(self.widget)
        self.verticalLayout_5.addWidget(self.widget_2)
        self.widget_6 = QtWidgets.QWidget(Form_new_task)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy)
        self.widget_6.setMinimumSize(QtCore.QSize(0, 40))
        self.widget_6.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_submit = QtWidgets.QPushButton(self.widget_6)
        self.pushButton_submit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_submit.setObjectName("pushButton_submit")
        self.horizontalLayout_4.addWidget(self.pushButton_submit)
        self.pushButton_cancel = QtWidgets.QPushButton(self.widget_6)
        self.pushButton_cancel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.horizontalLayout_4.addWidget(self.pushButton_cancel)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout_5.addWidget(self.widget_6)

        self.retranslateUi(Form_new_task)
        self.pushButton_cancel.clicked.connect(Form_new_task.handleCancel)
        self.pushButton_submit.clicked.connect(Form_new_task.handleSubmit)
        self.doubleSpinBox_similarity.valueChanged['double'].connect(Form_new_task.smilarityChanged)
        QtCore.QMetaObject.connectSlotsByName(Form_new_task)

    def retranslateUi(self, Form_new_task):
        _translate = QtCore.QCoreApplication.translate
        Form_new_task.setWindowTitle(_translate("Form_new_task", "Form"))
        self.widget_8.setProperty("class", _translate("Form_new_task", "toolbar"))
        self.label_7.setText(_translate("Form_new_task", "face_library"))
        self.label_2.setText(_translate("Form_new_task", "camera_list"))
        self.label_3.setText(_translate("Form_new_task", "camera_preview"))
        self.label_4.setText(_translate("Form_new_task", "other_setting"))
        self.label_5.setText(_translate("Form_new_task", "similarity"))
        self.pushButton_submit.setText(_translate("Form_new_task", "submit"))
        self.pushButton_submit.setProperty("class", _translate("Form_new_task", "primary"))
        self.pushButton_cancel.setText(_translate("Form_new_task", "cancel"))
        self.pushButton_cancel.setProperty("class", _translate("Form_new_task", "default"))
