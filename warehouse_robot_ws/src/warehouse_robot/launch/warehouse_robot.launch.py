from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():

    pkg_share = get_package_share_directory('warehouse_robot')

    world = os.path.join(pkg_share, 'worlds', 'warehouse.world')

    urdf = "/opt/ros/humble/share/turtlebot3_description/urdf/turtlebot3_burger.urdf"

    gazebo = ExecuteProcess(
        cmd=[
            'gazebo',
            '--verbose',
            world,
            '-s',
            'libgazebo_ros_factory.so'
        ],
        output='screen'
    )

    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{
            'robot_description': open(urdf).read()
        }]
    )

    spawn_robot = ExecuteProcess(
        cmd=[
            'ros2',
            'run',
            'gazebo_ros',
            'spawn_entity.py',
            '-entity',
            'warehouse_robot',
            '-file',
            '/opt/ros/humble/share/turtlebot3_gazebo/models/turtlebot3_burger/model.sdf',
            '-x', '0',
            '-y', '0',
            '-z', '0.05'
        ],
        output='screen'
    )

    return LaunchDescription([
        gazebo,
        robot_state_publisher,
        spawn_robot
    ])
