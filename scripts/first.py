# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'first.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_First(object):
    def setupUi(self, First):
        First.setObjectName("First")
        First.resize(400, 300)
        self.radioButton = QtWidgets.QRadioButton(First)
        self.radioButton.setGeometry(QtCore.QRect(70, 90, 112, 23))
        self.radioButton.setObjectName("radioButton")
        self.pushButton = QtWidgets.QPushButton(First)
        self.pushButton.setGeometry(QtCore.QRect(170, 250, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.checkBox = QtWidgets.QCheckBox(First)
        self.checkBox.setGeometry(QtCore.QRect(260, 100, 92, 23))
        self.checkBox.setObjectName("checkBox")

        self.retranslateUi(First)
        self.pushButton.clicked.connect(First.show)
        self.radioButton.clicked.connect(First.sample)
        self.checkBox.clicked.connect(First.motor)
        QtCore.QMetaObject.connectSlotsByName(First)

    def retranslateUi(self, First):
        _translate = QtCore.QCoreApplication.translate
        First.setWindowTitle(_translate("First", "Form"))
        self.radioButton.setText(_translate("First", "RadioButton"))
        self.pushButton.setText(_translate("First", "Go second"))
        self.checkBox.setText(_translate("First", "CheckBox"))

