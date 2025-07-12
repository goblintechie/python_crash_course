# 练习8-14：汽车　编写一个函数，将一辆汽车的信息存储在字典中。
# 这个函数总是接受制造商和型号，还接受任意数量的关键字实参。
# 这样调用该函数：提供必不可少的信息，以及两个名称值对，如颜色和选装配件。
# 这个函数必须能够像下面这样进行调用：
# car = make_car('subaru','outback',color='blue',tow_package=True)
# 打印返回的字典，确认正确地处理了所有的信息。

def make_car(brand,type,**car_info):
    """汽车的信息"""
    car_info['brand'] = brand
    car_info['type'] = type
    return car_info

car_info = make_car('byd','han',color='black',power='electric')
print(car_info)
