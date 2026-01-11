"""
10.4.2 程序运行时从文件username.json中获取姓名
先写一个获取姓名的try代码块
如果文件不存在就提示用户输入姓名
将用户输入的姓名存储到文件中
并告诉用户下次程序启动时会记住他
"""
import os
import json

filename = "username.json"
# 获取脚本所在目录
script_dir = os.path.dirname(os.path.abspath(__file__))
# 构建文件完整路径
file_path = os.path.join(script_dir, filename)

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("请输入你的姓名：")
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(username, f)
        print(f"We'll remember you when you come back, {username}!")
else:
    print(f"Welcome back, {username}!")
