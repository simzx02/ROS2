#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/msg/string.hpp"

using namespace std::placeholders;
     
class SmartphoneNode : public rclcpp::Node // MODIFY NAME
{
public:
    SmartphoneNode() : Node("smartphone") // MODIFY NAME
    {
        subscriber_ = this->create_subscription<example_interfaces::msg::String>(
            "robot_news", 10, std::bind(&SmartphoneNode::callbackRobotNews, this, std::placeholders::_1));
        RCLCPP_INFO(this->get_logger(), "Smartphone Node has been started"); // MODIFY NAME
    }
     
private:
void callbackRobotNews(const example_interfaces::msg::String::SharedPtr msg)
    {
        RCLCPP_INFO(this->get_logger(), "Robot News: '%s'", msg->data.c_str());
    }
     
    rclcpp::Subscription<example_interfaces::msg::String>::SharedPtr subscriber_ = 
        this->create_subscription<example_interfaces::msg::String>(
            "robot_news", 10, std::bind(&SmartphoneNode::callbackRobotNews, this, _1));

};
     
int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<SmartphoneNode>(); // MODIFY NAME
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}