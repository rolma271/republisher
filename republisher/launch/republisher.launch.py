from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    text_arg = DeclareLaunchArgument(
        'text',
        default_value='Lorem ipsum dolor sit amet',
        description='Texto a republicar'
    )
    text = LaunchConfiguration('text')

    republisher_server = Node(
        package='republisher',
        executable='republisher_server',
        name='nodo1',
    )

    republisher_client = Node(
        package='republisher',
        executable='republisher_client',
        name='nodo2',
        parameters=[{'text': text}]
    )

    return LaunchDescription([
        text_arg,
        republisher_server,
        republisher_client,
    ])
