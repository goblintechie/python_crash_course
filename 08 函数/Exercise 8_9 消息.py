# 练习8-9 消息 创建一个列表，其中包含一系列简短文本消息
# 将该列表传递给show_messages()的函数，这个函数会打印每条文本消息

msg = ['a','b','c','d','e']

def show_messages(message):
    """打印列表中的消息"""
    for m in msg:
        print(f"This is the message: {m}")

show_messages(msg)
