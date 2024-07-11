players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

# 如果要提取列表的第二、第三和第四个元素，可将起始索引指定为1，并将终止索引指定为4：
print(players[1:4])

# 如果没有指定第一个索引，Python将自动从列表开头开始
print(players[:4])

# 要让切片终止于列表末尾，也可使用类似的语法
print(players[2:])

# 负数索引返回离列表末尾相应距离的元素，
# 因此你可以输出列表末尾的任意切片
print(players[-3:])

# 如果要遍历列表的部分元素，可在for循环中使用切片。
# 下面的示例遍历前三名队员，并打印他们的名字：
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
