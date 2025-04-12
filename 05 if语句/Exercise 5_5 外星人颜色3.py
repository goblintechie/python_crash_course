# 将练习5-4中的if-else结构改为if-elif-else结构。
# 如果外星人是绿色的，就打印一条消息，指出玩家获得了5分。
# 如果外星人是黄色的，就打印一条消息，指出玩家获得了10分。
# 如果外星人是红色的，就打印一条消息，指出玩家获得了15分。
# 编写这个程序的三个版本，分别在外星人为绿色、黄色和红色时打印一条消息。

alien_color = 'green'
if alien_color == 'green':
    print("You have got 5 points.")
elif alien_color == 'yellow':
    print("You have got 10 points.")
else:
    print("You have got 15 points.")

alien_color = 'yellow'
if alien_color == 'green':
    print("You have got 5 points.")
elif alien_color == 'yellow':
    print("You have got 10 points.")
else:
    print("You have got 15 points.")

alien_color = 'red'
if alien_color == 'green':
    print("You have got 5 points.")
elif alien_color == 'yellow':
    print("You have got 10 points.")
else:
    print("You have got 15 points.")
