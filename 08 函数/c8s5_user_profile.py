# 有时需要接受任意数量的实参，但不知道传递给函数的会是什么信息
# 将函数编写成能够接受任意数量的键值对，调用语句提供多少就接受多少
# 比如创建按用户简介，知道会收到用户信息，但是不知道收到什么信息

def build_profile(first,last,**user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert','enstein',location='princeton',field='physics')
print(user_profile)

# 函数build_profile()定义要求提供名和姓，同时允许根据需要提供任意数量的名称值对
# **user_info让python创建一个空字典，将收到的所有键值对放到这个字典中
# 将名和姓加入字典user_info，因为总是能从用户那收到姓名