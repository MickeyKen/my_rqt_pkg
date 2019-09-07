# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bringup.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(952, 678)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(161, 164, 116, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(161, 236, 57, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(161, 308, 93, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(161, 380, 109, 17))
        self.label_4.setObjectName("label_4")
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(499, 164, 49, 23))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Form)
        self.radioButton_2.setGeometry(QtCore.QRect(499, 236, 49, 23))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(Form)
        self.radioButton_3.setGeometry(QtCore.QRect(499, 308, 49, 23))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(Form)
        self.radioButton_4.setGeometry(QtCore.QRect(499, 380, 49, 23))
        self.radioButton_4.setObjectName("radioButton_4")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(310, 480, 301, 25))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.bringup)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Dynamixel wheel"))
        self.label_2.setText(_translate("Form", "2D Lidar"))
        self.label_3.setText(_translate("Form", "RGB-D sensor"))
        self.label_4.setText(_translate("Form", "Dynamixel head"))
        self.radioButton.setText(_translate("Form", "use"))
        self.radioButton_2.setText(_translate("Form", "use"))
        self.radioButton_3.setText(_translate("Form", "use"))
        self.radioButton_4.setText(_translate("Form", "use"))
        self.pushButton.setText(_translate("Form", "launch"))

