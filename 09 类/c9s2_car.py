"""9.2 使用类和实例"""

class Car:
    """一次模拟汽车的尝试"""

    def __init__(self,make,model,year):
        """初始化汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        # 给属性指定默认值
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述信息"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """给属性指定默认值"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self,mileage):
        """
        将里程表读数设置为指定的值
        禁止将里程表读数回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self,miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading += miles

my_new_car = Car('audi','a4',2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# 用三种方法修改属性的值
# 1.直接通过实例修改 my_new_car.odometer_reading = 23
# 2.通过方法修改  def update_odometer(self,mileage)
# 3.通过方法进行递增

my_new_car.odometer_reading = 23
my_new_car.read_odometer()
my_new_car.update_odometer(26)
my_new_car.read_odometer()
