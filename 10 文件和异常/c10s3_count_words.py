# 10.3.7 使用多个文件
import os
def count_words(filename):
    """计算一个文件包含多少个单词"""
    # 获取脚本所在目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # 构建文件完整路径
    file_path = os.path.join(script_dir, filename)
    try:
        with open(file_path,encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        # 10.3.8 静默失败
        # 在except代码中明确告诉Python出现错误时什么都不要做
        pass
        # 也许以后会在pass这里做些什么，比如将不存在的文件收集起来，现在pass就是占位符
        # print(f"Sorry, the file {filename} does not exist.")
    else:
        # 计算文件包含多少个单词
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

filename = 'alice_in_wonderland.txt'
count_words(filename)
filenames = ["alice_in_wonderland.txt","siddhartha.txt","moby_dick.txt","little_women.txt"]
for filename in filenames:
    count_words(filename)
