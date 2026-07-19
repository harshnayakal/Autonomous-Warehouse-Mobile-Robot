from setuptools import find_packages, setup

package_name = "warehouse_robot"

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
    (
        'share/ament_index/resource_index/packages',
        ['resource/warehouse_robot'],
    ),
    (
        'share/warehouse_robot',
        ['package.xml'],
    ),
    (
        'share/warehouse_robot/launch',
        [
            'launch/warehouse.launch.py',
            'launch/warehouse_robot.launch.py',
        ],
    ),
    (
        'share/warehouse_robot/worlds',
        ['worlds/warehouse.world'],
    ),
],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='vboxuser',
    maintainer_email='vboxuser@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
    'console_scripts': [
        'robot_controller = warehouse_robot.robot_controller:main',
    ],
},
)
