"""
10.4.2 紧接着remember_me.py，再写一个程序，向存储的用户发出问候
"""
import os
import json

filename = "username.json"

# 获取脚本所在目录
script_dir = os.path.dirname(os.path.abspath(__file__))
# 构建文件完整路径
file_path = os.path.join(script_dir, filename)

with open(file_path, 'r' ,encoding='utf-8') as file:
    username = json.load(file)
print(f"Welcome back, {username}!")
