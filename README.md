# 使用文档

``` BASH
source /opt/ros/jazzy/setup.bash

# 安装 colcon 编译器
sudo apt install python3-colcon-common-extensions

# colcon 查看版本
colcon version-check

# 创建工作目录
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws

# 创建工作空间
ros2 pkg create --build-type ament_cmake --license Apache-2.0 cpp_pubsub

# 自动安装相关依赖（似乎不需要执行）
rosdep install -i --from-path src --rosdistro jazzy -y

# 编译代码，ros2_ws 目录下
colcon build --packages-select cpp_pubsub

# 把路径临时加到当前终端环境
. install/setup.bash

# 启动发送节点
ros2 run cpp_pubsub talker

# 启动接收节点
ros2 run cpp_pubsub listener

# 输出 topic 消息
ros2 topic echo /address_book
```