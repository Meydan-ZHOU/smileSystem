# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NewFaceUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(410, 465)
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(20, 20, 20, 20)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_name = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.gridLayout.addWidget(self.lineEdit_name, 1, 1, 1, 1)
        self.lineEdit_age = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_age.setObjectName("lineEdit_age")
        self.gridLayout.addWidget(self.lineEdit_age, 3, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_image = QtWidgets.QLabel(Dialog)
        self.label_image.setText("")
        self.label_image.setObjectName("label_image")
        self.gridLayout.addWidget(self.label_image, 7, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.pushButton_upload = QtWidgets.QPushButton(Dialog)
        self.pushButton_upload.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_upload.setObjectName("pushButton_upload")
        self.gridLayout.addWidget(self.pushButton_upload, 5, 1, 1, 1)
        self.label_tip = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_tip.sizePolicy().hasHeightForWidth())
        self.label_tip.setSizePolicy(sizePolicy)
        self.label_tip.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_tip.setObjectName("label_tip")
        self.gridLayout.addWidget(self.label_tip, 6, 1, 1, 1)
        self.widget = QtWidgets.QWidget(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton_man = QtWidgets.QRadioButton(self.widget)
        self.radioButton_man.setChecked(True)
        self.radioButton_man.setObjectName("radioButton_man")
        self.horizontalLayout.addWidget(self.radioButton_man)
        self.radioButton_female = QtWidgets.QRadioButton(self.widget)
        self.radioButton_female.setObjectName("radioButton_female")
        self.horizontalLayout.addWidget(self.radioButton_female)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.gridLayout.addWidget(self.widget, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.lineEdit_tel = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_tel.setObjectName("lineEdit_tel")
        self.gridLayout.addWidget(self.lineEdit_tel, 4, 1, 1, 1)
        self.Label = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Label.sizePolicy().hasHeightForWidth())
        self.Label.setSizePolicy(sizePolicy)
        self.Label.setObjectName("Label")
        self.gridLayout.addWidget(self.Label, 5, 0, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.comboBox_library = QtWidgets.QComboBox(Dialog)
        self.comboBox_library.setObjectName("comboBox_library")
        self.gridLayout.addWidget(self.comboBox_library, 0, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 6)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.widget_2 = QtWidgets.QWidget(Dialog)
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.widget_2)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.gridLayout_2.addWidget(self.widget_2, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.pushButton_upload.clicked.connect(Dialog.openImage)
        self.pushButton.clicked.connect(Dialog.handleSubmit)
        self.pushButton_2.clicked.connect(Dialog.handleCancel)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.comboBox_library, self.lineEdit_name)
        Dialog.setTabOrder(self.lineEdit_name, self.radioButton_man)
        Dialog.setTabOrder(self.radioButton_man, self.radioButton_female)
        Dialog.setTabOrder(self.radioButton_female, self.lineEdit_age)
        Dialog.setTabOrder(self.lineEdit_age, self.lineEdit_tel)
        Dialog.setTabOrder(self.lineEdit_tel, self.pushButton_upload)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "new_single_face"))
        self.label_2.setText(_translate("Dialog", "gender"))
        self.label_3.setText(_translate("Dialog", "age"))
        self.pushButton_upload.setText(_translate("Dialog", "upload_photo"))
        self.label_tip.setText(_translate("Dialog", "please_upload_photo"))
        self.radioButton_man.setText(_translate("Dialog", "male"))
        self.radioButton_female.setText(_translate("Dialog", "female"))
        self.label_4.setText(_translate("Dialog", "telephone"))
        self.Label.setText(_translate("Dialog", "photo"))
        self.label.setText(_translate("Dialog", "name"))
        self.label_5.setText(_translate("Dialog", "face_library"))
        self.pushButton.setText(_translate("Dialog", "submit"))
        self.pushButton_2.setText(_translate("Dialog", "cancel"))
