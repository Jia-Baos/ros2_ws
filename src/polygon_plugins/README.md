# 使用文档

``` BASH
# 把路径临时加到当前终端环境

colcon build --packages-select polygon_base polygon_plugins

source install/setup.bash

ros2 plugin list

ros2 run polygon_base area_node
```