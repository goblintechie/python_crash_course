# 我们曾用remove()删除列表中的特定值
# 这样做是可行的，因为要删除的值只出现一次
# 如果要删除的值多次出现怎么办？

pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)