import os

from ament_index_python.packages import get_package_share_directory


from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.actions import Node

joy_params=os.path.join(get_package_share_directory('my_bot'),'config','joytstick.yaml')

def generate_launch_description():

    joy_node=Node(
        package="joy",
        executable="joy_node"
        parameters=[joy_params]
    )
    teleop_node = Node(
        package="teleop_twist_joy",
        executable="teleop_node",
        parameters=[joy_params]
    )

    return LaunchDescription([
        joy_node,
        teleop_node
    ])