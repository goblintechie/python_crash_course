# 修改嘉宾名单 有位嘉宾无法赴约，需要邀请另一位
# 以3-4为基础，在默认打印一句，指出是谁无法参加
# 修改名单，将无法赴约的改为新的嘉宾
# 再次打印消息

dinner_guests = ['zhang san','li si','wang wu']
print(f"Mr {dinner_guests[0].title()}, Would you do me the honor of joining me for dinner this evening?")
print(f"Mr {dinner_guests[1].title()}, Would you do me the honor of joining me for dinner this evening?")
print(f"Mr {dinner_guests[2].title()}, Would you do me the honor of joining me for dinner this evening?")

print(f"Mr {dinner_guests[0].title()} is unable to attend the dinner due to unforeseen circumstances.")

dinner_guests[0] = 'zhu de'
print(f"Mr {dinner_guests[0].title()}, Would you do me the honor of joining me for dinner this evening?")
print(f"Mr {dinner_guests[1].title()}, Would you do me the honor of joining me for dinner this evening?")
print(f"Mr {dinner_guests[2].title()}, Would you do me the honor of joining me for dinner this evening?")
