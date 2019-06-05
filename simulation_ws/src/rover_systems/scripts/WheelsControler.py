#!/usr/bin/env python

import time
import rospy
from std_msgs.msg import Float64

class WheelsController(object):
    def __init__(self):
        rospy.init_node("WheelsControler")
        rospy.loginfo("WheelsControler Initialising...")
        self.rate = rospy.Rate(100)
        self.controller_ns = "iteso_rover"
        self.controller_cmd = "command"
        self.publishers = {}
        self.controller_list = [
            "rocker_bogie_left_controler",
            "rocker_bogie_right_controler",
            "wheel_1_controller",
            "wheel_2_controller",
            "wheel_3_controller",
            "wheel_4_controller",
            "wheel_5_controller",
            "wheel_6_controller",
            "drive_steering_1_controller",
            "drive_steering_2_controller",
            "drive_steering_3_controller",
            "drive_steering_4_controller"
        ]

        self.init_publishers()

        pass

    def init_publishers(self):
        for controller_name in self.controller_list:
            topic_name = "/{}/{}/{}".format(
                self.controller_ns, 
                controller_name, 
                self.controller_cmd
            )
            self.publishers[controller_name] = rospy.Publisher(
                topic_name, 
                Float64, 
                queue_size=1
            )

        rate_wait = rospy.Rate(10)
        for controller_name in self.controller_list:
            publisher_obj = self.publishers[controller_name]
            publisher_ready = False
            while not publisher_ready:
                rospy.logwarn("Checking Publisher for... " + str(controller_name))
                pub_num = publisher_obj.get_num_connections()
                publisher_ready = (pub_num > 0)
                rate_wait.sleep()
            rospy.loginfo("Publisher" + str(controller_name) + "... READY")
        pass

    def send_cmd(self):
        ctrl = [
            "wheel_1_controller",
            "wheel_2_controller",
            "wheel_3_controller",
            "wheel_4_controller",
            "wheel_5_controller",
            "wheel_6_controller"
        ]
        while not rospy.is_shutdown():
            for controller_name in ctrl:
                publisher_obj = self.publishers[controller_name]
                publisher_obj.publish(5)
            self.rate.sleep()
        pass

if __name__ == "__main__":
    controller = WheelsController()
    controller.send_cmd()