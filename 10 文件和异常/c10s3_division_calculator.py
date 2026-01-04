# 10.3 异常
# 当发生错误时，Python会创建一个异常对象
# 如果定义了处理异常的代码，程序会继续；如果没有，就会显示traceback
# 使用try-except代码块处理异常
# 10.3.1 处理ZeroDivisionError异常
# print(5/0)

# Traceback (most recent call last):
#   File "e:\Code\python_crash_course\10 文件和异常\c10s3_division_calculator.py", line 6, in <module>
#     print(5/0)
#           ~^~
# ZeroDivisionError: division by zero

# ZeroDivisionError就是个异常对象，当Python无法按要求执行就会创建这种对象

# 10.3.2　使用try-except代码块
# 如果认为可能发生错误，可以写一个try-except代码块来处理错误
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
# 将导致错误的代码放在try中
# 如果try没有问题，Python将跳过except模块
# 如果try有问题，则Python查找对应的except并执行其中的代码


# 10.3.3 使用异常避免崩溃
# 发生错误时，如果程序还有未执行完的工作，那么妥善处理错误就很重要
# 以下是捕捉错误后程序继续运行的示例
# print("Give me two numbers and I'll divide them.")
# print("Enter 'q' to quit.")
# while True:
#     first_number = input("\nFirst number:")
#     if first_number == 'q':
#         break
#     second_number = input("Second number:")
#     if second_number == 'q':
#         break
#     answer = int(first_number) / int(second_number)
#     print(answer)

# 10.3.4 else代码块
# 依赖try代码成功执行的代码都应放到else代码块中
print("Give me two numbers and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number:")
    if first_number == 'q':
        break
    second_number = input("Second number:")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)
