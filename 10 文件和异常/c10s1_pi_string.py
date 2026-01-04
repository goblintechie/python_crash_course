# 10.1.5 使用文件的内容
# 将文件读取到内存中后就可以使用这些数据了
file_path = 'E:/Code/python_crash_course/10 文件和异常/pi_digits.txt'

with open(file_path) as file_object:
    # 读取文件内容的每一行将其存储在列表中
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    # 每读取一行就添加到字符串中
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))
