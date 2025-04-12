# 使用range()生成一系列数字
# 函数range()让Python从指定的第一个值开始数，并在到达你指定的第二个值时停止。
# 因为它在第二个值处停止，所以输出不包含该值（这里为5）。
for value in range(1,5):
    print(value)

numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)
