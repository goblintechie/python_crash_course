# 8.4 传递列表
# 向函数传递列表，其中可能是名字、数字或更复杂的对象（字典）

def greet_users(names):
    """向列表中的每位用户发出简单的问候"""
    for name in names:
        msg = f"Hello, {name.title()}"
        print(msg)

usernames = ['hannah','ty','margot']
greet_users(usernames)
