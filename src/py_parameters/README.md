# 使用文档

``` BASH
# 把路径临时加到当前终端环境
source install/setup.bash

ros2 run py_parameters minimal_param_node

# list the params
ros2 param list

# modify the param
ros2 param set /minimal_param_node my_parameter earth
```