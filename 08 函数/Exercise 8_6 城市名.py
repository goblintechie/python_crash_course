# 编写一个名为city_country()的函数，接受城市名及所属国家
# 这个函数应该返回如下字符串
# Santiago,Chile

def city_country(city, country):
    """返回城市名及其所属国家名"""
    print(f"{city},{country}")

print("\nplease enter a name of a city:")
city_name = input("The name of the city:").title()
print("\nPlease enter the cuntry of the city:")
country_name = input("The cuntry of the city:").title()

city_country(city_name,country_name)
