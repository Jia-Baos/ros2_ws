import threading
import time

from example_interfaces.srv import Trigger
import rclpy
from rclpy.node import Node
from rclpy.executors import MultiThreadedExecutor


class TriggerServer(Node):
    def __init__(self):
        super().__init__("trigger_server")
        self._service = self.create_service(Trigger, "trigger", self._callback)
        self._lock = threading.Lock()

    def _callback(self, request, response):
        self.get_logger().info("Incoming trigger request")
        with self._lock:
            time.sleep(2)
        response.success = True
        response.message = "Slept for 2.0s (async with executor)"
        return response


def main(args=None):
    rclpy.init(args=args)
    node = None
    executor = None
    try:
        node = TriggerServer()
        executor = MultiThreadedExecutor(num_threads=4)
        executor.add_node(node)
        executor.spin()
    except Exception:
        pass
    finally:
        if executor and node:
            executor.remove_node(node)
            node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
