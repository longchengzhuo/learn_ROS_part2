from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess, IncludeLaunchDescription
# from launch.conditions import IfCondition, UnlessCondition
from launch.substitutions import Command, FindExecutable, LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from xacro import default_value


# from launch_ros.substitutions import FindPackageShare
# from launch.launch_description_sources import PythonLaunchDescriptionSource
# from launch.events import Shutdown
# from launch.actions import GroupAction, LogInfo, RegisterEventHandler, TimerAction
# from launch.event_handlers import OnProcessStart, OnProcessExit, OnExecutionComplete

def generate_launch_description():

    excort_back = DeclareLaunchArgument(name="excort_back",default_value="excort_back")
    excort_left = DeclareLaunchArgument(name="excort_left",default_value="excort_left")
    excort_right = DeclareLaunchArgument(name="excort_right",default_value="excort_right")

    master = Node(package="turtlesim",executable="turtlesim_node")
    spawn_back = Node(package="cpp05_exercise",
                      executable="exer01_spawn",
                      name="spawn_back",
                      parameters=[{"x":2.0,"y":5.0,"turtle_name":LaunchConfiguration("excort_back")}])
    spawn_left = Node(package="cpp05_exercise",
                      executable="exer01_spawn",
                      name="spawn_left",
                      parameters=[{"x":2.0,"y":5.0,"turtle_name":LaunchConfiguration("excort_left")}])
    spawn_right = Node(package="cpp05_exercise",
                      executable="exer01_spawn",
                      name="spawn_right",
                      parameters=[{"x":2.0,"y":5.0,"turtle_name":LaunchConfiguration("excort_right")}])
    turtle1_world = Node(package="cpp05_exercise",executable="exer02_tf_broadcaster",name="turtle1_world")
    back_world = Node(package="cpp05_exercise",
                      executable="exer02_tf_broadcaster",
                      name="back_world",
                      parameters=[{"turtle":LaunchConfiguration("excort_back")}])
    left_world = Node(package="cpp05_exercise",
                      executable="exer02_tf_broadcaster",
                      name="left_world",
                      parameters=[{"turtle":LaunchConfiguration("excort_left")}])
    right_world = Node(package="cpp05_exercise",
                      executable="exer02_tf_broadcaster",
                      name="right_world",
                      parameters=[{"turtle":LaunchConfiguration("excort_right")}])
    escort_goal_back = Node(package="tf2_ros",
                            executable="static_transform_publisher",
                            name="escort_goal_back",
                            arguments=["--frame-id","turtle1","--child-frame-id","escort_goal_back","--x","-1.5"]
                            )
    escort_goal_left = Node(package="tf2_ros",
                            executable="static_transform_publisher",
                            name="escort_goal_left",
                            arguments=["--frame-id","turtle1","--child-frame-id","escort_goal_left","--y","-1.5"]
                            )
    escort_goal_right = Node(package="tf2_ros",
                            executable="static_transform_publisher",
                            name="escort_goal_right",
                            arguments=["--frame-id","turtle1","--child-frame-id","escort_goal_right","--y","1.5"]
                            )
    back_escort_goal_back = Node(package="cpp05_exercise",
                                 executable="exer03_tf_listener",
                                 name="back_escort_goal_back",
                                 parameters=[{"father_frame":LaunchConfiguration("excort_back"),"child_frame":"escort_goal_back"}])
    left_escort_goal_left = Node(package="cpp05_exercise",
                                 executable="exer03_tf_listener",
                                 name="left_escort_goal_left",
                                 parameters=[{"father_frame":LaunchConfiguration("excort_left"),"child_frame":"escort_goal_left"}])
    right_escort_goal_right = Node(package="cpp05_exercise",
                                 executable="exer03_tf_listener",
                                 name="right_escort_goal_right",
                                parameters=[{"father_frame":LaunchConfiguration("excort_right"),"child_frame":"escort_goal_right"}])


    # Compile all actions into a launch description
    return LaunchDescription([
        excort_back,
        excort_left,
        excort_right,
        master,
        spawn_back,
        spawn_left,
        spawn_right,
        turtle1_world,
        back_world,
        escort_goal_back,
        back_escort_goal_back,
        left_world,
        escort_goal_left,
        left_escort_goal_left,
        right_world,
        escort_goal_right,
        right_escort_goal_right
    ])

# Entry point for the launch file
if __name__ == '__main__':
    generate_launch_description()