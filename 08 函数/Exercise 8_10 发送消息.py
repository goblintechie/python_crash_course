# 练习8-10：发送消息　在你为完成练习8-9而编写的程序中，
# 编写一个名为send_messages()的函数，
# 将每条消息都打印出来并移到一个名为sent_messages的列表中。
# 调用函数send_messages()，再将两个列表都打印出来，确认正确地移动了消息。

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
send_messages(message_list,send_messages_list)
# show_messages(send_messages_list)
show_messages(message_list)