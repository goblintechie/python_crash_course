"""
继续重构greet_user.py，将提升用户输入姓名的代码放入独立的函数中
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

def get_new_username():
    """提示用户输入用户名："""
    username = input("请输入你的姓名：")
    with open(file_path, 'w', encoding='uft-8') as f:
        json.dump(username,f)
    return username

def greet_user():
    """问候用户，指出其姓名"""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")
greet_user()
