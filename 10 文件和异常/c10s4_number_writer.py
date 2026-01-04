"""
10.4 存储数据
程序将用户提供的信息存储在列表和字典等数据结构中
一种简单的方式是使用模块json来存储数据

JSON(JavaScript Object Notation)格式最初是为JavaScript开发的，
但随后成了一种常见格式，被包括Python在内的众多语言采用。
"""

# 10.4.1　使用json.dump()和json.load()
# 编写一个存储一组数的程序，再编写一个将这些数读取到内存的程序

# json.dump()接受两个实参，要存储的数据，用于存储数据的文件对象
import json
import os

# 指定目标文件
filename = 'numbers.json'

# 获取脚本所在目录
script_dir = os.path.dirname(os.path.abspath(__file__))

# 构建文件完整路径
file_path = os.path.join(script_dir, filename)

numbers = [1,2,3,5,7,9,11]

# 以写入模式打开这个文件filename
with open(file_path, 'w', encoding='utf-8') as f:
    # 使用函数json.dump()将数字列表存储到JSON文件中
    json.dump(numbers,f)
