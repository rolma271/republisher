from setuptools import setup

package_name = 'republisher'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    py_modules=[],
    data_files=[
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/republisher.launch.py']),
        ('share/' + package_name + '/action', ['action/Republish.action']),     
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='marco',
    maintainer_email='rolma271@gmail.com',
    description='Republisher action example',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'republisher_server = republisher.republisher_server:main',
            'republisher_client = republisher.republisher_client:main',
        ],
    },
)
