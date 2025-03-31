from launch import LaunchDescription
# from launch.actions import DeclareLaunchArgument, ExecuteProcess, IncludeLaunchDescription
# from launch.conditions import IfCondition, UnlessCondition
# from launch.substitutions import Command, FindExecutable, LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node, PushRosNamespace
# from launch_ros.substitutions import FindPackageShare
# from launch.launch_description_sources import PythonLaunchDescriptionSource
# from launch.events import Shutdown
from launch.actions import GroupAction, LogInfo, RegisterEventHandler, TimerAction
# from launch.event_handlers import OnProcessStart, OnProcessExit, OnExecutionComplete

def generate_launch_description():
    t1 = Node(
        package="turtlesim",executable="turtlesim_node",name="t1"
    )
    t2 = Node(
        package="turtlesim",executable="turtlesim_node",name="t2"
    )
    t3 = Node(
        package="turtlesim",executable="turtlesim_node",name="t3"
    )
    g1 = GroupAction(actions=[PushRosNamespace("g1"),t1,t2])
    g2 = GroupAction(actions=[PushRosNamespace("g2"),t3])
    # Compile all actions into a launch description
    return LaunchDescription([
        g1,g2
    ])

# Entry point for the launch file
if __name__ == '__main__':
    generate_launch_description()