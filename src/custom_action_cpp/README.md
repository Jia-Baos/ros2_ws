# 使用文档

``` BASH
# 把路径临时加到当前终端环境
source install/setup.bash

colcon build --packages-select custom_action_interfaces custom_action_cpp

ros2 interface show custom_action_interfaces/action/Fibonacci

ros2 run custom_action_cpp fibonacci_action_server

ros2 run custom_action_cpp fibonacci_action_client

```