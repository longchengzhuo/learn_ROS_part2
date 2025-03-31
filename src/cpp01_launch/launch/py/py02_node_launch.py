import os

from launch import LaunchDescription
# from launch.actions import DeclareLaunchArgument, ExecuteProcess, IncludeLaunchDescription
# from launch.conditions import IfCondition, UnlessCondition
# from launch.substitutions import Command, FindExecutable, LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
# from launch_ros.substitutions import FindPackageShare
# from launch.launch_description_sources import PythonLaunchDescriptionSource
# from launch.events import Shutdown
# from launch.actions import GroupAction, LogInfo, RegisterEventHandler, TimerAction
# from launch.event_handlers import OnProcessStart, OnProcessExit, OnExecutionComplete
from ament_index_python import get_package_share_directory
def generate_launch_description():
    turtle1 = Node(
        package="turtlesim",
        executable="turtlesim_node",
        exec_name="my_label",
        ros_arguments=["--remap","__ns:=/t2"]
    )
    turtle2 = Node(
        package="turtlesim",
        executable="turtlesim_node",
        respawn=True,
        name="haha",
        parameters=[os.path.join(get_package_share_directory("cpp01_launch"),"config","haha.yaml")]
    )

    # Compile all actions into a launch description
    return LaunchDescription([
        turtle2
    ])

# Entry point for the launch file
if __name__ == '__main__':
    generate_launch_description()