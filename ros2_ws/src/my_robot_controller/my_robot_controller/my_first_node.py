#!/usr/bin/env python3
import rclpy #python lib for ros. needed anytime we want to use ros in python
from rclpy.node import Node #Node is the base class for all ROS nodes in python

class MyNode(Node):
    """A simple ROS 2 node that logs a message."""
    def __init__(self):
        super().__init__('first_node') #initialize the node with a name
        self.counter_ = 0
        self.create_timer(1.0, self.timer_callback) #create a timer that calls the callback function every second
        

    def timer_callback(self):
        """A callback function that can be used for periodic tasks."""
        self.get_logger().info('Hello ' + str(self.counter_))
        self.counter_ += 1

def main(args=None):
    rclpy.init(args=args) #initialize the ros python library
    node = MyNode() #create an instance of MyNode
    rclpy.spin(node) #keep the node running until Ctrl+C is pressed

    rclpy.shutdown() #shutdown the ros python library

if __name__ == '__main__':
    main() # this will call the main function when the script is run
