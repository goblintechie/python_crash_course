# 在字典中存储列表
# 有时需要将列表存在字典，而不是将字典存在列表

pizza = {
    'crust':'thick',
    'toppings':['mushrooms','extra cheese'],
    }

print(f"You ordered a {pizza['crust']}-crust pizza."
      "With the following toppings:")
for topping in pizza['toppings']:
    print(topping)
