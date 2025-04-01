#include "rclcpp/rclcpp.hpp"
#include "tf2_ros/static_transform_broadcaster.h"
#include "geometry_msgs/msg/transform_stamped.hpp"
#include "tf2/LinearMath/Quaternion.h"
class TFStaticBroadcaster : public rclcpp::Node {
public:
    TFStaticBroadcaster(char * argv[]): Node("tf_static_broadcaster_node_cpp") // Initialize the node with a name
    {
        // Constructor implementation
        RCLCPP_INFO(this->get_logger(), "TFStaticBroadcaster has been initialized.");
        broadcaster_ = std::make_shared<tf2_ros::StaticTransformBroadcaster>(this);
        pub_static_tf(argv);
    }

private:
    std::shared_ptr<tf2_ros::StaticTransformBroadcaster> broadcaster_;
    void pub_static_tf(char * argv[]) {
        geometry_msgs::msg::TransformStamped transform;
        transform.header.stamp = this->now();
        transform.header.frame_id = argv[7];
        transform.child_frame_id = argv[8];
        transform.transform.translation.x = atof(argv[1]);
        transform.transform.translation.y = atof(argv[2]);
        transform.transform.translation.z = atof(argv[3]);

        tf2::Quaternion qtn;
        qtn.setRPY(atof(argv[4]),atof(argv[5]),atof(argv[6]));
        transform.transform.rotation.x = qtn.x();
        transform.transform.rotation.y = qtn.y();
        transform.transform.rotation.z = qtn.z();
        transform.transform.rotation.w = qtn.w();

        broadcaster_->sendTransform(transform);
    }
};

int main(int argc, char *argv[]) {
    if (argc != 9) {
        RCLCPP_ERROR(rclcpp::get_logger("rclcpp"),"parameter is invalid!");
    }
    // Initialize ROS 2
    rclcpp::init(argc, argv);

    // Create and spin the node
    auto node = std::make_shared<TFStaticBroadcaster>(argv);
    rclcpp::spin(node);

    // Shutdown ROS 2
    rclcpp::shutdown();
    return 0;
}
