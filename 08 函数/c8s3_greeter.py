# 结合使用函数get_formatted_name()和while循环，以更正式方式问候用户

def get_formatted_name(first_name,last_name):
    """返回整洁的姓名"""
    full_name = f"{first_name} {last_name}"
    return full_name

# 这是一个循环
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name:")
    if f_name =='q':
        break
    l_name = input("last name:")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello,{formatted_name}")
