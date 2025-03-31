from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess, IncludeLaunchDescription
# from launch.conditions import IfCondition, UnlessCondition
# from launch.substitutions import Command, FindExecutable, LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node

# from launch_ros.substitutions import FindPackageShare
# from launch.launch_description_sources import PythonLaunchDescriptionSource
# from launch.events import Shutdown
from launch.actions import GroupAction, LogInfo, RegisterEventHandler, TimerAction
from launch.event_handlers import OnProcessStart, OnProcessExit, OnExecutionComplete

def generate_launch_description():
    turtle = Node(
        package = "turtlesim",
        executable="turtlesim_node"
    )
    spawn = ExecuteProcess(
        cmd=["ros2 service call /spawn turtlesim/srv/Spawn \"{'x':8.0,'y':3.0}\""],
        output="both",
        shell=True
    )
    event_start = RegisterEventHandler(
        event_handler=OnProcessStart(
            target_action=turtle,
            on_start=spawn
        )
    )
    event_exit = RegisterEventHandler(
        event_handler=OnProcessExit(
            target_action=turtle,
            on_exit=LogInfo(msg="turtlesim_node exit!----------")
        )
    )
    # Compile all actions into a launch description
    return LaunchDescription([
        turtle,event_start,event_exit
    ])

# Entry point for the launch file
if __name__ == '__main__':
    generate_launch_description()