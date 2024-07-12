# 序数表示位置，如1st和2nd。
# 序数大多以th结尾，只有1、2和3例外。
# 在一个列表中存储数字1～9。遍历这个列表。
# 在循环中使用一个if-elif-else结构，以打印每个数字对应的序数。
# 输出内容应为"1st 2nd 3rd 4th 5th 6th 7th 8th 9th"，但每个序数都独占一行。

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
for number in numbers:
    if number == '1':
        print('1st')
    elif number == '2':
        print('2nd')
    elif number == '3':
        print('3rd')
    else:
        print(number + 'th')
