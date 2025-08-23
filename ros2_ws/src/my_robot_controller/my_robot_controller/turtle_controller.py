#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

class TurtleControllerNode(Node):
    def __init__(self):
        super().__init__('turtle_controller')
        self.cmd_vel_publisher_ = self.create_publisher(
            Twist, 
            'turtle1/cmd_vel', 
            10
        )
        self.pose_subscriber_ = self.create_subscription(
            Pose, 
            'turtle1/pose', 
            self.pose_callback, 
            10
        )
        self.get_logger().info("Turtle Controller Node has been initialized.")
    
    def pose_callback(self, pose: Pose):
        cmd = Twist()
        if pose.x > 9.0 or pose.x < 2.0 or pose.y > 9.0 or pose.y < 2.0:
            cmd.linear.x = 1.0  # Stop moving forward
            cmd.angular.z = 0.9  # Stop rotating
        else:
            cmd.linear.x = 5.0  # Move forward at 1 m/s
            cmd.angular.z = 0.0  # No rotation
        self.cmd_vel_publisher_.publish(cmd)
        #self.get_logger().info("Turtle Position: (" + str(msg.x) + ", " + str(msg.y) + ") at angle " + str(msg.theta))

def main(args=None):
    rclpy.init(args=args)
    node = TurtleControllerNode()
    rclpy.spin(node)
    rclpy.shutdown()