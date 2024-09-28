# 创建一个名为sandwich_orders的列表
# 其中包含各种三明治的名字
# 再创建一个名为finished_sandwiches的空列表
# 遍历sandwich_orders，对每种三明治打印一条消息
# I made your tuna sandwich
# 将其移动到finished_sandwiches中，所有的三明治制作好
# 打印一条消息，将这些三明治列出来

sandwich_orders = ['Panini','Egg Salad Sandwich','French Dip Sandwich']
finished_sandwiches = []
for sandwich in sandwich_orders:
    print(f"I made your {sandwich}.")
    finished_sandwiches.append(sandwich)
print(finished_sandwiches)