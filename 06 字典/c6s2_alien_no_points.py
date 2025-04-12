# 使用方括号中的键获取值，如果键不存在，就会出问题
alien_0 = {'color':'green','speed':'slow'}
# print(alien_0['points'])

# 上述代码会报错KeyError: 'points'
# 可使用get()方法在指定键不存在时返回一个默认值
point_value = alien_0.get('points','No point value assigned.')
print(point_value)
