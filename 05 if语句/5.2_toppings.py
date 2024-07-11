# 判断不相等，使用!=
requested_topping = "mushrooms"
if requested_topping != "anchovies":
    # anchovy：凤尾鱼
    print("Hold the anchovies.")

requested_toppings = ['mushrooms','extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")

# 如果只想执行一个代码块，就使用if-elif-else结构；
# 如果要执行多个代码块，就使用一系列独立的if语句。

requested_toppings = ['mushrooms','green peppers','extra cheese']
for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")
print("Finished making your pizza.")

requested_toppings = ['mushrooms','green peppers','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")
print("Finished making your pizza.")

requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

# 在if语句中将列表名用作条件表达式时，Python将在列表至少包含一个元素时返回True，并在列表为空时返回False。
# 简言之，if加列表，空就是false，非空就是true
    
available_toppings = ['mushrooms','olives','green peppers',
                      'pepperoni','pineapple','extra cheese']
requested_toppings = ['mushrooms','french fries','extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print("\nFinished making your pizza!")
