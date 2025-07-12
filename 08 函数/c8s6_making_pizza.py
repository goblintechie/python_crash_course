"""
引用模块，制作披萨
"""

import pizza

pizza.make_pizza(16,'pepperoni')
pizza.make_pizza(12,'mushrooms','green peppers','extra cheese')

# 还可以使用from module_name import function_name的方式导入模块中指定函数
# 如果要导入多个指定函数，将函数列出来，用逗号分隔
# 如果导入的函数名称与现有的名称冲突，可以使用as来重命名
# from pizza import make_pizza as mp
# 也可以给模块重命名
# 如果要导入所有的函数 from pizza import *
