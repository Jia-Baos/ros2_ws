# 使用文档

``` BASH
# 把路径临时加到当前终端环境
source install/setup.bash

colcon build --packages-select custom_action_interfaces

ros2 interface show custom_action_interfaces/action/Fibonacci

```