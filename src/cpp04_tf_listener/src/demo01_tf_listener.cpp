#include "rclcpp/rclcpp.hpp"
#include "tf2_ros/buffer.h"
#include "tf2_ros/transform_listener.h"
using namespace std::chrono_literals;
class TFListener : public rclcpp::Node {
public:
    TFListener(): Node("tf_listener_node_cpp") // Initialize the node with a name
    {
        // Constructor implementation
        RCLCPP_INFO(this->get_logger(), "TFListener has been initialized.");
        buffer_ = std::make_unique<tf2_ros::Buffer>(this->get_clock());
        listener_ = std::make_shared<tf2_ros::TransformListener>(*buffer_,this);
        timer_ = this->create_wall_timer(1s,std::bind(&TFListener::on_timer, this));
    }

private:
    void on_timer() {
        try {
            auto ts = buffer_->lookupTransform("camera","laser",tf2::TimePointZero);
            RCLCPP_INFO(this->get_logger(),"---------transformed info---------");
            RCLCPP_INFO(this->get_logger(),"frame_id:%s,child_frame_id:%s,offset:(%.2f,%.2f,%.2f)",
                ts.header.frame_id.c_str(),ts.child_frame_id.c_str(),ts.transform.translation.x,ts.transform.translation.y,ts.transform.translation.z
                );


        } catch (const tf2::LookupException &e) {
            RCLCPP_INFO(this->get_logger(),"something wrong: %s",e.what());
        }
    }
    std::unique_ptr<tf2_ros::Buffer> buffer_;
    std::shared_ptr<tf2_ros::TransformListener> listener_;
    rclcpp::TimerBase::SharedPtr timer_;
};

int main(int argc, char *argv[]) {
    // Initialize ROS 2
    rclcpp::init(argc, argv);

    // Create and spin the node
    auto node = std::make_shared<TFListener>();
    rclcpp::spin(node);

    // Shutdown ROS 2
    rclcpp::shutdown();
    return 0;
}
