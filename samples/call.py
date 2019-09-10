#!/usr/bin/env python
import roslaunch
import rospy
from subprocess import * 
import rosnode
import time



def kill_node(nodename):
  p2 = Popen(['rosnode','list'],stdout=PIPE)
  p2.wait()
  nodelist=p2.communicate()
  nd=nodelist[0]
  nd=nd.split("\n")
  for i in range(len(nd)):
    tmp=nd[i]
    ind=tmp.find(nodename)
    if ind==1:
      call(['rosnode','kill',nd[i]])
      break


rospy.init_node('tester3', anonymous=True)

#cmd = ["rosrun","pcl_ros","pointcloud_to_pcd","input:=camera/depth/points"]
cmd = ["roslaunch","pir2_description","pir2_description.launch"]
proc = Popen(cmd)
#proc = call(cmd)
#time.sleep(1)  # maybe needed to wait the process to do something useful
print "finish"
time.sleep(5)
#proc.kill()

isNodeAlive=rosnode.rosnode_ping("/rviz",max_count=1,verbose=False)
print isNodeAlive
if isNodeAlive:
  kill_node('rviz')
