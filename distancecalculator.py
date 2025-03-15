import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from std_msgs.msg import Float32
import math

class DistanceCalculator(Node):
    def __init__(self):
        super().__init__('distance_calculator')
        self.subscription = self.create_subscription(
            Pose, 
            '/turtle1/pose', 
            self.pose_callback, 
            10)
        self.publisher = self.create_publisher(Float32, '/turtle1/distance_from_origin', 10)

    def pose_callback(self, msg):
        distance = math.sqrt(msg.x**2 + msg.y**2)
        self.get_logger().info(f'Distance from origin: {distance:.2f}')
        self.publisher.publish(Float32(data=distance))

def main(args=None):
    rclpy.init(args=args)
    node = DistanceCalculator()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
