"""
11.1 测试函数
函数get_full_name会返回一个整洁的全名，姓和名之间有空格，且首字母大写输出
为了核实它确实正确工作，我们写一个测试函数来验证
"""
from c11s1_name_function import get_full_name

print("Enter 'q' to quit at anytime.")
while True:
    first = input("\nPlease give me a first name:")
    if first == 'q':
        break
    last = input("Please give me a last name:")
    if last == 'q':
        break
    formatted_name = get_full_name(first,last)
    print(f"\tNeatly formatted name: {formatted_name}")
