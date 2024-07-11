# 缩减名单 你只能邀请2位嘉宾
# 以3-6为基础，末尾添加一行消息，你只能邀请2人
# 使用pop()不断删除名单的嘉宾，直到只有2位为止，每次删除一位都要打印抱歉信息

message = """
I apologize for the inconvenience, 
but due to limited seating, 
we must regrettably remove some guests from the dinner invitation list. 
We hope to include you in future events.
"""

dinner_guests = ['zhang san','li si','wang wu']

print(f"Mr {dinner_guests[0].title()}, Would you do me the honor of joining me for dinner this evening?\n")
print(f"Mr {dinner_guests[1].title()}, Would you do me the honor of joining me for dinner this evening?\n")
print(f"Mr {dinner_guests[2].title()}, Would you do me the honor of joining me for dinner this evening?\n")

print("I have found a larger table for dinner.")
dinner_guests.insert(0,'Anti-Mage')
dinner_guests.insert(2,'lina')
dinner_guests.append('luna')

for name in dinner_guests:
    print(f"{name.title()}, Would you do me the honor of joining me for dinner this evening?\n")

print("Due to limited seating, I can only invite two person to the dinner today.\n")

print(dinner_guests.pop().title() + message)
print(dinner_guests.pop().title() + message)
print(dinner_guests.pop().title() + message)
print(dinner_guests.pop().title() + message)
