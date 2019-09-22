#! /usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from casher_sample import Ui_Form
import rospy
from geometry_msgs.msg import Twist
import rospkg
from subprocess import *
import rosnode


class Test(QDialog):
    def __init__(self,parent=None):
        super(Test, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        p = self.palette()
        p.setColor(self.backgroundRole(), QColor(190, 190, 190))
        self.setPalette(p)

	self.cy = 0
	self.name = ""

        self.ui.dial.setMinimum(0)
        self.ui.dial.setMaximum(14) 
        self.ui.dial.setValue(0)
	self.ui.dial.valueChanged.connect(self.sliderMoved)
        name = "Lee"
        self.ui.label.setFont(QFont("Times", 16, QFont.Bold))
        self.ui.label.setText(name)

        self.ui.pushButton_5.setFont(QFont("ＭＳ 明朝", 22, QFont.Bold))
        self.ui.pushButton_5.setText("精算")

        # add signals
        self.ui.pushButton.clicked.connect(self.drink)
        self.ui.pushButton_2.clicked.connect(self.cup)
        self.ui.pushButton_3.clicked.connect(self.okashi)
        self.ui.pushButton_4.clicked.connect(self.dagashi)
        self.ui.pushButton_5.clicked.connect(self.cash)

    def sliderMoved(self):
	value = self.ui.dial.value()
	name=""
        if value == 0:
	  name = "Lee"
	elif value == 1:
	  name = "yamazoe"
	elif value == 2:
	  name = "kuroda"
	elif value == 3:
	  name = "Tran"
	elif value == 4:
	  name = "kojima"
	elif value == 5:
	  name = "fujii"
	elif value == 6:
	  name = "Miran"
	elif value == 7:
	  name = "Frank"
	elif value == 8:
	  name = "Oozono"
	elif value == 9:
	  name = "Sei"
	elif value == 10:
	  name = "nakamura"
	elif value == 11:
	  name = "imazaike"
	elif value == 12:
	  name = "imanaka"
	elif value == 13:
	  name = "miki"
	elif value == 14:
	  name = "yamamoto"
	else:
	  pass
	self.name = name 
        self.ui.label.setFont(QFont("Times", 16, QFont.Bold))
        self.ui.label.setText(name)

        print("Dial value = %i" % (self.ui.dial.value()))

    def drink(self):
	self.cy += 100
	self.display()
    def cup(self):
	self.cy += 100
	self.display()
    def okashi(self):
	self.cy += 100
	self.display()
    def dagashi(self):
	self.cy += 30
	self.display()
    def cash(self):
 	QMessageBox.information(self, "精算", "名前:  " + self.name + "\n" + "合計: " + str(self.cy) + "円")
	self.init()

    def init(self):
	self.cy = 0
	self.display()
        self.ui.dial.setValue(0)


    def display(self):
	 self.ui.lcdNumber.display(self.cy)

if __name__ == '__main__':
    rospy.init_node('casher_program')
    app = QApplication(sys.argv)
    window = Test()
    window.show()
    sys.exit(app.exec_())
