from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument(
            'text',
            default_value='Lorem ipsum dolor sit amet consectetur adipiscing',
            description='Texto a republicar'
        ),
        Node(
            package='republisher',
            executable='republisher_server',
            name='nodo1'
        ),
        Node(
            package='republisher',
            executable='republisher_client',
            name='nodo2',
            arguments=[LaunchConfiguration('text')]
        )
    ])
