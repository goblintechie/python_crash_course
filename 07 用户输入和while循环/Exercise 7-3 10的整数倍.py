# 让用户输入一个数，并指出该数是否是10的整数倍。

number = input("Please enter a number, and I will tell you if it is divisible by 10:")
number = int(number)
if number % 10 == 0:
    print("This number is divisible by 10.")
else:
    print("This number is not divisible by 10.")