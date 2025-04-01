#include "rclcpp/rclcpp.hpp"
#include "geometry_msgs/msg/twist.hpp"
#include "rosbag2_cpp/writer.hpp"

class SimpleBagRecorder : public rclcpp::Node {
public:
    SimpleBagRecorder(): Node("simple_bag_recorder_node_cpp") // Initialize the node with a name
    {
        // Constructor implementation
        RCLCPP_INFO(this->get_logger(), "SimpleBagRecorder has been initialized.");
        writer_ = std::make_unique<rosbag2_cpp::Writer>();
        writer_->open("my_bag");
        sub_ = this->create_subscription<geometry_msgs::msg::Twist>("turtle1/cmd_vel",10,std::bind(&SimpleBagRecorder::do_write_msg,this,std::placeholders::_1));
    }

private:
    void do_write_msg(std::shared_ptr<rclcpp::SerializedMessage> msg) {
        writer_->write(msg,"turtle1/cmd_vel","geometry_msgs/msg/Twist",this->now());
    }
    std::unique_ptr<rosbag2_cpp::Writer> writer_;
    rclcpp::Subscription<geometry_msgs::msg::Twist>::SharedPtr sub_;
};

int main(int argc, char *argv[]) {
    // Initialize ROS 2
    rclcpp::init(argc, argv);

    // Create and spin the node
    auto node = std::make_shared<SimpleBagRecorder>();
    rclcpp::spin(node);

    // Shutdown ROS 2
    rclcpp::shutdown();
    return 0;
}
