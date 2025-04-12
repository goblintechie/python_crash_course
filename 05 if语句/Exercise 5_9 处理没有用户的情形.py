# 处理没有用户的情形　在为完成练习5-8编写的程序中，添加一条if语句，检查用户名列表是否为空。
# 如果为空，就打印如下消息。
# We need to find some users!
# 删除列表中的所有用户名，确定将打印正确的消息。

# users = ["Emily", "Jack", "Sophia", "Liam", "Isabella", "admin"]
users = [ ]

if users:
    for user in users:
        if user == "admin":
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {user.title()}, thank you for logging in again.")
else:
    print("We need to find some users!")
