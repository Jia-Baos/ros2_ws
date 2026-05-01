# 使用文档

``` BASH
# 把路径临时加到当前终端环境
source install/setup.bash

colcon build --packages-select cpp_parameter_event_handler

ros2 run cpp_parameter_event_handler parameter_event_handler

ros2 param set node_with_parameters an_int_param 43

```