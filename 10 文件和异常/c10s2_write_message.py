import os

# 详细的诊断信息
print("=== 诊断信息 ===")
print("当前工作目录:", os.getcwd())
print("脚本文件路径:", __file__)
print("脚本所在目录:", os.path.dirname(os.path.abspath(__file__)))
print("脚本绝对路径:", os.path.abspath(__file__))

# 检查文件是否真的存在
script_dir = os.path.dirname(os.path.abspath(__file__))
print("脚本目录是否存在:", os.path.exists(script_dir))

filename = os.path.join(script_dir, 'programming.txt')
print("目标文件路径:", filename)

# 10.2 写入文件
# 10.2.1 写入空文件
# open提供两个实参，一个是要打开的文件的名称
# 一个是用写入模式打开
# 如果写入的文件不存在，open会创建它
# 注意，写入模式会清空之前的内容
with open(filename, 'w') as file_object:
    # 将字符串写入文件中
    file_object.write("I Love Programming.\n")
    # Python只能写入字符串，如果要写入数字，需要先用str()转为字符串
    # 10.2.2 写入多行
    file_object.write("I love creating new games.\n")

# 10.2.3 附加模式
# 如果不清空文件，在文件内容后接着写入，要使用附加模式
with open(filename,'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")

print("文件已创建")
