"""
11.1.1 单元测试和测试用例
单元测试用于核实函数的某个方面没有问题。
测试用例是一组单元测试，它们核实函数在各种情况下都符合要求。
良好的测试用例考虑了函数可能收到的各种输入。
全覆盖的测试用例包含一整套单元测试，涵盖了各种可能的函数使用方式。
"""
# 可能需要花一点时间来适应创建测试用例的语法
# 但创建测试用例之后，再添加针对函数的测试单元就简单了
# 要为函数创建测试用例可以先导入模块unittest和要测试的函数
# 再创建一个继承unittest.TestCase的类
# 编写一系列方法对函数的各个方面进行测试

# 以下测试用例只有一个方法，检查get_full_name()在给定姓和名时能否正确工作

# 首先导入模块和要测试的函数
import unittest
from c11s1_name_function import get_full_name

# 创建一个NamesTestCase的类
# 用于包含一系列针对get_full_name()的单元测试
class NamesTestCase(unittest.TestCase):
    """测试test_name_function.py"""
    # 这个类只包含一个方法，只核实姓和名能够被正确格式化
    # 运行这个Python文件时，所有test开头的方法都会自动运行
    def test_first_last_name(self):
        """能够正确处理Bob Bao这样的名字吗"""
        # 使用实参bob、bao调用get_full_name()
        # 将结果赋给变量formatted_name
        formatted_name = get_full_name('bob','bao')
        # 使用了unittest的功能：断言方法
        # 该方法将核实得到的结果是否与期望的结果一致
        self.assertEqual(formatted_name,'Bob Bao')
        # 这段代码的意思是，将formatted_name的值与字符串'Bob Bao'比较，如果相等就OK

    """
    11.1.5 添加新测试
    确定get_full_name()能处理简单的姓名后，再写一个测试，用于测试包含中间名的姓名
    """
    def test_first_last_middle_name(self):
        """能够正确处理Wolfgang Amadeus Mozart这样的姓名吗"""
        formatted_name = get_full_name('wolfgang','mozart','amadeus')
        self.assertEqual(formatted_name,'Wolfgang Amadeus Mozart')

if __name__ == '__main__':
    unittest.main()

"""
普通程序中需要先定义一个类，实例化对象，用对象调用方法
但是在使用unittest框架时控制权被反转了
unittest.main()会检查当前模块中所有变量
会寻找任何继承自unittest.TestCase的类
后台会自动创建该类的实例
它会查找该类中所有以test_开头的方法，按顺序依次执行它们
test_开头是必须的，否则将不会自动执行
这种“我不调用框架，框架调用我”的概念就是控制反转（IoC）
只要按照它的命名规则（类继承TestCase，方法以test_开头）即可
"""
