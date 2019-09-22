# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'casher_sample.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1366, 768)
        self.dial = QtWidgets.QDial(Form)
        self.dial.setGeometry(QtCore.QRect(100, 60, 481, 431))
        self.dial.setObjectName("dial")
	self.dial.setStyleSheet('background-color:#f5f5f5')

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(620, 100, 221, 141))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setIcon(QtGui.QIcon('drink2.png'))
        self.pushButton.setIconSize(QtCore.QSize(221,141))
	self.pushButton.setStyleSheet('background-color:#eee8aa')

        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(620, 300, 221, 141))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setIcon(QtGui.QIcon('noodle2.png'))
        self.pushButton_2.setIconSize(QtCore.QSize(221,141))
	self.pushButton_2.setStyleSheet('background-color:#eee8aa')

        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(880, 100, 221, 141))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setIcon(QtGui.QIcon('okashi2.png'))
        self.pushButton_3.setIconSize(QtCore.QSize(221,141))
	self.pushButton_3.setStyleSheet('background-color:#eee8aa')

        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(880, 300, 221, 141))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setIcon(QtGui.QIcon('dagashi2.png'))
        self.pushButton_4.setIconSize(QtCore.QSize(221,141))
	self.pushButton_4.setStyleSheet('background-color:#eee8aa')

        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(880, 490, 221, 71))
        self.pushButton_5.setObjectName("pushButton_5")
	self.pushButton_5.setStyleSheet('background-color:#ffff00')

        self.lcdNumber = QtWidgets.QLCDNumber(Form)
        self.lcdNumber.setGeometry(QtCore.QRect(670, 500, 151, 51))
        self.lcdNumber.setObjectName("lcdNumber")
	self.lcdNumber.setStyleSheet('background-color:#ffffff')

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(300, 250, 111, 41))
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", ""))
        self.pushButton_2.setText(_translate("Form", ""))
        self.pushButton_3.setText(_translate("Form", ""))
        self.pushButton_4.setText(_translate("Form", ""))
        self.pushButton_5.setText(_translate("Form", ""))
        self.label.setText(_translate("Form", "Lee"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

