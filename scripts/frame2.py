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
        p.setColor(self.backgroundRole(), Qt.lightGray)
        self.setPalette(p)

        self.cmd_vel_Twist = Twist()
        self.pub_cmd_vel = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)

    def start(self):

        self.cmd_vel_Twist.angular.z = 1 
        self.pub_cmd_vel.publish(self.cmd_vel_Twist)
        self.cmd_vel_Twist.angular.z = 0


if __name__ == '__main__':
    rospy.init_node('casher_program')
    app = QApplication(sys.argv)
    window = Test()
    window.show()
    sys.exit(app.exec_())
