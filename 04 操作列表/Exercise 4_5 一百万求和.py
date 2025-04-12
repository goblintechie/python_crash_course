# 一百万求和 创建一个包含1-1000000的列表，使用min()和max()核实确实从1开始，到1000000结束，对列表调用sum()，查看相加需要多久

one_million = list(range(1,1000001))
print(min(one_million))
print(max(one_million))
print(sum(one_million))
