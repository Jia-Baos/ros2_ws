# 使用文档

``` BASH
source /opt/ros/jazzy/setup.bash

# 安装 colcon 编译器
sudo apt install python3-colcon-common-extensions

# colcon 查看版本
colcon version-check

# 创建工作目录
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src

# 创建工作空间
ros2 pkg create --build-type ament_cmake --license Apache-2.0 cpp_pubsub

# 自动安装相关依赖（似乎不需要执行）
rosdep install -i --from-path src --rosdistro jazzy -y

# 编译代码，ros2_ws 目录下
colcon build --packages-select cpp_pubsub

# 把路径临时加到当前终端环境
source install/setup.bash

# 输出 msg 内容
ros2 interface show tutorial_interfaces/msg/Num

# 输出 topic 消息
ros2 topic echo /address_book

# 输出 plugin 列表
ros2 plugin list

# 输出完整报告
ros2 doctor --report
```

## Publishing messages using YAML files

```BASH
ros2 topic echo --once  /cmd_vel > cmd_vel.yaml

ros2 topic pub /cmd_vel geometry_msgs/msg/Twist --yaml-file cmd_vel.yaml
```

## ```rosdep```

rosdep 是一款依赖管理工具，可用于处理功能包及外部库的依赖关系。它是一个命令行工具，作用是识别并安装编译、运行功能包所需的依赖。

rosdep 本身并不是独立的包管理器，而是一款元包管理工具：它依托自身对当前系统和依赖关系的内置数据库，自动匹配适配当前系统平台的安装包。实际的软件安装操作，仍由系统原生包管理器完成（例如 Debian/Ubuntu 上的 apt、Fedora/RHEL 上的 dnf 等）。

rosdep 最常用的场景是编译工作空间之前，自动安装工作空间内所有功能包的全部依赖。

它既可以针对单个功能包处理依赖，也能批量处理整个功能包目录（比如整个 ROS 工作空间）。

[参考链接](https://docs.ros.org/en/rolling/index.html)