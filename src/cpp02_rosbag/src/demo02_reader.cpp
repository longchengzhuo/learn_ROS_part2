#include "rclcpp/rclcpp.hpp"
#include "rosbag2_cpp/reader.hpp"
#include "geometry_msgs/msg/twist.hpp"

class SimpleBagPlay : public rclcpp::Node {
public:
    SimpleBagPlay(): Node("simple_bag_play_node_cpp") // Initialize the node with a name
    {
        // Constructor implementation
        RCLCPP_INFO(this->get_logger(), "SimpleBagPlay has been initialized.");
        reader_ = std::make_unique<rosbag2_cpp::Reader>();
        reader_->open("my_bag");
        while (reader_->has_next()) {
            auto twist = reader_->read_next<geometry_msgs::msg::Twist>();
            RCLCPP_INFO(this->get_logger(), "linear velocity:%.2f",twist.linear.x);

        }
        reader_->close();
    }

private:
    std::unique_ptr<rosbag2_cpp::Reader> reader_;
};

int main(int argc, char *argv[]) {
    // Initialize ROS 2
    rclcpp::init(argc, argv);

    // Create and spin the node
    auto node = std::make_shared<SimpleBagPlay>();
    rclcpp::spin(node);

    // Shutdown ROS 2
    rclcpp::shutdown();
    return 0;
}
