"""
练习10-7：加法计算器
将为完成练习10-6而编写的代码放在一个while循环中，让用户犯错（输入的是文本而不是数）后能够继续输入数。
"""
print("输入两个数字，我将进行加法运算")
print("Enter 'q' to quit")
while True:
    first_number = input("\nFirst number:")
    if first_number == 'q':
        break
    second_number = input("Second number:")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("请输入阿拉伯数字。")
    else:
        print(answer)
