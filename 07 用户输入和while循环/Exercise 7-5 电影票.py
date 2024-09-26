# 有家电影院根据观众的年龄收取不同的票价：
# 不到3岁的观众免费；
# 3～12岁的观众收费10美元；
# 超过12岁的观众收费15美元。
# 请编写一个循环，在其中询问用户的年龄，并指出其票价。

active = True
while active:
    age = input("Tell me your age, enter 99 to exit.")
    if int(age) < 3:
        print("It's free for you.")
    elif int(age) >=3 and int(age) < 12:
        print("The ticket is 10 dollars.")
    elif int(age) > 12 and int(age) != 99:
        print("The ticket is 15 dollars.")
    elif int(age) == 99:
        break
