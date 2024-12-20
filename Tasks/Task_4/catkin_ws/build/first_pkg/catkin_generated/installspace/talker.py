#!/ usr/bin/env python3

import rospy
from std_msgs.msg import String


def talker() :
    pub = rospy.Publisher('chatter', String, queue_size=10)         # publish on 'chatter'
    rospy.init_node('mostafa_talker', anonymous=True)               # Initialize the node (name = 'talker')
    rate = rospy.Rate(10)                                           # 10 Messages per Second 

    while not rospy.is_shutdown() :                                 # While the node is running
        hello_string = "Hi Mostafa %s" % rospy.get_time()           
        rospy.loginfo(hello_string)                                 # print the string on terminal
        pub.publish(hello_string)                                   # start publishing
        rate.sleep()

if __name__ == '__main__' :
    try :
        talker()
    except rospy.ROSInterruptException :
        pass
