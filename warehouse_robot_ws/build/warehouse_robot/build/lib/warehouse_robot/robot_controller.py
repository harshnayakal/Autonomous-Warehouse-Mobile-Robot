#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class RobotController(Node):

    def __init__(self):
        super().__init__('robot_controller')

        self.publisher = self.create_publisher(
            Twist,
            '/cmd_vel',
            10
        )

        self.timer = self.create_timer(
            0.1,
            self.timer_callback
        )

        self.get_logger().info("Robot Controller Started")

    def timer_callback(self):

        cmd = Twist()

        # Move forward
        cmd.linear.x = 0.20

        # No turning
        cmd.angular.z = 0.0

        self.publisher.publish(cmd)


def main(args=None):

    rclpy.init(args=args)

    node = RobotController()

    try:
        rclpy.spin(node)

    except KeyboardInterrupt:
        pass

    stop = Twist()
    node.publisher.publish(stop)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
