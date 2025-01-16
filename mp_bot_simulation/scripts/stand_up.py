#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from std_msgs.msg import Header

class JointTrajectoryPublisher(Node):
    def __init__(self):
        super().__init__('move_your_ass')
        self.publisher_ = self.create_publisher(JointTrajectory, '/joint_trajectory_controller/joint_trajectory', 10)
        
        self.timer = self.create_timer(1.0, self.publish_trajectory)

    def publish_trajectory(self):
        msg = JointTrajectory()
        
        # Header
        msg.header = Header()
        msg.header.stamp.sec = 0
        msg.header.stamp.nanosec = 0
        msg.header.frame_id = ''

        # Joint names
        msg.joint_names = [
            'fr_coxa_to_baselink',
            'fr_femur_to_coxa',
            'fr_tibia_to_femur',
            'fl_coxa_to_baselink',
            'fl_femur_to_coxa',
            'fl_tibia_to_femur',
            'rr_coxa_to_baselink',
            'rr_femur_to_coxa',
            'rr_tibia_to_femur',
            'rl_coxa_to_baselink',
            'rl_femur_to_coxa',
            'rl_tibia_to_femur'
        ]

        """ points = [
            {
                'positions': [1.069, 0.0, -2.70, 1.069, 0.0, -2.70, 1.069, 0.0, -2.70, 1.069, 0.0, -2.70],
                'time_from_start': (2, 0)  # (sec, nanosec)
            },
            {
                'positions': [1.069, -2.56, -2.70, 1.069, -2.56, -2.70, 1.069, -2.56, -2.70, 1.069, -2.56, -2.70],
                'time_from_start': (4, 0)  # (sec, nanosec)
            }
        ] """
        """ {
                'positions': [1.069, 0.0, -1.78, 1.069, 0.0, -1.78, 1.069, 0.0, -1.78, 1.069, 0.0, -1.78],
                'time_from_start': (2, 0)  # (sec, nanosec)
            }, """

        points = [
            
            {
                'positions': [1.069, -1.83, -1.78, 1.069, -1.83,-1.78, 1.069, -1.83, -1.78, 1.069, -1.83, -1.78],
                'time_from_start': (4, 0)  # (sec, nanosec)
            }
        ]

        # Points
        """ point = JointTrajectoryPoint()
        point.positions = [1.069, -2.56, -2.70, 1.069, -2.56, -2.70, 1.069, -2.56, -2.70, 1.069, -2.56, -2.70]
        point.time_from_start.sec = 2
        point.time_from_start.nanosec = 0

        msg.points.append(point) """
        for point_data in points:
            point = JointTrajectoryPoint()
            point.positions = point_data['positions']
            point.time_from_start.sec = point_data['time_from_start'][0]
            point.time_from_start.nanosec = point_data['time_from_start'][1]
            msg.points.append(point)

        # Publish the message
        self.publisher_.publish(msg)
        self.get_logger().info('Published JointTrajectory message')

def main(args=None):
    rclpy.init(args=args)
    joint_trajectory_publisher = JointTrajectoryPublisher()
    rclpy.spin(joint_trajectory_publisher)
    joint_trajectory_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
