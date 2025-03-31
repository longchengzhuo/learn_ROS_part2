from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess, IncludeLaunchDescription
# from launch.conditions import IfCondition, UnlessCondition
# from launch.substitutions import Command, FindExecutable, LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
# from launch_ros.substitutions import FindPackageShare
from launch.launch_description_sources import PythonLaunchDescriptionSource
# from launch.events import Shutdown
# from launch.actions import GroupAction, LogInfo, RegisterEventHandler, TimerAction
# from launch.event_handlers import OnProcessStart, OnProcessExit, OnExecutionComplete
from ament_index_python.packages import get_package_share_directory
import os
def generate_launch_description():
    include = IncludeLaunchDescription(
        launch_description_source=PythonLaunchDescriptionSource(
            launch_file_path=os.path.join(
                get_package_share_directory("cpp01_launch"),"launch/py","py04_args_launch.py"
            )
        ),launch_arguments=[("backg_r","0")]
    )

    # Compile all actions into a launch description
    return LaunchDescription([
        include
    ])

# Entry point for the launch file
if __name__ == '__main__':
    generate_launch_description()