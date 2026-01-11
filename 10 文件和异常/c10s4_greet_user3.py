"""
10.4.3 继续重构greet_user.py，将提升用户输入姓名的代码放入独立的函数中
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
            # 加载文件中的用户名，将结果存储到username变量中
            username = json.load(f)
    except FileNotFoundError:
        # 如果文件不存在，返回None
        return None
    else:
        # 否则返回用户名
        return username

def get_new_username():
    """提示用户输入用户名："""
    username = input("请输入你的姓名：")
    with open(file_path, 'w', encoding='uft-8') as f:
        # 将用户名存储到文件中
        json.dump(username,f)
    return username

def greet_user():
    """问候用户，指出其姓名"""
    username = get_stored_username()
    if username:
        # 如果找到了用户名，就问候用户
        print(f"Welcome back, {username}!")
    else:
        # 如果用户名不存在，就提示用户输入用户名
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")
greet_user()
