# 有时候并不知道函数需要多少参数
# python允许函数从调用语句中收集任意数量的实参

# 制作披萨，事先不知道接受多少配料
# 只有一个形参：*toppings，不管调用语句提供多少实参，这个形参都会接受

# def make_pizza(*toppings):
#     """打印顾客所有配料"""
#     print(toppings)

# make_pizza('pepperoni')
# make_pizza('mushrooms','green peppers','extra cheese')

# 形参*topping的星号是让python创建了一个空元组，将接受的所有值放进这个元组
# def make_pizza(*toppings):
#     """概述要制作的比萨。"""
#     print("\nMaking a pizza with the following toppings:")
#     for topping in toppings:
#         print(f"- {topping}")

# make_pizza('pepperoni')
# make_pizza('mushrooms','green peppers','extra cheese')

# 8.5.1 结合使用位置实参和任意数量实参
# 如果让函数接受不同类型的实参
# 可以接受任意数量实参的形参要放在最后

def make_pizza(size,*toppings):
    """概述要制作的披萨"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')

# python将收到的第一个赋值给形参size，将其他所有值存储在元组toppings中
