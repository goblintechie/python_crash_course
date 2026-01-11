"""
练习10-11：喜欢的数
编写一个程序，提示用户输入喜欢的数，并使用json.dump()将这个数存储到文件中。
再编写一个程序，从文件中读取这个值，并打印如下所示的消息。
I know your favorite number!It's _____.
"""
import json
import os

filename = 'favorite_number.json'
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, filename)

def store_number():
    """存储最喜欢的数字"""
    # 提示输入最喜欢的数字
    favorite_number = input("请输入你最喜欢的数字：")
    # 将数字存入json文件
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(favorite_number,f)
    except FileNotFoundError:
        return None
    else:
        print(f"Log ===> Your favorite number is {favorite_number}.")

def get_number():
    """获取最喜欢的数字"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            favorite_number = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return favorite_number

store_number()
print(f"My favorite number is {get_number()}")
