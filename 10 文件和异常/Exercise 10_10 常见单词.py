"""
练习10-10：常见单词
访问古登堡计划，找一些你想分析的图书。
下载这些作品的文本文件或将浏览器中的原始文本复制到文本文件中。
可以使用方法count()来确定特定的单词或短语在字符串中出现了多少次。
请注意，通过使用lower()将字符串转换为小写，可捕捉要查找单词的所有格式，而不管其大小写如何。
编写一个程序，它读取你在古登堡计划中获取的文件，并计算单词'the'在每个文件中分别出现了多少次。
这里计算得到的结果并不准确，因为将诸如'then'和'there'等单词也计算在内了。
请尝试计算'the '（包含空格）出现的次数，看看结果相差多少。
"""

import os

filename = "The Complete Works of William Shakespeare.txt"

# 获取脚本所在目录
script_dir = os.path.dirname(os.path.abspath(__file__))
# 构建文件完整路径
file_path = os.path.join(script_dir, filename)

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        contents = file.read()
except FileNotFoundError:
    print("文件不存在！")
else:
    print(f"the出现的次数是：{contents.lower().count('the')}")
    print(f"去重后（there,then,they等），the出现的次数是：{contents.lower().count('the ')}")
