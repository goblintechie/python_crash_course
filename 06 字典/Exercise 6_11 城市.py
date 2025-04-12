# 创建一个名为cities的字典，将三个城市名用作键。
# 对于每座城市，都创建一个字典，并在其中包含该城市所属的国家、人口约数以及一个有关该城市的事实。
# 在表示每座城市的字典中，应包含country、population和fact等键。
# 将每座城市的名字以及有关信息都打印出来。

# 创建字典，存储城市及其相关信息
cities = {
    "New York": {
        "country": "USA",
        "population": "8.4 million",
        "fact": "Known as the Big Apple."
    },
    "Tokyo": {
        "country": "Japan",
        "population": "14 million",
        "fact": "Largest metropolitan area in the world."
    },
    "Paris": {
        "country": "France",
        "population": "2.1 million",
        "fact": "Known as the City of Light."
    }
}

# 打印每座城市的名字以及有关信息
for city, info in cities.items():
    print(f"City: {city}")
    print(f"Country: {info['country']}")
    print(f"Population: {info['population']}")
    print(f"Fact: {info['fact']}\n")
