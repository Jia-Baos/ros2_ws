# 使用文档

``` BASH
# 把路径临时加到当前终端环境
source install/setup.bash

colcon build --packages-select py_parameter_event_handler

ros2 run py_parameter_event_handler node_with_parameters

ros2 param set node_with_parameters an_int_param 43

```