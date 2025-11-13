"""
练习9-4：就餐人数　
在为完成练习9-1而编写的程序中，添加一个名为number_served的属性，并将其默认值设置为0。
根据这个类创建一个名为restaurant的实例。
打印有多少人在这家餐馆就餐过，然后修改这个值并再次打印它。

添加一个名为set_number_served()的方法，让你能够设置就餐人数。
调用这个方法并向它传递一个值，然后再次打印这个值。

添加一个名为increment_number_served()的方法，让你能够将就餐人数递增。
调用这个方法并向它传递一个这样的值：你认为这家餐馆每天可能接待的就餐人数。
"""

class Restaurant:
    """创建一个餐厅的类"""

    def __init__(self,restaurant_name,cuisine_type):
        """初始化属性"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 20

    def describe_restaurant(self):
        """定义描述餐厅的方法"""
        print("This is a Chinese restaurant.")

    def open_restaurant(self):
        """定义餐厅的营业时间"""
        print("We are open from 4 p.m. to 11 p.m.")

    def set_number_served(self,number):
        """设置就餐人数"""
        self.number_served = number

    def increment_number_served(self,number):
        """就餐人数增加"""
        self.number_served += number

restaurant = Restaurant('Sat.BBQ','chinese bbq')
print(f"There are {restaurant.number_served} people dining here.")
