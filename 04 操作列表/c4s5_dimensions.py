# 元组
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

# 严格地说，元组是由逗号标识的，圆括号只是让元组看起来更整洁、更清晰。
# 如果你要定义只包含一个元素的元组，必须在这个元素后面加上逗号
my_t = (1,)

# 虽然不能修改元组的元素，但可以给存储元组的变量赋值。
dimensions = (200,50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400,100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
