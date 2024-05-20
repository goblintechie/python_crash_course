alien_0 = {'color':'green','points':5}
print(alien_0['color'])
print(alien_0['points'])
new_points = alien_0['points']
print(f"You just earned {new_points} points!")

# 字典是一种动态结构，可随时在其中添加键值对。
# 要添加键值对，可依次指定字典名、用方括号括起的键和相关联的值。

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_0 = {'x_position':0,'y_position':25,'speed':'medium'}
print(f"Original x-position:{alien_0['x_position']}")
# 向右移动外星人
# 根据当前速度确定外星人移动多少
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position:{alien_0['x_position']}")

del alien_0['x_position']
print(alien_0)