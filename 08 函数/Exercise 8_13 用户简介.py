# 练习8-13：用户简介　复制前面的程序user_profile.py，
# 在其中调用build_profile()来创建有关你的简介。
# 调用这个函数时，指定你的名和姓，以及三个描述你的键值对。

def build_profile(first,last,**user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('bob','bao',location='sz',age=18,job='pm')
print(user_profile)
