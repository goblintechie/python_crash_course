"""
随着不断给类添加功能,文件会变得很长,我们应该让文件保持简洁
Python允许将类存储在模块中,在主程序中导入模块即可.
我们已经在文件夹中创建了一个car.py,我们需要将它导入到本文件
"""
from car import Car,ElectricCar

my_new_car = Car('BYD','han L',2025)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

my_byd = ElectricCar('yangwang','U7',2025)
print(my_byd.get_descriptive_name())
my_byd.battery.describe_battery()
my_byd.battery.get_range()
