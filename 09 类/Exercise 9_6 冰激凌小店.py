"""
练习9-6:冰激凌小店 冰激凌小店是一种特殊的餐馆。
编写一个名为IceCreamStand的类,让它继承为完成练习9-1或练习9-4而编写的Restaurant类。
这两个版本的Restaurant类都可以,挑选你更喜欢的那个即可。
添加一个名为flavors的属性,用于存储一个由各种口味的冰激凌组成的列表。
编写一个显示这些冰激凌的方法。创建一个IceCreamStand实例,并调用这个方法。
"""

class Restaurant:
    """创建一个餐厅的类"""

    def __init__(self,restaurant_name,cuisine_type):
        """初始化属性"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """定义描述餐厅的方法"""
        print(f"餐厅名称: {self.restaurant_name}")
        print(f"菜系类型: {self.cuisine_type}")

    def open_restaurant(self):
        """定义餐厅的营业时间"""
        print("We are open from 4 p.m. to 11 p.m.")

class IceCreamStand(Restaurant):
    """继承Restaurant"""
    def __init__(self, restaurant_name, cuisine_type = "冰激凌店"):
        """初始化父类的属性"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['香草', '巧克力', '草莓', '抹茶', '芒果']

    def show_flavor(self):
        """展示冰激凌的各种口味"""
        print("我们提供以下冰激凌的口味：")
        for flavor in self.flavors:
            print(f"- {flavor}")

my_icecream_shop = IceCreamStand("BOB的冰激凌店")
my_icecream_shop.describe_restaurant()
my_icecream_shop.show_flavor()
