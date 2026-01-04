"""
练习10-6：加法运算
提示用户提供数值输入时，常出现的一个问题是，用户提供的是文本而不是数。
在此情况下，当你尝试将输入转换为整数时，将引发ValueError异常。
编写一个程序，提示用户输入两个数，再将其相加并打印结果。
在用户输入的任何一个值不是数时都捕获ValueError异常，并打印一条友好的错误消息。
对你编写的程序进行测试：先输入两个数，再输入一些文本而不是数。
"""
print("输入两个数字，我将进行加法运算")
print("Enter 'q' to quit")
first_number = input("\nFirst number:")
second_number = input("Second number:")
try:
    answer = int(first_number) + int(second_number)
except ValueError:
    print("请输入阿拉伯数字。")
else:
    print(answer)
