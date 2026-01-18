"""
练习11-3：雇员

测试Employee类
"""

import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """测试Employee类"""
    def setUp(self):
        self.employee = Employee('Bob','Bao',30000)
        self.amount = 10000
    
    def test_give_default_raise(self):
        """测试默认涨薪"""
        salary = self.employee.give_raise()
        self.assertEqual(35000,self.employee.salary)
    
    def test_give_custom_raise(self):
        """测试自定义涨薪"""
        salary = self.employee.give_raise(10000)
        self.assertEqual(40000,self.employee.salary)

if __name__ == '__main__':
    unittest.main()
