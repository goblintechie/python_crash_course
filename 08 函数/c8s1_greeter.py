"""
展示简单的函数结构
"""

# 8.1 定义函数

def greet_user():
    """现实简单的问候语"""
    print("hello")

# 关键字def告诉Python要定义一个函数
# 这是函数定义，向Python指出了函数名
# 以及可能在圆括号里指出函数为完成任务需要什么信息
# def greet_user():后面的所有缩进行构成了函数体
# 三引号括起的是文档字符串（docstring），描述函数的作用
# print("hello")是代码行

greet_user()
# 依次指定函数名以及用圆括号括起的必要信息，即可调用函数

# 8.1.1 向函数传递信息

# 在函数定义def greet_user_1()的括号里添加username
# 可以让函数接受你给username指定的任何值
def greet_user_1(username):
    """显示简单的问候语"""
    print(f"Hello, {username.title()}!")

# 调用greet_user_1()，向它提供执行函数调用print()所需的信息
greet_user_1('jesse')

# 8.1.2 实参和形参
# 在函数greet_user()的定义中，变量username是一个形参（parameter），即函数完成工作所需的信息。在代码greet_user('jesse')中，'jesse'是一个实参（argument），即调用函数时传递给函数的信息。实参'jesse'传递给函数greet_user()，这个值被赋给了形参username
