# 以不同的方式完成练习7-4或练习7-5，在程序中采取如下做法。
# 在while循环中使用条件测试来结束循环。
# 使用变量active来控制循环结束的时机。
# 使用break语句在用户输入'quit'时退出循环。

prompt = "Please enter pizza toppings. Type 'quit' to exit."

# 方法1
while True:
    topping = input(prompt)
    print(f"We will add {topping} to the pizza.")
    if topping == 'quit':
        break

# 方法2
active = True
while active:
    topping = input(prompt)
    if topping == 'quit':
        active = False
    else:
        print(f"We will add {topping} to the pizza.")

# 方法3
while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    else:
        print(f"We will add {topping} to the pizza.")