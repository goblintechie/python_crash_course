"""
11.1 测试函数
通过测试确定代码面对各种输入都能按照要求工作
本章将学习使用Python的unittest模块来测试代码
学习编写测试用例，核实输入都将得到预期的输出
将学习到测试通过是什么样，测试不通过是什么样
还将学习如何测试函数和类，知道为项目编写多少个测试
"""
def get_full_name(first_name, last_name, middle_name=''):
    """返回完整的姓名"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()
