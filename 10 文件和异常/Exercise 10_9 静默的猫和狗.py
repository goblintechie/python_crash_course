"""
练习10-9：静默的猫和狗
修改你在练习10-8中编写的except代码块，让程序在任意文件不存在时静默失败。
"""
import os

filename = "cats1.txt"
# 获取脚本所在目录
script_dir = os.path.dirname(os.path.abspath(__file__))
# 构建文件完整路径
file_path = os.path.join(script_dir, filename)

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        contents = file.read()
    print(contents)
except FileNotFoundError:
    pass
