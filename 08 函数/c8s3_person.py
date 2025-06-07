# 8.3.3 返回字典
# 函数可返回任何类型的值，包括列表和字典等复杂数据结构

def build_person(first_name,last_name):
    """返回一个字典，包含有关一个人的信息"""
    person = {'first':first_name,'last':last_name}
    return person

musician = build_person('jimi','hendrix')
print(musician)

def build_person2(first_name,last_name,age=None):
    """返回一个字典，包含有关一个人的信息"""
    person = {'first':first_name,'last':last_name}
    if age:
        person['age'] = age
    return person

musician = build_person2('jimi','hendrix',age=27)
print(musician)

musician = build_person2('li','wang')
print(musician)
