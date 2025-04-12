# 如果想尝试做更多比较，可再编写一些测试，并将它们加入conditional_tests.py中。
# 对于下面列出的各种情况，至少编写两个结果分别为True和False的测试。
# 检查两个字符串相等和不等。
# 使用方法lower()的测试。
# 涉及相等、不等、大于、小于、大于等于和小于等于的数值测试。
# 使用关键字and和or的测试。
# 测试特定的值是否包含在列表中。
# 测试特定的值是否未包含在列表中。

print("检查两个字符串相等和不等：")

message = 'I love hangzhou city.'
print("Is message == 'I love hangzhou city'?")
print(message == 'I love hangzhou city.')

print("\nIs message == 'I love guangzhou city'?")
print(message == 'I love guangzhou city.')

print("\n使用方法lower()的测试：")
city = 'Hangzhou'
print(city.lower() == 'hangzhou')

print("\n涉及相等、不等、大于、小于、大于等于和小于等于的数值测试：")
number = 20
print(30 > number)
print(19 < number)
print(20 >= number)
print(21 <= number)

print("\n使用关键字and和or的测试：")
status_1 = "on"
status_2 = "off"
print(status_1 == "off" or status_2 == "off")
print(status_1 == "on" and status_2 == "on")

print("\n测试特定的值是否包含在列表中：")
users = ['zhangsan', 'lisi', 'wangwu']
print('zhangsan' in users)

print("\n测试特定的值是否包含在列表中：")
print('zhaosi' not in users)
