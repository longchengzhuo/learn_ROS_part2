from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess, IncludeLaunchDescription
# from launch.conditions import IfCondition, UnlessCondition
from launch.substitutions import Command, FindExecutable, LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
# from launch_ros.substitutions import FindPackageShare
# from launch.launch_description_sources import PythonLaunchDescriptionSource
# from launch.events import Shutdown
# from launch.actions import GroupAction, LogInfo, RegisterEventHandler, TimerAction
# from launch.event_handlers import OnProcessStart, OnProcessExit, OnExecutionComplete

def generate_launch_description():
    t2 = DeclareLaunchArgument(name="t2_name",default_value="t2")
    turtle = Node(package="turtlesim",executable="turtlesim_node")
    spawn = Node(package="cpp05_exercise",executable="exer01_spawn",parameters=[{"turtle_name":LaunchConfiguration("t2_name")}])
    broadcaster1 = Node(package="cpp05_exercise",executable="exer02_tf_broadcaster",name="broa1")
    broadcaster2 = Node(package="cpp05_exercise",executable="exer02_tf_broadcaster",name="broa2",parameters=[{"turtle":LaunchConfiguration("t2_name")}])

    listener = Node(package="cpp05_exercise",executable="exer03_tf_listener",parameters=[{"father_frame":LaunchConfiguration("t2_name"),"child_frame":"turtle1"}])
# Compile all actions into a launch description
    return LaunchDescription([
        t2,
        turtle,
        spawn,
        broadcaster1,
        broadcaster2,
        listener
    ])

# Entry point for the launch file
if __name__ == '__main__':
    generate_launch_description()