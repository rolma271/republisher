import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from republisher_interfaces.action import Republish
import time

class RepublisherServer(Node):
    def __init__(self):
        super().__init__('republisher_server')
        self._action_server = ActionServer(
            self,
            Republish,
            'republish_text',
            self.execute_callback
        )

    async def execute_callback(self, goal_handle):
        text = goal_handle.request.text
        words = text.split()

        for word in words:
            feedback = Republish.Feedback()
            feedback.word = word
            goal_handle.publish_feedback(feedback)
            self.get_logger().info(f'Republicando: {word}')
            time.sleep(1.0)

        goal_handle.succeed()
        result = Republish.Result()
        result.success = True
        return result

def main(args=None):
    rclpy.init(args=args)
    node = RepublisherServer()
    rclpy.spin(node)
    rclpy.shutdown()
