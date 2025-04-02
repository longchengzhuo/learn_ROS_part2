#include "rclcpp/rclcpp.hpp"
#include "geometry_msgs/msg/point_stamped.hpp"

using namespace std::chrono_literals;
class PointBroadcaster : public rclcpp::Node {
public:
    PointBroadcaster(): Node("point_broadcaster_node_cpp"),x(0.0) // Initialize the node with a name
    {
        // Constructor implementation
        RCLCPP_INFO(this->get_logger(), "point_broadcaster_node_cpp has been initialized.");
        point_pub_ = this->create_publisher<geometry_msgs::msg::PointStamped>("point",10);
        timer_ = this->create_wall_timer(1s,std::bind(&PointBroadcaster::on_timer,this));
    }

private:
    void on_timer() {
        geometry_msgs::msg::PointStamped ps;
        ps.header.stamp = this->now();
        ps.header.frame_id = "laser";
        x += 0.05;
        ps.point.x = x;
        ps.point.y = 0.0;
        ps.point.z = -0.1;

        point_pub_->publish(ps);
    }
    rclcpp::Publisher<geometry_msgs::msg::PointStamped>::SharedPtr point_pub_;
    rclcpp::TimerBase::SharedPtr timer_;
    double x;
};

int main(int argc, char *argv[]) {
    // Initialize ROS 2
    rclcpp::init(argc, argv);

    // Create and spin the node
    auto node = std::make_shared<PointBroadcaster>();
    rclcpp::spin(node);

    // Shutdown ROS 2
    rclcpp::shutdown();
    return 0;
}
