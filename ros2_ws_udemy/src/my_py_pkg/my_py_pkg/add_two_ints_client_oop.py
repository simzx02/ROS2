#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts
from functools import partial
     
     
class AddTwoIntsClient(Node): # MODIFY NAME
    def __init__(self):
        super().__init__("add_two_ints_client_oop") # MODIFY NAME
        self.client = self.create_client(AddTwoInts, "add_two_ints")
        
    def call_add_two_ints(self, a, b):
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().warn("service not available, waiting for Int server ...")
        request = AddTwoInts.Request()
        request.a = a
        request.b = b
        future = self.client.call_async(request)

        future.add_done_callback(partial(self.callback_call_add_two_ints, request=request))

    def callback_call_add_two_ints(self, future, request):
        response = future.result()
        self.get_logger().info(str(request.a) + " + " + str(request.b) + " = " + str(response.sum))

     
     
def main(args=None):
    rclpy.init(args=args)
    node = AddTwoIntsClient() # MODIFY NAME
    node.call_add_two_ints(5, 3)
    node.call_add_two_ints(15, 3)
    node.call_add_two_ints(5, 13)
    node.call_add_two_ints(5, 113)
    rclpy.spin(node)
    rclpy.shutdown()
     
     
if __name__ == "__main__":
    main()


