# 编写一个程序，询问用户有多少人用餐。
# 如果超过8位，就打印一条消息，指出没有空桌；否则指出有空桌。

number = input("How many people will be dining?")
number = int(number)
if number > 8:
    print("Sorry, there are no available tables.")
else:
    print("There are still available tables.")
    