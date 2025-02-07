import rclpy  # Import the ROS 2 Python client library
from rclpy.node import Node  # Import the Node class
from std_msgs.msg import String  # Change message type as needed

class PublisherNode(Node):
    def __init__(self):
        super().__init__('piduino_pub_test01')  # Name of the node
        self.publisher_ = self.create_publisher(String, 'piduino_topic_test01', 10)  # Topic name & queue size
        self.timer = self.create_timer(1.0, self.publish_message)  # Timer to call function periodically

    def publish_message(self):
        msg = String()
        msg.data = 'piduino placeholder message'  # Replace with actual data
        self.publisher_.publish(msg)
        self.get_logger().info(f'Published: {msg.data}')  # Log message

def main(args=None):
    rclpy.init(args=args)  # Initialize ROS 2
    node = PublisherNode()
    rclpy.spin(node)  # Keep node running
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

