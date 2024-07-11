# 比萨 写出至少三种比萨，存在列表中，用for循环打印出来
# 修改这个for循环，使其打印包含比萨名称的句子，而不仅仅是比萨的名称，对每种比萨都显示一行输出
# 程序末尾加一行代码，不在for循环中，指出你有多喜欢比萨

pizzas = ['Pizza Margherita', 'Pizza Napoletana', 'Pizza Quattro Stagioni', 'Pizza Quattro Formaggi',
         'Pizza Marinara', 'Pizza Capricciosa', 'Pizza Prosciutto e Funghi', 'Pizza Diavola']

for pizza in pizzas:
    print(pizza)

for pizza in pizzas:
    print(f"I like {pizza}.")
print("I really like pizza.")
