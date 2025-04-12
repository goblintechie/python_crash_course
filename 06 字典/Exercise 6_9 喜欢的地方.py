# 创建一个名为favorite_places的字典。
# 在这个字典中，将三个人的名字用作键，并存储每个人喜欢的1～3个地方。
# 为了让这个练习更有趣些，可以让一些朋友说出他们喜欢的几个地方。
# 遍历这个字典，并将其中每个人的名字及其喜欢的地方打印出来。

# names = ["Emily", "Jack", "Sophia", "Liam", "Isabella"]

favorite_places = {
    'Emily':['New York','Tokyo','Paris'],
    'Jack':['Sydney','Mumbai','London'],
    'Sophia':['Beijing','Rio de Janeiro','Cape Town'],
}

for name,cities in favorite_places.items():
    print(f"\n{name}'s favorite places are:")
    for city in cities:
        print(f"\t{city}")
