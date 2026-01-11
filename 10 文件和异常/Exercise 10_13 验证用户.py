"""
练习10-13：验证用户
最后一个remember_me.py版本假设用户要么已输入用户名，要么是首次运行该程序。
我们应该修改这个程序，以防当前用户并非上次运行该程序的用户。
为此，在greet_user()中打印欢迎用户回来的消息前，询问他用户名是否正确。
如果不对，就调用get_new_username()让用户输入正确的用户名。
"""
import os
import json

filename = 'username.json'
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, filename)

def get_stored_username():
    """
    如果用户存储了username，就获取它
    处理文件为空、文件不存在、文件异常情况
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            # 先读取文件内容，判断是否为空
            content = f.read().strip()
            if not content:
                print(f"The file {filename} is empty.")
                return None
            # 如果文件不为空，则解析文件
            username = json.load(f)
            return username
    except FileNotFoundError:
        # 如果文件不存在，返回None
        print(f"The file {file_path} does not exsist.")
        return None
    except json.JSONDecodeError:
        # 如果文件内容不是有效的JSON格式，返回None
        print(f"The file {filename} contains invalid JSON.")
        return None
    except Exception as e:
        # 处理其他错误
        print(f"An error occurred: {e}")
        return None

def get_new_username():
    """提示用户输入用户名："""
    username = input("请输入你的姓名：")
    with open(file_path, 'w', encoding='utf-8') as f:
        # 将用户名存储到文件中
        json.dump(username,f)
    return username

def greet_user():
    """问候用户，指出其姓名"""
    username = get_stored_username()
    if username:
        # 如果找到了用户名，就问候用户
        answer = input("Is " + username + " your username? (y/n): ")
        if answer.lower() == 'y':
            print(f"Welcome back, {username}!")
        else:
            username = get_new_username()
            print(f"We'll remember you when you come back, {username}!")
    else:
        # 如果用户名不存在，就提示用户输入用户名
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")
greet_user()
