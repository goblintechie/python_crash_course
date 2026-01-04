# 10.3.5 处理FileNotFoundError异常

import os

# 获取脚本所在目录
script_dir = os.path.dirname(os.path.abspath(__file__))
# 构建文件完整路径
file_path = os.path.join(script_dir, 'alice_in_wonderland.txt')

try:
    with open(file_path,encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {file_path} does not exist.")
# 10.3.6 分析文本
# split以空格为分隔符将字符串拆开存进列表
else:
    # 计算文件包含多少个单词
    words = contents.split()
    num_words = len(words)
    print(f"The file {file_path} has about {num_words} words.")
