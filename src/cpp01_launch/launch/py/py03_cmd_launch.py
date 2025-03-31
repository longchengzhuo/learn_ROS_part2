from launch import LaunchDescription
from launch.actions import ExecuteProcess
# from launch.actions import DeclareLaunchArgument, ExecuteProcess, IncludeLaunchDescription
# from launch.conditions import IfCondition, UnlessCondition
# from launch.substitutions import Command, FindExecutable, LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
# from launch_ros.substitutions import FindPackageShare
# from launch.launch_description_sources import PythonLaunchDescriptionSource
# from launch.events import Shutdown
# from launch.actions import GroupAction, LogInfo, RegisterEventHandler, TimerAction
# from launch.event_handlers import OnProcessStart, OnProcessExit, OnExecutionComplete

def generate_launch_description():
    turtle = Node(package="turtlesim",executable="turtlesim_node")

    cmd = ExecuteProcess(
        cmd=["ros2 topic echo /turtle1/pose"],
        output="both",
        shell=True
    )

    # Compile all actions into a launch description
    return LaunchDescription([
        turtle,
        cmd
    ])

# Entry point for the launch file
if __name__ == '__main__':
    generate_launch_description()