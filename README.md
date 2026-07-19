# Autonomous Warehouse Mobile Robot using ROS2 Humble

An autonomous warehouse mobile robot developed using **ROS2 Humble**, **Gazebo**, **RViz2**, **Nav2**, and **SLAM Toolbox**. The project demonstrates autonomous navigation, LiDAR-based mapping, obstacle avoidance, path planning, and warehouse simulation.

---

## Project Overview

This project simulates an autonomous mobile robot operating inside a warehouse environment. The robot is capable of creating maps using LiDAR, localizing itself, planning optimal paths, avoiding obstacles, and navigating to target locations autonomously.

The project follows a modular ROS2 architecture and demonstrates core concepts used in modern warehouse automation systems.

---

## Features

- Autonomous warehouse navigation
- LiDAR-based obstacle detection
- Simultaneous Localization and Mapping (SLAM)
- Autonomous path planning using Nav2
- Gazebo warehouse simulation
- RViz2 visualization
- Waypoint navigation
- ROS2 Python nodes
- Modular package structure
- Easy to extend and customize

---

## Technologies Used

- ROS2 Humble
- Python 3
- Gazebo
- RViz2
- Nav2
- SLAM Toolbox
- TurtleBot3
- Ubuntu 22.04
- Git & GitHub

---

## Project Structure

```
Autonomous-Warehouse-Mobile-Robot-ROS2
│
├── warehouse_robot
│   ├── robot_controller.py
│   ├── obstacle_avoidance.py
│   ├── navigation.py
│   ├── goal_sender.py
│   ├── warehouse_manager.py
│   └── battery_manager.py
│
├── launch
├── config
├── maps
├── models
├── meshes
├── rviz
├── urdf
├── worlds
├── screenshots
│
├── package.xml
├── setup.py
├── setup.cfg
├── README.md
└── LICENSE
```

---

## System Workflow

```
Warehouse Environment
        │
        ▼
Gazebo Simulation
        │
        ▼
LiDAR Sensor
        │
        ▼
SLAM Toolbox
        │
        ▼
Map Generation
        │
        ▼
Localization
        │
        ▼
Nav2 Path Planning
        │
        ▼
Obstacle Avoidance
        │
        ▼
Autonomous Navigation
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/Autonomous-Warehouse-Mobile-Robot-ROS2.git
```

Navigate to the workspace

```bash
cd Autonomous-Warehouse-Mobile-Robot-ROS2
```

Build the workspace

```bash
colcon build
```

Source the workspace

```bash
source install/setup.bash
```

---

## Running the Project

Launch Gazebo

```bash
export TURTLEBOT3_MODEL=burger

ros2 launch warehouse_robot warehouse.launch.py
```

Run the robot controller

```bash
ros2 run warehouse_robot robot_controller
```

Launch autonomous navigation

```bash
ros2 launch warehouse_robot navigation.launch.py
```

---

## Results

- Autonomous navigation inside a warehouse environment
- LiDAR-based obstacle detection
- Real-time map generation
- Path planning using Nav2
- Robot visualization using RViz2
- Warehouse simulation using Gazebo

---

## Future Improvements

- Multi-robot fleet management
- Pick and place automation
- QR code based inventory management
- AI-based object detection
- Dynamic obstacle avoidance
- Battery monitoring system
- Warehouse task scheduling
- Cloud-based fleet monitoring

---

## Screenshots

### Gazebo Simulation

_Add your Gazebo simulation screenshot here._

### RViz2 Visualization

_Add your RViz2 screenshot here._

### Warehouse Navigation

_Add navigation screenshots here._

---

## Contributors

This project was collaboratively developed by:

- **Harshvardhan Nayakal**
- **Sakshi Patil**

Special thanks to the **Department of Mechatronics Engineering, Rajarambapu Institute of Technology**, for providing the learning environment and support throughout the development of this project.

---

## License

This project is released under the MIT License.

---

## Contact

**Harshvardhan Nayakal**

GitHub: https://github.com/harshnayakal

LinkedIn: *(Add your LinkedIn profile here)*

---

### ⭐ If you found this project helpful, consider giving it a Star on GitHub.
