#!/usr/bin/env python3

import rospy
from nav_msgs.msg import Odometry

def odometry_callback(msg):
    
    linear_displacement = msg.twist.twist.linear
    angular_displacement = msg.twist.twist.angular

    rospy.loginfo(f"Linear Displacement: x={linear_displacement.x}, y={linear_displacement.y}, z={linear_displacement.z}")
    rospy.loginfo(f"Angular Displacement: x={angular_displacement.x}, y={angular_displacement.y}, z={angular_displacement.z}")

def main():
    rospy.init_node('vehicle_displacement_subscriber', anonymous=True)

   
    rospy.Subscriber('/odom', Odometry, odometry_callback)

    rospy.spin()

if __name__ == '__main__':
    main()

