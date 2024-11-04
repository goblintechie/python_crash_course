# 函数定义中可能包含多个形参
# 向函数中传递实参的方式有很多
# 可以用位置实参，实参的顺序与形参相同
# 可以用关键字实参，每个实参由变量名和值组成
# 还可以用列表和字典

# 位置实参

def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster','harry')
describe_pet('dog','willie')

# 关键字实参

def describe_pet(animal_type,pet_name):
    """显示宠物的信息"""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type='hamster', pet_name='harry')

# 默认值
# 在调用函数时，给形参提供了实参时，Python使用指定实参值，否则使用形参默认值

def describe_pet(pet_name,animal_type='dog'):
    """显示宠物的信息"""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='harry')

# 修改了形参位置，因为animal_type指定了默认值，在调用函数的时候
# 只会包含宠物名字的实参，Python依然将这个实参视为位置实参，如果animal_type放在前面
# 那么实参就会与第一个形参关联，因此pet_name放在前面
# 如果调用函数时指定了宠物种类，那么就会忽略默认值

# 等效调用
def describe_pet(pet_name,animal_type='dog'):
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('willie')
describe_pet(pet_name='willie')
describe_pet('harry','hamster')
describe_pet(pet_name='harry',animal_type='hamster')
describe_pet(animal_type='hamster',pet_name='harry')