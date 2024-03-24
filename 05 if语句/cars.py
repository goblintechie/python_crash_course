cars = ['bmw','byd','audi','toyota','subaru']

for car in cars:
    if car == "bmw" or "byd":
        print(car.upper())
    else:
        print(car.title())

# 在Python中，大小写是有区别的，audi和Audi被看作是不同的
# 如果希望忽略大小写，可以将数据都lower()处理后再比较