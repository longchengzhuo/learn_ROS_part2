from ament_index_python import get_package_share_directory
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
from launch_ros.parameter_descriptions import ParameterValue
def generate_launch_description():
    model = DeclareLaunchArgument(name="model",default_value=get_package_share_directory("cpp06_urdf")+"/urdf/urdf/demo01_helloworld.urdf")
    p_value = ParameterValue(Command(["xacro ",LaunchConfiguration("model")]))
    robot_state_publisher = Node(package="robot_state_publisher",executable="robot_state_publisher",parameters=[{"robot_description":p_value}])
    joint_state_pub = Node(package="joint_state_publisher",executable="joint_state_publisher")

    rviz2 = Node(package="rviz2",
                 executable="rviz2",
                 arguments=["-d",get_package_share_directory("cpp06_urdf") + "/rviz/urdf.rviz"]
                 )

    # Compile all actions into a launch description
    return LaunchDescription([
        model,robot_state_publisher,joint_state_pub,rviz2
    ])

# Entry point for the launch file
if __name__ == '__main__':
    generate_launch_description()