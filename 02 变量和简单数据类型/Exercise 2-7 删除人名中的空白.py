# 剔除人名中的空白 变量表示人名，开头和末尾包含空白符，务必至少使用字符组合\t和\n各一次
# 打印这个人名，显示开头和末尾空白，然后分别使用lstrip()、rstrip()和strip()处理

name = "\tBob\n"
print(name)

print(name.lstrip())
print(name.rstrip())
print(name.strip())
