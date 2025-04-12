# 在为完成练习6-1而编写的程序中，再创建两个表示人的字典，
# 然后将这三个字典都存储在一个名为people的列表中。
# 遍历这个列表，将其中每个人的所有信息都打印出来。

person = {'first_name':'lily','last_name':'wang','age':30,'city':'hangzhou'}

people = [
    {
        'first_name':'lily',
        'last_name':'wang',
        'age':30,
        'city':'hangzhou'
    },
    {
        'first_name':'grace',
        'last_name':'ye',
        'age':26,
        'city':'nanjing'
    },
    {
        'first_name':'unknown',
        'last_name':'unknown',
        'age':'unknown',
        'city':'unknown'
    }
]

for person in people:
    print(person)