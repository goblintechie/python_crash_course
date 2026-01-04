"""
10.4.3 重构
重构让代码更清晰，更易于理解，更容易拓展
"""
import os
import json

def greet_user():
    """问候用户，并指出用户的名字"""
    filename = "username.json"
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, filename)
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            username = json.load(f)
    except FileNotFoundError:
        username = input("请输入你的姓名：")
        print(f"We'll remember you when you come back, {username}!")
    else:
        print(f"Welcome back, {username}!")

greet_user()
