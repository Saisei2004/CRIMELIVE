cmake_minimum_required(VERSION 3.10)
project(crml_msgs)

find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)

set(msg_files
  "msg/AudioChunk.msg"
  "msg/ClipTag.msg"
  "msg/ClipTagArray.msg"
  "msg/NewsSubtitle.msg"
  "msg/PipelineState.msg"
)

rosidl_generate_interfaces(${PROJECT_NAME}
  ${msg_files}
)

ament_export_dependencies(rosidl_default_runtime)
ament_package()
