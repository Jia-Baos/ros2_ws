import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node

class MinimalParam(Node):
    def __init__(self):
        super().__init__('minimal_param_node')

        self.declare_parameter('my_parameter', 'world')

        self.timer = self.create_timer(1, self.timer_callback)

    def timer_callback(self):
        my_param = self.get_parameter('my_parameter').get_parameter_value().string_value

        self.get_logger().info('Hello %s!' % my_param)

        # my_new_param = rclpy.parameter.Parameter(
        #     'my_parameter',
        #     rclpy.Parameter.Type.STRING,
        #     'world'
        # )
        # all_new_parameters = [my_new_param]
        # self.set_parameters(all_new_parameters)

def main(args=None):
    # 初始化 ROS2（正确写法！）
    rclpy.init(args=args)
    
    # 创建节点
    node = MinimalParam()
    
    # 循环运行
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    # 销毁节点 + 关闭 ROS2
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()