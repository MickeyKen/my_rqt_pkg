# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'second.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QLabel, QVBoxLayout
import rospkg

class Ui_Second(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(200, 40, 67, 17))
        self.label.setObjectName("label")

        self.combo = QtWidgets.QComboBox(Form)
        self.combo.addItem("Ubuntu")
        self.combo.addItem("Mandriva")
        self.combo.addItem("Fedora")
        self.combo.addItem("Arch")
        self.combo.addItem("Gentoo")
        self.combo.move(50, 100)
        # self.combo.setGeometry(QtCore.QRect(300, 300, 300, 200))
        self.label.setObjectName("Motion")

        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(80, 60, 256, 41))
        self.textBrowser.setObjectName("textBrowser")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(Form)
        self.commandLinkButton.setGeometry(QtCore.QRect(70, 140, 177, 41))
        self.commandLinkButton.setObjectName("commandLinkButton")

        # image = QImage('color_image.png')
        self.imageLabel = QtWidgets.QLabel(Form)
        path = rospkg.RosPack().get_path('my_rqt_pkg') + '/scripts/color_image.png'
        self.imageLabel.setPixmap(QtGui.QPixmap(path))
        self.imageLabel.move(10,10)
        # self.imageLabel.scaleFactor = 1.0
        # self.layout = QVBoxLayout()
        # self.layout.addWidget(self.imageLabel)
        # Form.setLayout(self.layout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "TextLabel"))
        # self.combo.setText(_translate("Form", "Motion"))
        self.commandLinkButton.setText(_translate("Form", "CommandLinkButton"))
