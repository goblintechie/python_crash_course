# 添加嘉宾 你找到更大的桌子，想想还要邀请哪三位
# 以3-4为基础，末尾添加你找到更大桌子
# 使用insert()将嘉宾添加到开头
# 使用insert()将嘉宾添加到中间
# 使用appedn()将嘉宾添加到末尾
# 打印消息

dinner_guests = ['zhang san','li si','wang wu']

print(f"Mr {dinner_guests[0].title()}, Would you do me the honor of joining me for dinner this evening?")
print(f"Mr {dinner_guests[1].title()}, Would you do me the honor of joining me for dinner this evening?")
print(f"Mr {dinner_guests[2].title()}, Would you do me the honor of joining me for dinner this evening?")

print("I have found a larger table for dinner.")
dinner_guests.insert(0,'Anti-Mage')
dinner_guests.insert(2,'lina')
dinner_guests.append('luna')

for name in dinner_guests:
    print(f"{name.title()}, Would you do me the honor of joining me for dinner this evening?")
