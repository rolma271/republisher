import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from republisher_interfaces.action import Republish
import sys

class RepublisherClient(Node):
    def __init__(self):
        super().__init__('republisher_client')
        self.declare_parameter('text', '')
        self._text = self.get_parameter('text').get_parameter_value().string_value

        self._client = ActionClient(self, Republish, 'republish_text')
        self._client.wait_for_server()
        self.send_goal()

    def send_goal(self):
        goal_msg = Republish.Goal()
        goal_msg.text = self._text

        self._client.send_goal_async(
            goal_msg,
            feedback_callback=self.feedback_callback
        ).add_done_callback(self.goal_response_callback)

    def feedback_callback(self, feedback_msg):
        word = feedback_msg.feedback.word
        self.get_logger().info(f'{word}')

    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().error('Goal rejected :(')
            return

        self._result_future = goal_handle.get_result_async()
        self._result_future.add_done_callback(self.result_callback)

    def result_callback(self, future):
        result = future.result().result
        if result.success:
            self.get_logger().info('Texto republicado!')
        rclpy.shutdown()

def main(args=None):
    rclpy.init(args=args)
    node = RepublisherClient()
    rclpy.spin(node)
