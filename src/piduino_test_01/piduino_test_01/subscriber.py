import rclpy  # Import the ROS 2 Python client library
from rclpy.node import Node  # Import the Node class
from std_msgs.msg import String  # Change message type as needed

class SubscriberNode(Node):
    def __init__(self):
        super().__init__('piduino_sub_test01')  # Name of the node
        self.subscription = self.create_subscription(
            String, 'piduino_topic_test01', self.listener_callback, 10)
        self.subscription  # Prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info(f'Received: {msg.data}')  # Log received message

def main(args=None):
    rclpy.init(args=args)  # Initialize ROS 2
    node = SubscriberNode()
    rclpy.spin(node)  # Keep node running
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

