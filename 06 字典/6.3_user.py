# 遍历所有键值对

user_0 = {
    'username':'efermi',
    'first':'enrico',
    'last':'fermi',
}

for key,value in user_0.items():
    print(f"\nKey:{key}")
    print(f"\nValue:{value}")

# 遍历所有键

favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}

# for name in favorite_languages.keys():
#     print(name.title())

friends = ['phil','sarah']
# for name in favorite_languages.keys():
#     print(f"Hi {name.title()}")
#     if name in friends:
#         language = favorite_languages[name].title()
#         print(f"\t{name.title()}, I see you love {language}!")

for name,language in favorite_languages.items():
    if name in friends:
        print(f"Hi, {name.title()}")
        print(f"\t{name.title()}, I see you love {language.title()}")


# 按特定顺序遍历字典中的所有键

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

# 遍历所有的值
for language in favorite_languages.values():
    print(language.title())
# 这种方法提取所有的值，但是没有考虑是否重复
# 为了剔除重复项，可以使用集合set，每个元素都是独有的

for language in set(favorite_languages.values()):
    print(language.title())
# 集合不会以特定顺序存储元素
