"""
练习10-12：记住喜欢的数
将练习10-11中的程序合二为一。
如果存储了用户喜欢的数，就向用户显示它，否则提示用户输入喜欢的数并将其存储到文件中。
运行这个程序两次，看看它能否像预期的那样工作。
"""
import json
import os

filename = 'favorite_number.json'
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, filename)

def remember_your_favorite_number():
    """10-11的函数合二为一"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            favorite_number = json.load(f)
    except FileNotFoundError:
        print("The file doesn't exist.")
    if favorite_number:
        return favorite_number
    else:
        favorite_number = input("Please input your favorite number:")
        with open(file_path, 'w', encoding='uft-8') as f:
            json.dump(favorite_number,f)
        return favorite_number

print(f"Your favorite number is {remember_your_favorite_number()}.")
