"""
传递实参
"""
# 函数定义中可能包含多个形参，调用函数也可能包含多个实参
# 向函数中传递实参的方式有很多
# 可以用位置实参，这要求实参的顺序与形参相同
# 可以用关键字实参，其中每个实参都由变量名和值组成
# 还可以用列表和字典

# 8.2.1 位置实参
def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster','harry')
describe_pet('dog','willie')
# 使用位置实参时，实参的顺序非常重要

# 8.2.2 关键字实参
# 关键字实参是传递给函数的名称值对，在实参中将名称和值关联起来，所以传递实参时不会混淆
# 使用关键字实参无需考虑函数调用中的实参顺序，可以清楚知道函数调用中各个值的作用
def describe_pet_1(animal_type,pet_name):
    """显示宠物的信息"""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet_1(animal_type='hamster', pet_name='harry')

# 8.2.3 默认值
# 在调用函数时，给形参提供了实参时，Python使用指定实参值，否则使用形参默认值
def describe_pet_2(pet_name,animal_type='dog'):
    """显示宠物的信息"""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet_2(pet_name='harry')
# 在这个函数中，修改了形参的排列顺序
# 因为animal_type指定了默认值，无须通过实参来指定动物类型
# 所以在函数调用中只包含一个实参——宠物的名字
# 然而Python将这个实参依然视为位置实参，因此如果函数调用中只包含宠物名字
# 宠物名字的实参将关联到函数定义的第一个形参
# 因此需要将pet_name放在形参开头
# 也就是说，使用默认值时，在形参列表中先列出没有默认值的形参，再列出有默认值的实参

# 8.2.4 等效的函数调用
def describe_pet_3(pet_name,animal_type='dog'):
    """等效调用"""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# 一条名为willie的小狗
describe_pet_3('willie')
describe_pet_3(pet_name='willie')

# 一只名为Harry的仓鼠
describe_pet_3('harry','hamster')
describe_pet_3(pet_name='harry',animal_type='hamster')
describe_pet_3(animal_type='hamster',pet_name='harry')
