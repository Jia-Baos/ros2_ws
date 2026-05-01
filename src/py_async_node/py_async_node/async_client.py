from example_interfaces.srv import Trigger
import rclpy
from rclpy.node import Node


class TriggerClient(Node):
    def __init__(self):
        super().__init__("trigger_client")
        self._client = self.create_client(Trigger, "trigger")

    def send_request(self):
        self.get_logger().info("Waiting for trigger service...")
        self._client.wait_for_service()

        self.get_logger().info("Service is available, sending request")
        request = Trigger.Request()
        future = self._client.call_async(request)
        rclpy.spin_until_future_complete(self, future)

        response = future.result()
        self.get_logger().info(
            f"Service responded: success={response.success}, "
            f'message="{response.message}"'
        )


def main(args=None):
    rclpy.init(args=args)
    try:
        node = TriggerClient()
        node.send_request()
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
