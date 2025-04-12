# Python中用方括号([])表示列表，并用逗号分隔其中的元素

bicycles = ['trek','cannondale','redline','specialized']
print(bicycles)

# 列表是有序集合，因此要访问列表的任意元素，只需将该元素的位置（索引）告诉Python即可
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[1])
print(bicycles[3])
print(bicycles[-1])

message = f"My first bicycle was a {bicycles[0].title()}."
print(message)
