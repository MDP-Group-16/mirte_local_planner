#!/usr/bin/env python3
import rospy
from turtlesim.msg import Pose
from sensor_msgs.msg import LaserScan
import math

# Parameters
RADIUS = 4.0  # Radius of the circular obstacles
LASER_RANGE = 6.0  # Range for the laser scan to simulate circular obstacles
RESOLUTION = 360  # Resolution of the fake laser scan (number of points)

# Global variable to store turtle1's pose
turtle1_pose = None

def create_fake_laser_scan(turtle2_pose):
    scan = LaserScan()
    scan.header.stamp = rospy.Time.now()
    scan.header.frame_id = "turtle2"
    scan.angle_min = -math.pi
    scan.angle_max = math.pi
    scan.angle_increment = 2 * math.pi / RESOLUTION
    scan.range_min = 0.0
    scan.range_max = LASER_RANGE
    scan.ranges = [LASER_RANGE] * RESOLUTION

    if turtle1_pose:
        for i in range(RESOLUTION):
            angle = scan.angle_min + i * scan.angle_increment
            world_angle = angle + turtle2_pose.theta  # Transform angle to world frame

            # Calculate the end point of the laser ray in world coordinates
            x_end = turtle2_pose.x + LASER_RANGE * math.cos(world_angle)
            y_end = turtle2_pose.y + LASER_RANGE * math.sin(world_angle)

            # Calculate the distance from turtle1 to the laser ray end point
            dx = turtle1_pose.x - turtle2_pose.x
            dy = turtle1_pose.y - turtle2_pose.y
            distance = math.sqrt(dx ** 2 + dy ** 2)

            # Check if the distance is within the obstacle radius
            if distance <= RADIUS:
                # Calculate the angle to turtle1 from turtle2
                angle_to_turtle1 = math.atan2(dy, dx)
                # Normalize the angle difference
                angle_diff = abs(angle_to_turtle1 - world_angle)
                if angle_diff > math.pi:
                    angle_diff = 2 * math.pi - angle_diff

                # If the angle difference is within the laser scan increment, update the range
                if angle_diff < scan.angle_increment:
                    scan.ranges[i] = distance

    return scan

def pose_callback_turtle1(msg):
    global turtle1_pose
    turtle1_pose = msg

def pose_callback_turtle2(msg):
    global turtle2_scan_pub
    scan = create_fake_laser_scan(msg)
    turtle2_scan_pub.publish(scan)

if __name__ == '__main__':
    rospy.init_node('fake_laser_scan')

    turtle2_scan_pub = rospy.Publisher('/turtle2/scan', LaserScan, queue_size=10)

    rospy.Subscriber('/turtle1/pose', Pose, pose_callback_turtle1)
    rospy.Subscriber('/turtle2/pose', Pose, pose_callback_turtle2)

    rospy.spin()
