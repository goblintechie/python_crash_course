# 切片 选择一个程序，末尾添加代码，完成以下任务：
# 打印消息“The first three items in the list are:”，使用切片打印列表前三元素
# 打印消息“Three items from the middle of the list are:”，使用切片打印中间三个元素
# 打印消息“The last three items in the list are:”，再使用切片来打印列表的末尾三个元素

cube = [number**3 for number in range(1,11)]
print(cube)
# [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

print('The first three items in the list are:')
print(cube[0:3])

print('Three items from the middle of the list are:')
print(cube[4:7])

print('The last three items in the list are:')
print(cube[-3:])
