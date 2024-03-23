cars = ['bmw','byd','audi','toyota','subaru']
# 按照字母顺序排序，永久修改排序
cars.sort()
print(cars)

cars = ['bmw','byd','audi','toyota','subaru']
# 按照字母倒序排列，永久修改排序
cars.sort(reverse=True)
print(cars)

cars = ['bmw','byd','audi','toyota','subaru']
# sorted()临时排序
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list:")
print(cars)

# 倒序（不是按照字母倒序，而是将列表元素的原顺序翻转）
cars = ['bmw','byd','audi','toyota','subaru']
print(cars)
cars.reverse()
print(cars)

print(len(cars))