favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

alien_0 = {'color':'green','speed':'slow'}
# 通过指定键获取对应的值，如果键不存在就会报错
# 此时可使用get()方法，如果键不存在，就返回一个默认值
point_value = alien_0.get('point','No point value assigned.')
print(point_value)
