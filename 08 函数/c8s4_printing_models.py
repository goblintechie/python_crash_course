# 8.4.1 在函数中修改列表
# 讲列表传给函数后，函数可以对其进行修改
# 在函数中对列表做的修改是永久的

# 创建一个列表，包含要打印的设计
unprinted_designs = ['phone case','robot pandant','dodecahedron']
completed_models = []

# 模拟打印每个设计，直到没有未打印的设计为止
# 打印每个设计后，将其移到列表completed_models中
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model:{current_design}")
    completed_models.append(current_design)

# 显示打印的所有模型
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

# 使用while循环每次从列表末尾移除一个元素
# 将这个元素打印出来
# 并将这个元素添加到新列表中
# 最后循环打印新列表

# 现在编写两个函数，第一个函数负责打印，第二个负责描述打印了哪些
def print_models(unprinted_designs,completed_models):
    """
    模拟打印每个设计，直到没有未打印的设计为止
    打印每个设计后，将其移动到列表completed_models中
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model:{current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """显示打印好的所有模型"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case','robot pandant','dodecahedron']
completed_models = []
print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)

# 如果不想修改原来的列表
# 我们在调用函数的时候可以向函数传递列表的副本
# print_models(unprinted_designs[:],completed_models)