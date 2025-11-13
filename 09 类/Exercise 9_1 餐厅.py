"""
练习9-1：餐馆
创建一个名为Restaurant的类，为其方法__init__()设置属性restaurant_name和cuisine_type。
创建一个名为describe_restaurant()的方法和一个名为open_restaurant()的方法，
前者打印前述两项信息，而后者打印一条消息，指出餐馆正在营业。
根据这个类创建一个名为restaurant的实例，分别打印其两个属性，再调用前述两个方法。
"""

class Restaurant:
    """创建一个餐厅的类"""

    def __init__(self,restaurant_name,cuisine_type):
        """初始化属性"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        """定义描述餐厅的方法"""
        print("This is a Chinese restaurant.")
    
    def open_restaurant(self):
        """定义餐厅的营业时间"""
        print("We are open from 4 p.m. to 11 p.m.")

restaurant = Restaurant('Sat.BBQ','chinese bbq')
restaurant.describe_restaurant()
restaurant.open_restaurant()
