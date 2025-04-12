# 人生的不同阶段　设置变量age的值，再编写一个if-elif-else结构，
# 根据age的值判断一个人处于人生的哪个阶段。
# 如果年龄小于2岁，就打印一条消息，指出这个人是婴儿。
# 如果年龄为2（含）～4岁，就打印一条消息，指出这个人是幼儿。
# 如果年龄为4（含）～13岁，就打印一条消息，指出这个人是儿童。
# 如果年龄为13（含）～20岁，就打印一条消息，指出这个人是青少年。
# 如果年龄为20（含）～65岁，就打印一条消息，指出这个人是成年人。
# 如果年龄超过65岁（含），就打印一条消息，指出这个人是老年人。

age = 33
if age < 2:
    print("This is a baby.")
elif 2 <= age < 4:
    print("This is a toddler.")
elif 4 <= age < 13:
    print("This is a child.")
elif 13 <= age < 20:
    print("This is a teenager.")
elif 20 <= age < 65:
    print("This is an adult.")
else:
    print("This is an elderly person.")
