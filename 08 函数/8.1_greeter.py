# 8.1 定义函数

def greet_user():
    """现实简单的问候语"""
    print("hello")

greet_user()

def greet_user(username):
    """显示简单的问候语"""
    print(f"Hello, {username}")

greet_user('jesse')