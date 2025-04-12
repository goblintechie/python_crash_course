# 使用while循环提醒用户输入任意多的信息
# 每次提示输入被调查者的名字和回答
# 将数据存储在字典中

responses = {}

# 设置一个标志，代表调查是否继续
polling_active = True

while polling_active:
    # 提示输入名字和回答
    name = input("\nWhat is your name?")
    response = input("Which mountain would you like to climb someday?")

    # 将回答存储在字典中
    responses[name] = response

    # 询问调查是否继续
    repeat = input("Would you like to let another person respond?(yes/no)")
    if repeat == "no":
        polling_active = False

# 调查结束，显示结果
print("\n---Poll Results---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")