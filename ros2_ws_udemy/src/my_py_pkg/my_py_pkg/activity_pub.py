#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64
     
     
class NumPublisherNode(Node): # MODIFY NAME
    def __init__(self):
        super().__init__("number_publisher") # MODIFY NAME
        self.number_ = 2
        self.publisher_ = self.create_publisher(Int64, 'number', 10)
        self.timer_ = self.create_timer(1, self.publish_number)
        self.get_logger().info("Number Publisher is online!")

    def publish_number(self):
        integer = Int64()
        integer.data = self.number_
        self.publisher_.publish(integer)
        #self.get_logger().info(f"Published: {integer.data}")
     
def main(args=None):
    rclpy.init(args=args)
    node = NumPublisherNode() # MODIFY NAME
    rclpy.spin(node)
    rclpy.shutdown()
     
     
if __name__ == "__main__":
    main()


