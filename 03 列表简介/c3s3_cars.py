cars = ['bmw','byd','audi','toyota','subaru']
# 按照字母顺序排序，永久修改排序
cars.sort()
print(cars)
# >>> ['audi', 'bmw', 'byd', 'subaru', 'toyota']

cars = ['bmw','byd','audi','toyota','subaru']
# 按照字母倒序排列，永久修改排序
cars.sort(reverse=True)
print(cars)
# >>> ['toyota', 'subaru', 'byd', 'bmw', 'audi']

cars = ['bmw','byd','audi','toyota','subaru']
# sorted()临时排序
print("Here is the original list:")
print(cars)
# >>> Here is the original list:
# ['bmw', 'byd', 'audi', 'toyota', 'subaru']
print("\nHere is the sorted list:")
print(sorted(cars))
# >>> Here is the sorted list:
# ['audi', 'bmw', 'byd', 'subaru', 'toyota']

print("\nHere is the original list:")
print(cars)
# >>> Here is the original list:
# ['bmw', 'byd', 'audi', 'toyota', 'subaru']

# 反序（不是按照字母倒序，而是将列表元素的原顺序翻转）
cars = ['bmw','byd','audi','toyota','subaru']
print(cars)
cars.reverse()
print(cars)
# >>> ['bmw', 'byd', 'audi', 'toyota', 'subaru']
# >>> ['subaru', 'toyota', 'audi', 'byd', 'bmw']

print(len(cars))
