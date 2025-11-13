# 10.1 从文件中读取数据
# 10.1.1 读取整个文件

# 定义文件的位置，此处采用了绝对路径
file_path = 'E:/Code/python_crash_course/10 文件和异常/pi_digits.txt'
# 下面的程序会读取路径的文件并将其内容显示在屏幕
with open(file_path) as file_object:
    # 要使用文件，首先要打卡它，open接收一个参数：要打开的文件的名称
    # open返回一个表示文件的对象，Python将这个对象赋给file_object
    # with会在不再需要文件后将其关闭，这样做比手动调用close要好
    # 方法read()读取文件的内容，将结果作为一个长字符串赋值给contents
    contents = file_object.read()
print(contents.rstrip())

# 10.1.2 文件路径
# 将文件名传递给open时,Python将在当前执行的.py文件所在目录中查找

# 以每次一行的方式检查文件，对文件对象使用for循环
with open(file_path) as file_object:
    for line in file_object:
        print("逐行检查：")
        print(line.rstrip())

# 使用关键字with时，open()返回的文件对象只在with代码块内可用
# 如果要在with代码块外访问文件的内容，可在with代码块内将文件的各行存储在一个列表中
with open(file_path) as file_object:
    # readlines从文件中读取每一行，并将其存储在一个列表中
    # 列表被赋值给lines，在列表之外还可以使用这个变量
    lines = file_object.readlines()

# 在with之外使用变灵lines
for line in lines:
    print(line.rstrip())
