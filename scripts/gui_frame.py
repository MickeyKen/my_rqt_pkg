#! /usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from tutorial import Ui_Form
import rospy
from geometry_msgs.msg import Twist
import rospkg


class Test(QDialog):
    def __init__(self,parent=None):
        # GUI。
        super(Test, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # ROS。pubの設定。
        self.cmd_vel_Twist = Twist()
        self.pub_cmd_vel = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)

    def start(self):

        self.cmd_vel_Twist.angular.z = 1 # 1[rad/s]で左に回転
        self.pub_cmd_vel.publish(self.cmd_vel_Twist)
        self.cmd_vel_Twist.angular.z = 0

    def slam(self):

        self.cmd_vel_Twist.linear.x = 1 # 1[m/s]で直進
        self.pub_cmd_vel.publish(self.cmd_vel_Twist)
        self.cmd_vel_Twist.linear.x = 0

    def create(self):

        self.cmd_vel_Twist.angular.z = -1 # 1[rad/s]で右に回転
        self.pub_cmd_vel.publish(self.cmd_vel_Twist)
        self.cmd_vel_Twist.angular.z = 0


if __name__ == '__main__':
    rospy.init_node('turtlesim_talker')
    app = QApplication(sys.argv)
    window = Test()
    window.show()
    sys.exit(app.exec_())
