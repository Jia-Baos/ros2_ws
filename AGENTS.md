# AGENTS.md - ROS2 Workspace Development Guide

This is a ROS2 workspace (`ros2_ws`) using the Jazzy distribution with multiple C++ and Python packages.

## Build Commands

### Prerequisites
```bash
source /opt/ros/jazzy/setup.bash
sudo apt install python3-colcon-common-extensions
```

### Build All Packages
```bash
colcon build
```

### Build Specific Package
```bash
colcon build --packages-select <package_name>
# Example: colcon build --packages-select cpp_pubsub
```

### Build with Options
```bash
colcon build --cmake-args -DCMAKE_BUILD_TYPE=Release
colcon build --symlink-install  # Symlink instead of copy (faster iteration)
```

### Clean Build
```bash
rm -rf build/ install/ log/
colcon build
```

### Run Tests
```bash
colcon test
colcon test --packages-select <package_name>
colcon test-result --all
```

### Build and Test Single Package
```bash
colcon build --packages-select <package_name> && colcon test --packages-select <package_name>
```

## Code Style Guidelines

### General
- **C++ Standard**: C++17 (enforced in CMakeLists.txt)
- **Format Style**: LLVM-based (see `.clang-format`)
- **Linting**: clang-tidy with `readability-identifier-naming` checks (see `.clang-tidy`)

### Formatting Rules (from .clang-format)
- **Indent**: 4 spaces (no tabs)
- **Access Modifier Offset**: -4 (private/protected indented less)
- **Braces**: Custom style - Opening brace on new line for functions (`AfterFunction: true`)
- **Line Length**: Unlimited (`ColumnLimit: 0`)
- **Pointer Alignment**: Right (`PointerAlignment: Right`)
- **Namespace Indentation**: Inner only

### Naming Conventions (from .clang-tidy)
| Element | Convention | Example |
|---------|-----------|---------|
| Variables | lower_case | `count_`, `timer_callback` |
| Class/Struct Names | CamelCase | `MinimalPublisher`, `RegularPolygon` |
| Functions | CamelCase | `createPublisher`, `handleService` |
| Namespaces | lower_case | `polygon_base`, `polygon_plugins` |
| Constants | kCamelCase | `kDefaultValue` |
| Enums | kCamelCase | `kEnumValue` |
| Macros | UPPER_CASE | `MAX_BUFFER_SIZE` |
| Private Members | lower_case with `_` suffix | `timer_`, `publisher_` |

### File Organization
```
package_name/
├── CMakeLists.txt
├── package.xml
├── include/
│   └── package_name/
│       └── *.hpp
├── src/
│   └── *.cpp
├── msg/
│   └── *.msg
├── srv/
│   └── *.srv
└── test/
    └── *.cpp
```

### Include Order
1. Implementation header (e.g., `"polygon_plugins/polygon_plugins.hpp"`)
2. ROS2 headers (e.g., `"rclcpp/rclcpp.hpp"`)
3. Message headers (e.g., `"std_msgs/msg/string.hpp"`)
4. Standard library headers (e.g., `<memory>`, `<string>`)
5. Third-party headers

### ROS2 Node Patterns

**Publisher Node (Lambda)**
```cpp
#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"

using namespace std::chrono_literals;

class MinimalPublisher : public rclcpp::Node
{
public:
  MinimalPublisher()
  : Node("minimal_publisher"), count_(0)
  {
    publisher_ = this->create_publisher<std_msgs::msg::String>("topic", 10);
    auto timer_callback = [this]() -> void {
      // ... publish logic
    };
    timer_ = this->create_wall_timer(500ms, timer_callback);
  }

private:
  rclcpp::TimerBase::SharedPtr timer_;
  rclcpp::Publisher<std_msgs::msg::String>::SharedPtr publisher_;
  size_t count_;
};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<MinimalPublisher>());
  rclcpp::shutdown();
  return 0;
}
```

**Subscriber Node (Lambda)**
```cpp
#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"

class MinimalSubscriber : public rclcpp::Node
{
public:
  MinimalSubscriber()
  : Node("minimal_subscriber")
  {
    auto topic_callback = [this](std_msgs::msg::String::UniquePtr msg) -> void {
      RCLCPP_INFO(this->get_logger(), "I heard: '%s'", msg->data.c_str());
    };
    subscription_ = this->create_subscription<std_msgs::msg::String>("topic", 10, topic_callback);
  }

private:
  rclcpp::Subscription<std_msgs::msg::String>::SharedPtr subscription_;
};
```

### Logging
- Use `RCLCPP_INFO()`, `RCLCPP_WARN()`, `RCLCPP_ERROR()` for logging
- Use `RCLCPP_INFO_STREAM()` for stream-style logging
- Use `(void)variable` to suppress unused parameter warnings

### CMakeLists.txt Requirements
```cmake
cmake_minimum_required(VERSION 3.5)  # or 3.8 for message generation
project(package_name)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
# ... other dependencies

# Executables
add_executable(talker src/publisher.cpp)
target_link_libraries(talker PUBLIC rclcpp::rclcpp ${std_msgs_TARGETS})

# Install
install(TARGETS talker listener DESTINATION lib/${PROJECT_NAME})

ament_package()
```

### Header Guards
```cpp
#ifndef PACKAGE_NAME__FILE_NAME_HPP_
#define PACKAGE_NAME__FILE_NAME_HPP_
// ... content
#endif  // PACKAGE_NAME__FILE_NAME_HPP_
```

### Interface Definitions (msg/srv)

**Message (.msg)**
```msg
int64 num
string name
```

**Service (.srv)**
```srv
int64 a
int64 b
---
int64 sum
```

## Running Nodes

```bash
source /opt/ros/jazzy/setup.bash
source install/setup.bash

# Run a node
ros2 run <package_name> <executable_name>

# List topics
ros2 topic list

# Echo topic
ros2 topic echo /topic_name

# Show message interface
ros2 interface show <package_name>/msg/<MessageName>
```
