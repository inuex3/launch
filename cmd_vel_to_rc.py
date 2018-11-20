#!/usr/bin/python
# -*- coding:utf-8 -*-

import rospy
import time
from geometry_msgs.msg import Twist,TwistStamped
from mavros_msgs.msg import Thrust,OverrideRCIn,ActuatorControl

control = OverrideRCIn()

def teleop():
    linear_value = 1
    angular_value = 1

    while not rospy.is_shutdown():
	control = OverrideRCIn() #1:steering,2:thrust
	#control.channels = [1500, 1500, 1500, 1500, 1325, 1560, 2000, 1500]
	#pub_rc.publish(control)
       	time.sleep(0.5)
	control.channels = [1100, 1900, 1500, 1500, 1500, 1500, 1500, 1500]
	pub_rc.publish(control)
       	time.sleep(0.5)

def input():
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    new = termios.tcgetattr(fd)
    new[3] &= ~termios.ICANON
    new[3] &= ~termios.ECHO

    try:
        termios.tcsetattr(fd, termios.TCSANOW, new)
        i,o,e = select.select([sys.stdin],[],[], 0.1)
        if (i):
            key = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSANOW, old)

    if (i):
        return key
    else:
        return None   

if __name__=="__main__":
    pub_rc = rospy.Publisher('/mavros/rc/override', OverrideRCIn, queue_size = 1)
    rospy.init_node('teleop_twist_keyboard')
    manual_str = "ready to sanyo_keyboard_teleop\n\rw:forward, a:left, s:backward, d:right\n\re:r_forward, q:l_forward, z:l_backward, c:r_backward\n\ri:linear speed increase, o:decrease\n\rk:angular speed increase, l:decrease\n\r0:exit"

    print manual_str

    teleop()
