#!/usr/bin/env python3

import rclpy 
from rclpy.node import Node 
from std_msgs.msg import Float32MultiArray
from sensor_msgs.msg import JointState



class publisher(Node):

  
    def __init__(self):
        
        super().__init__("publisher_node")

        self.cmd_pub = self.create_publisher(JointState,"/joint_states", 10)
        self.create_timer(0.5, self.send_velocity_command)
        self.get_logger().info("Publishing command")

    def send_velocity_command(self):
        self.angle=JointState()
        self.angle.name=['left_wheel','right_wheel']
        self.angle.velocity=[0.0, 0.0]
        self.angle.position=[0.0, 0.0]
        self.angle.effort=[0.00, 0.0]
        self.cmd_pub.publish(self.angle)
        # self.get_logger().info(str(self.angle))

def main(args=None):
    rclpy.init(args=args)
    node = publisher()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=='__main__':
    main()