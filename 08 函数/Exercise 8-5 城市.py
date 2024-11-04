# 编写一个describe_city()的函数，接受一座城市名字以及城市所属的国家
# 打印句子：Reykjavik is in Iceland.
# 给用语存储国家的形参指定默认值，为三个不同城市调用这个函数，之少有一个城市不属于默认国家

def describe_city(city,country='china'):
    print(f"{city.title()} is in {country.title()}")

describe_city('hangzhou')
describe_city('shenzhen')
describe_city('tokyo','japan')