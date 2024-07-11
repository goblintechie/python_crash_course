# 放眼世界 想出至少5个想去旅游的地方
# 将这些地方存在一个列表，确保元素不是按字母顺序排列
# 按照原始排列顺序打印列表
# 使用sorted()按字母顺序打印，不要修改它
# 再次打印，核实排列顺序未变
# 使用sorted()按语字母顺序相反顺序打印，不要修改它
# 再次打印，核实列表顺序未变
# 使用reverse()修改列表元素排列顺序，打印列表，核实列表顺序确实改变
# 使用reverse()修改列表顺序，打印，核实已回复到原来顺序
# 使用sort()修改顺序，打印核实
# 使用sort()修改顺序，按相反顺序排列，打印核实

cities = ['beijing', 'nanjing', 'guangzhou', 'hangzhou', 'suzhou']

print('使用sorted()按照字母顺序打印列表')
print(sorted(cities))
print('\n再次打印原列表，核实排列顺序未变')
print(cities)

print('\n使用sorted()按与字母相反的顺序打印列表')
print(sorted(cities,reverse=True))
print('\n再次打印原列表，核实排列顺序未变')
print(cities)

print('\n使用reverse()修改列表，打印核实列表顺序改变')
cities.reverse()
print(cities)

print('\n再次使用reverse()修改列表，核实已恢复到原来顺序')
cities.reverse()
print(cities)

print('\n使用sort()修改列表，打印核实列表顺序改变')
cities.sort()
print(cities)

print('\n使用sort()修改列表，按照字母相反顺序排列，打印核实列表顺序改变')
cities.sort(reverse=True)
print(cities)
