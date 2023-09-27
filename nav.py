#!/usr/bin/env python3

import rospy
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import actionlib

def get_user_input():
    x = float(input("Enter X-coordinate for the goal position: "))
    y = float(input("Enter Y-coordinate for the goal position: "))
    orientation_w = float(input("Enter the orientation (w): "))
    return x, y, orientation_w

def main():
    rospy.init_node('simple_navigation_goals')

    # Create a MoveBaseClient
    ac = actionlib.SimpleActionClient('move_base', MoveBaseAction)
    
    # Wait for the action server to come up
    if not ac.wait_for_server(rospy.Duration(5.0)):
        rospy.loginfo("Waiting for the move_base action server to come up")

    goal = MoveBaseGoal()

    # Set the frame and timestamp for the goal
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()

    # Get user input for the goal position and orientation
    x, y, orientation_w = get_user_input()

    # Set the goal position and orientation based on user input
    goal.target_pose.pose.position.x = x
    goal.target_pose.pose.position.y = y
    goal.target_pose.pose.orientation.w = orientation_w

    rospy.loginfo("Sending goal")
    ac.send_goal(goal)

    ac.wait_for_result()

    if ac.get_state() == actionlib.GoalStatus.SUCCEEDED:
        rospy.loginfo("Hooray, the base reached the goal!")
    else:
        rospy.loginfo("The base failed to reach the goal for some reason")

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass

