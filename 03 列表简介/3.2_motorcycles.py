motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# 添加元素
# append()给列表附加元素时，它将添加到列表末尾
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# 使用方法insert()可在列表的任何位置添加新元素。
# 需要指定新元素的索引和值。
motorcycles.insert(0,'ducati')
print(motorcycles)

motorcycles = ['honda','yamaha','suzuki']
motorcycles.insert(1,'ducati')
print(motorcycles)

# 删除元素
# 如果知道要删除的元素在列表中的位置，可使用del语句
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)

# 有时候要将元素从列表中删除，并接着使用它的值
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# 方法pop()删除列表末尾的元素，并让你能够接着使用它。
# 术语弹出(pop)源自这样的类比：
# 列表就像一个栈，而删除列表末尾的元素相当于弹出栈顶元素。
motorcycles = ['honda','yamaha','suzuki']
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

# 实际上，可以使用pop()来删除列表中任意位置的元素，
# 只需在圆括号中指定要删除元素的索引即可。
motorcycles = ['honda','yamaha','suzuki']
first_owned = motorcycles.pop(0)
print(f"The last motorcycle I owned was a {first_owned.title()}.")

# 有时候，你不知道要从列表中删除的值所处的位置。
# 如果只知道要删除的元素的值，可使用方法remove()。
motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(f"\nA {too_expensive.title()} is too expensive for me.")
