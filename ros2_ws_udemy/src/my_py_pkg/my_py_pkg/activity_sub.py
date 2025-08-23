#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64
     
     
class MyNumberCounter(Node): # MODIFY NAME
    def __init__(self):
        super().__init__("number_counter") # MODIFY NAME
        self.counter_ = 0
        self.publisher_ = self.create_publisher(Int64, 'number_count', 10)
        self_subscriber_ = self.create_subscription(
            Int64, 'number', self.listener_callback, 10)
        self.get_logger().info("Number Counter is online!")

    def listener_callback(self, msg: Int64):
        
        integer = msg.data
        self.counter_ += integer
        self.get_logger().info(f"Published count: {self.counter_}")
        new_msg = Int64()
        new_msg.data = self.counter_
        self.publisher_.publish(new_msg)
        #self.get_logger().info(f"Published total count: {new_msg.data}")
     
     
def main(args=None):
    rclpy.init(args=args)
    node = MyNumberCounter() # MODIFY NAME
    rclpy.spin(node)
    rclpy.shutdown()
     
     
if __name__ == "__main__":
    main()


