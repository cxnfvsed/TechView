#!/usr/bin/env python

import rospy
import time
from std_msgs.msg import String

class Sender:

    def send(topic_name,signal):
        i = 0
        pub = rospy.Publisher(topic_name, String, queue_size=10)
        try:
            #rate = rospy.Rate(1)
            #time.sleep(0.5)
            i += 1
            msg = signal
            pub.publish(msg)
            #print(f"[SENT] {msg}")
            #rate.sleep()
        except Exception as e:
            rospy.logwarn(e)


class Recv:

    comList = []

    def receive(self):
        rospy.Subscriber("route_cmds", String, Recv.callback)
        rospy.spin()

    def callback(data):
        print(f"Received: {data.data}")
        rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
        Recv.comList.append(data.data)