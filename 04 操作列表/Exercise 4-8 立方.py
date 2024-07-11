# 立方 将同一个数乘三次为立方，创建1-10的立方，打印

cube = []
for number in range(1,11):
    cube.append(number**3)
print(cube)

cube = [number**3 for number in range(1,11)]
print(cube)