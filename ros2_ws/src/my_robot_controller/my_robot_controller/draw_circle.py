#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class DrawCircleNode(Node):
    """A simple ROS 2 node that draws a circle."""
    def __init__(self):
        super().__init__('draw_circle')  # Initialize the node with a name
        self.cmd_vel_pub_ = self.create_publisher(Twist , 'turtle1/cmd_vel', 10)#10 messages to be buffered
        self.timer_=self.create_timer(0.5, self.send_velocity_command)  # Timer to call send_velocity_command every 0.1 seconds
        self.get_logger().info('Draw circle node has been started')

    def send_velocity_command(self):
        msg = Twist()
        msg.linear.x = 2.0  # Set linear velocity
        msg.angular.z = 1.0  # Set angular velocity for circular motion
        self.cmd_vel_pub_.publish(msg)  # Publish the velocity command

        # Here you would add the logic to draw a circle, e.g., using a robot arm or simulation
def main (args=None):
    rclpy.init(args=args)
    node = DrawCircleNode()  # Create an instance of the DrawCircleNode
    rclpy.spin(node)  # Keep the node running until it is shut down
    rclpy.shutdown()  # Shutdown the ROS 2 Python library