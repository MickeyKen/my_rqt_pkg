# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tutorial.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QVBoxLayout

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.Start = QtWidgets.QPushButton(Form)
        self.Start.setGeometry(QtCore.QRect(150, 50, 40, 25))
        self.Start.setObjectName("Start")
        self.Create = QtWidgets.QPushButton(Form)
        self.Create.setGeometry(QtCore.QRect(150, 110, 40, 25))
        self.Create.setObjectName("Create")
        self.Slam = QtWidgets.QPushButton(Form)
        self.Slam.setGeometry(QtCore.QRect(150, 180, 40, 25))
        self.Slam.setObjectName("SLAM")

        self.retranslateUi(Form)
        self.Start.clicked.connect(Form.start)
        self.Create.clicked.connect(Form.create)
        self.Slam.clicked.connect(Form.slam)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.Start, self.Slam)
        Form.setTabOrder(self.Slam, self.Create)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.Start)
        self.layout.addWidget(self.Create)
        self.layout.addWidget(self.Slam)
        Form.setLayout(self.layout)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Start.setText(_translate("Form", "Execute Motion Script"))
        self.Create.setText(_translate("Form", "Create Motion Script"))
        self.Slam.setText(_translate("Form", "SLAM Mode"))
