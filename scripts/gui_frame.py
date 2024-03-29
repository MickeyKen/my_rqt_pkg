#! /usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from tutorial import Ui_Form
from first import Ui_First
from second import Ui_Second
from radio_group import Ui_rg
import rospy
from geometry_msgs.msg import Twist
import rospkg
from subprocess import *
import rosnode




class Test(QDialog):
    def __init__(self,parent=None):
        # GUI。
        super(Test, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.lightGray)
        self.setPalette(p)

        # ROS。pubの設定。
        self.cmd_vel_Twist = Twist()
        self.pub_cmd_vel = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)

    def start(self):

        self.cmd_vel_Twist.angular.z = 1 # 1[rad/s]で左に回転
        self.pub_cmd_vel.publish(self.cmd_vel_Twist)
        self.cmd_vel_Twist.angular.z = 0
        window3.showMaximized()

    def slam(self):

        self.cmd_vel_Twist.linear.x = 1 # 1[m/s]で直進
        self.pub_cmd_vel.publish(self.cmd_vel_Twist)
        self.cmd_vel_Twist.linear.x = 0
        window2.showMaximized()

    def create(self):
        ROS_PROGRAM = QProcess(self)
        print "Launching..."
        program = 'roslaunch pir2_description pir2_description.launch'
        ROS_PROGRAM.start(program)
        self.cmd_vel_Twist.angular.z = -1 # 1[rad/s]で右に回転
        self.pub_cmd_vel.publish(self.cmd_vel_Twist)
        self.cmd_vel_Twist.angular.z = 0

    # def create(self):
    #     position = self.ui.pos()  # 遷移前のdlgの座標を取得
    #     size = self.ui.size()  # 遷移前のサイズを取得
    #     self.uif = Ui_First()
    #     self.uif.move(position.x(), position.y())  # 同じ位置へ
    #     self.uif.resize(size)  # 同じサイズへ
    #     # 画面の位置が完全に重なる
    #     self.uif.show()  # 遷移後のダイアログを表示
    #     self.ui.hide()  # 遷移前のダイアログを非表示

class Test2(QDialog):
    def __init__(self,parent=None):
        # GUI。
        super(Test2, self).__init__(parent)
        self.uis = Ui_Second()
        self.uis.setupUi(self)
        # ROS。pubの設定。
        self.cmd_vel_Twist = Twist()
        self.pub_cmd_vel = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)

    def koushin(self, text):
        self.cmd_vel_Twist.angular.z = -1 # 1[rad/s]で右に回転
        self.pub_cmd_vel.publish(self.cmd_vel_Twist)
        self.cmd_vel_Twist.angular.z = 0

class Test3(QDialog):
    def __init__(self,parent=None):
        # GUI。
        super(Test3, self).__init__(parent)
        self.uis = Ui_First()
        self.uis.setupUi(self)

    def show(self):
        pass
    def sample(self):
        pass
    def motor(self):
        pass

class Test4(QDialog):
    def __init__(self,parent=None):
        # GUI。
        super(Test4, self).__init__(parent)
        self.uis = Ui_rg()
        self.uis.setupUi(self)
        # ROS。pubの設定。
        self.cmd_vel_Twist = Twist()
        self.pub_cmd_vel = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)


    def bringup(self):

        self.cmd_vel_Twist.linear.x = self.uis.Dynamixel_motor.checkedId()
        self.cmd_vel_Twist.linear.y = self.uis.Lidar.checkedId()
        self.cmd_vel_Twist.linear.z = self.uis.realsense.checkedId()
        self.cmd_vel_Twist.angular.x = self.uis.Dynamixel_head.checkedId()
        self.pub_cmd_vel.publish(self.cmd_vel_Twist)
        # print self.uis.Dynamixel_motor.checkedId()

        # print("Radio: %d" % self.uis.Dynamixel_motor.checkedId())
        # window3.showMaximized()



if __name__ == '__main__':
    rospy.init_node('turtlesim_talker')
    app = QApplication(sys.argv)
    window = Test()
    window2 = Test2()
    window3 = Test3()
    window4 = Test4()
    window.showMaximized()
    sys.exit(app.exec_())
