#!/usr/bin/env python3
import rospy
import tf
from turtlesim.msg import Pose

def handle_turtle_pose(msg, turtle_name):
    br = tf.TransformBroadcaster()
    br.sendTransform((msg.x, msg.y, 0),
                     tf.transformations.quaternion_from_euler(0, 0, msg.theta),
                     rospy.Time.now(),
                     turtle_name,
                     "world")

if __name__ == '__main__':
    rospy.init_node('tf_broadcaster')
    turtle_name = rospy.get_param('~turtle_name')
    rospy.Subscriber('/%s/pose' % turtle_name,
                     Pose,
                     handle_turtle_pose,
                     turtle_name)
    rospy.spin()
