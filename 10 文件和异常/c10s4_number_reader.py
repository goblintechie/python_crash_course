"""

"""
import json
import os

# 指定目标文件
filename = 'numbers.json'

# 获取脚本所在目录
script_dir = os.path.dirname(os.path.abspath(__file__))

# 构建文件完整路径
file_path = os.path.join(script_dir, filename)

with open(file_path,'r',encoding='utf-8') as f:
    # 使用json.load记载存储在numbers.json中的信息并赋值给numbers
    numbers = json.load(f)
print(numbers)
