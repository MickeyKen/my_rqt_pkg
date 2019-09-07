# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'second.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QLineEdit, QGridLayout, QPushButton
import rospkg

class Ui_Second(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(200, 40, 67, 17))
        self.label.setObjectName("label")

        self.combo = QtWidgets.QComboBox(Form)
        self.combo.addItem("acceleration")
        self.combo.addItem("forward")
        self.combo.addItem("rotation")
        self.combo.addItem("turning")
        self.combo.addItem("pause")
        self.combo.addItem("stop")
        self.combo.addItem("slowstop")
        self.combo.addItem("detect")
        self.combo.addItem("e")
        self.combo.addItem("end")
        self.combo.move(50, 100)
        # self.combo.setGeometry(QtCore.QRect(300, 300, 300, 200))
        self.combo.activated[str].connect(self.onActivated)

        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(80, 60, 256, 41))
        self.textBrowser.setObjectName("textBrowser")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(Form)
        self.commandLinkButton.setGeometry(QtCore.QRect(70, 140, 177, 41))
        self.commandLinkButton.setObjectName("commandLinkButton")

        self.textBrowser2 = QtWidgets.QTextBrowser(Form)
        self.textBrowser2.setStyleSheet("background-color:red")
        self.textBrowser2.setVisible(False)
        self.myLineEdit = QtWidgets.QLineEdit(Form)
        self.myLineEdit.setVisible(False)

        # image = QImage('color_image.png')
        self.imageLabel = QtWidgets.QLabel(Form)
        path = rospkg.RosPack().get_path('my_rqt_pkg') + '/scripts/color_image.png'
        self.imageLabel.setPixmap(QtGui.QPixmap(path))
        self.imageLabel.move(300,700)


        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(250, 180, 281, 120))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 0, 2, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 1, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 1, 1, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.widget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 1, 2, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.widget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 2, 0, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.widget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 2, 1, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.widget)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 2, 2, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.widget)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout.addWidget(self.pushButton_10, 3, 0, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.widget)
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout.addWidget(self.pushButton_11, 3, 1, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(self.widget)
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout.addWidget(self.pushButton_12, 3, 2, 1, 1)
        self.widget.setVisible(False)

        # self.textBrowser3 = QtWidgets.QTextBrowser(Form)
        # self.textBrowser3.setGeometry(QtCore.QRect(340, 370, 256, 192))
        # self.textBrowser3.setObjectName("textBrowser")


        self.retranslateUi(Form)
        # self.textBrowser3.anchorClicked['QUrl'].connect(Form.koushin)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "TextLabel"))
        # self.combo.setText(_translate("Form", "Motion"))
        self.commandLinkButton.setText(_translate("Form", "CommandLinkButton"))

    def onActivated(self, text):

        self.label.setText(text)
        self.label.adjustSize()
        self.textBrowser2.setVisible(False)
        self.myLineEdit.setVisible(False)
        self.widget.setVisible(False)

        if text == "stop":

            self.textBrowser2.setGeometry(QtCore.QRect(160, 60, 256, 141))
            self.textBrowser2.setObjectName("textBrowser")
            self.textBrowser2.setVisible(True)
            self.myLineEdit.setGeometry(QtCore.QRect(500, 300, 500, 50))
            self.myLineEdit.setObjectName("textBrowser")
            self.myLineEdit.setVisible(True)

        elif text == "slowstop":
            self.widget.setVisible(True)
            # pass
