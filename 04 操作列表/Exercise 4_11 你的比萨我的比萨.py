# 你的比萨，我的比萨　在你为完成练习4-1而编写的程序中，创建比萨列表的副本，并将其赋给变量friend_pizzas，再完成如下任务。
# 在原来的比萨列表中添加一种比萨。
# 在列表friend_pizzas中添加另一种比萨。
# 核实有两个不同的列表。
# 为此，打印消息“My favorite pizzas are:”，再使用一个for循环来打印第一个列表；
# 打印消息“My friend's favorite pizzas are:”，再使用一个for循环来打印第二个列表。
# 核实新增的比萨被添加到了正确的列表中。

my_pizzas = ['Pizza Margherita', 'Pizza Napoletana', 'Pizza Quattro Stagioni', 'Pizza Quattro Formaggi',
         'Pizza Marinara', 'Pizza Capricciosa', 'Pizza Prosciutto e Funghi', 'Pizza Diavola']
friend_pizzas = my_pizzas[:]

my_pizzas.append('Pizza Margherita Extra')
friend_pizzas.append('Pizza Salsiccia e Peperoni')

# print(my_pizzas)
# print(friend_pizzas)

print('My favorite pizzas are:')
for pizza in my_pizzas:
    print(pizza)
print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
