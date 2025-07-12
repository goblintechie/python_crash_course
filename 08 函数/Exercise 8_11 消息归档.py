# 练习8-11：消息归档　修改你为完成练习8-10而编写的程序，
# 在调用函数send_messages()时，向它传递消息列表的副本。
# 调用函数send_messages()后，将两个列表都打印出来，
# 确认保留了原始列表中的消息。

message_list = ['a','b','c','d','e']
send_messages_list = []

def show_messages(message):
    """打印列表中的消息"""
    for m in message:
        print(f"This is the message: {m}")

def send_messages(message,sent_messages):
    """打印消息，移动消息"""
    while message:
        send_msg = message.pop()
        print(f"The sent message is {send_msg}")
        sent_messages.append(send_msg)
    
show_messages(message_list)
send_messages(message_list[:],send_messages_list)
# show_messages(send_messages_list)
show_messages(message_list)
