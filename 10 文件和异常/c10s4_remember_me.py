"""
10.4.2 保存和读取用户生成的数据
提示用户首次运行程序时输入自己的名字，在程序再次运行时记住他
"""
import os
import json

username = input("请输入你的姓名：")
filename = "username.json"

# 获取脚本所在目录
script_dir = os.path.dirname(os.path.abspath(__file__))
# 构建文件完整路径
file_path = os.path.join(script_dir, filename)

with open(file_path, 'w', encoding='utf-8') as file:
    # 将通过input接收的信息写入json文件
    json.dump(username,file)
    print(f"We'll remember you when you come back, {username}!")
