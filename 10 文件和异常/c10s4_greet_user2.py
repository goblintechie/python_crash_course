"""
10.4.3 重构greet_user.py，将获取用户名的代码转移到另一个函数中
"""
import os
import json

filename = 'username.json'
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, filename)

def get_stored_username():
    """如果用户存储了username，就获取它"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def greet_user():
    """问候用户，指出其姓名"""
    username = get_stored_username()
    if username:
        print(f"[01] Welcome back, {username}!")
    else:
        username = input("请输入你的姓名：")
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(username,f)
            print(f"[02] We'll remember you when you come back, {username}!")

greet_user()
