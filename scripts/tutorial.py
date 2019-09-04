# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tutorial.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.Start = QtWidgets.QPushButton(Form)
        self.Start.setGeometry(QtCore.QRect(150, 50, 89, 25))
        self.Start.setObjectName("Start")
        self.Create = QtWidgets.QPushButton(Form)
        self.Create.setGeometry(QtCore.QRect(150, 110, 89, 25))
        self.Create.setObjectName("Create")
        self.SLAM = QtWidgets.QPushButton(Form)
        self.SLAM.setGeometry(QtCore.QRect(150, 180, 89, 25))
        self.SLAM.setObjectName("SLAM")

        self.retranslateUi(Form)
        self.Start.clicked.connect(Form.start)
        self.Create.clicked.connect(Form.create)
        self.SLAM.clicked.connect(Form.slam)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.Start, self.SLAM)
        Form.setTabOrder(self.SLAM, self.Create)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Start.setText(_translate("Form", "PushButton"))
        self.Create.setText(_translate("Form", "PushButton"))
        self.SLAM.setText(_translate("Form", "PushButton"))

