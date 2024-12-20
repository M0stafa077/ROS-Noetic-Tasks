#!/ usr/bin/env python3

import rospy
from std_msgs.msg import String

def callback_function(received_str:String) :
    rospy.loginfo('I heard %s', received_str.data)


def listener() :
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('chatter', String, callback_function)

if __name__ == '__main__' :
    try :
        listener()
    except rospy.ROSInterruptException :
        pass