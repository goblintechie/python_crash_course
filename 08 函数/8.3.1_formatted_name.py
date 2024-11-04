# 返回值

def get_formatted_name(first_name,last_name):
    """返回整洁的姓名"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi','hendrix')
print(musician)

# 该函数的定义通过形参接受名和姓
# 将姓名结合，将结果赋给full_name，将full_name转为首字母大写
# 并将结果返回到函数调用行
# 调用返回值的函数时，需要提供一个变量，以便将返回的值赋给它
# 例中将返回值赋给了musician

# 让实参变为可选
# 实参变为可选，使用函数时在必要时提供额外信息

def get_formatted_name(first_name,middle_name,last_name):
    full_name=f"{first_name} {middle_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('john','lee','hooker')
print(musician)

# 并非所有人有中间名，如果只提供了名和姓就无法正常工作
# 为了让中间名可选，可给middle_name指定一个空的默认值，并将其移动到形参末尾
# 在用户没有提供中间名的时候不使用这个形参

def get_formatted_name(first_name,last_name,middle_name=''):
    if middle_name:
        full_name=f"{first_name} {middle_name} {last_name}"
    else:
        full_name=f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi','hendrix')
print(musician)

musician = get_formatted_name('john','lee','hooker')
print(musician)