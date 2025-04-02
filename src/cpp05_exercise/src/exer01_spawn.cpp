#include "rclcpp/rclcpp.hpp"
#include "turtlesim/srv/spawn.hpp"

using namespace std::chrono_literals;
class Exer01Spawn : public rclcpp::Node {
public:
    Exer01Spawn(): Node("exer01_spawn_node_cpp") // Initialize the node with a name
    {
        // Constructor implementation
        RCLCPP_INFO(this->get_logger(), "exer01_spawn_node_cpp has been initialized.");
        this->declare_parameter("x",3.0);
        this->declare_parameter("y",3.0);
        this->declare_parameter("theta",0.0);
        this->declare_parameter("turtle_name","turtle2");
        x = this->get_parameter("x").as_double();
        y = this->get_parameter("y").as_double();
        theta = this->get_parameter("theta").as_double();
        turtle_name = this->get_parameter("turtle_name").as_string();
        spawn_client_ = this->create_client<turtlesim::srv::Spawn>("/spawn");
    }
    bool connect_server() {
        while(!spawn_client_->wait_for_service(1s)) {
            if (!rclcpp::ok()) {
                RCLCPP_INFO(rclcpp::get_logger("rclcpp"),"force quit!!");
                return false;
            }
            RCLCPP_INFO(this->get_logger(),"connecting....");
        }
        return true;
    }
    rclcpp::Client<turtlesim::srv::Spawn>::FutureAndRequestId request() {
        auto req = std::make_shared<turtlesim::srv::Spawn::Request>();
        req->x = x;
        req->y = y;
        req->theta = theta;
        req->name = turtle_name;
        return spawn_client_->async_send_request(req);
    }
private:
    double x,y,theta;
    std::string turtle_name;
    rclcpp::Client<turtlesim::srv::Spawn>::SharedPtr spawn_client_;
};

int main(int argc, char *argv[]) {
    // Initialize ROS 2
    rclcpp::init(argc, argv);
    auto client_ = std::make_shared<Exer01Spawn>();
    bool flag = client_->connect_server();
    if (!flag) {
        RCLCPP_INFO(rclcpp::get_logger("rclcpp"),"service connect fail");
        return 1;
    }
    auto response = client_->request();
    if (rclcpp::spin_until_future_complete(client_,response) == rclcpp::FutureReturnCode::SUCCESS) {
        std::string name = response.get()->name;
        if (name.empty()) {
            RCLCPP_ERROR(client_->get_logger(),"already exists same name turtle");
        }else {
            RCLCPP_INFO(client_->get_logger(),"response success");
        }
    }else {
        RCLCPP_INFO(client_->get_logger(),"response fail");
    }

    // Shutdown ROS 2
    rclcpp::shutdown();
    return 0;
}
