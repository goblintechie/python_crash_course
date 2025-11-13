"""
练习9-9:电瓶升级 在本节最后一个electric_car.py版本中,给Battery类添加一个名为upgrade_battery()的方法。
该方法检查电瓶容量,如果不是100,就将其设置为100。
创建一辆电瓶容量为默认值的电动汽车,调用方法get_range(),然后对电瓶进行升级,并再次调用get_range()。
你将看到这辆汽车的续航里程增加了。
"""

class Car:
    """一次模拟汽车的简单尝试"""

    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """定义"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """读取里程"""
        print(f"This car has {self.odometer_reading} miles on ")

    def update_odometer(self,mileage):
        """更新里程，修改属性的值"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self,miles):
        """里程增加"""
        self.odometer_reading += miles

    def fill_gas_tank(self):
        """用来给子类改写的方法"""
        print("This car has a big gas tank.")

class Battery:
    """
    有时属性和方法越来越多，我们可以将类的一部分提取出来，作为一个独立的类
    定义一个Battery类,没有继承Car
    有一个形参battery_size
    """
    def __init__(self,battery_size=75):
        """初始化电池属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印描述电池的消息"""
        print(f"This car has a {self.battery_size}-KWh battery.")

    def upgrade_battery(self):
        """升级电瓶的方法"""
        if self.battery_size != 100:
            self.battery_size = 100

class ElectricCar(Car):
    """电动车的独特之处"""
    def __init__(self, make, model, year):
        """
        初始化父类的属性
        再初始化电动汽车特有的属性
        """
        super().__init__(make, model, year)
        # self.battery_size = 75
        # 这个属性让Python创建一个Battery的实例，将这个实例赋值给属性self.battery
        self.battery = Battery()

    def fill_gas_tank(self):
        """
        重写父类的方法
        电动汽车没有油箱
        """
        print("This car doesn't need a gas tank!")

my_byd = ElectricCar("BYD","han",2025)
my_byd.battery.describe_battery()
my_byd.battery.upgrade_battery()
my_byd.battery.describe_battery()
