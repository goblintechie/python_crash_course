squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares)

digits = list(range(1,11))
print(min(digits))
print(max(digits))
print(sum(digits))

# 列表解析将for循环和创建新元素的代码合并成一行，并自动附加新元素
squares = [value ** 2 for value in range(1,11)]
print(squares)
