# 修改为完成练习6-2而编写的程序，让每个人都可以有多个喜欢的数，然后将每个人的名字及其喜欢的数打印出来。

favorite_numbers = {
    "Olivia": [1,2,3,4,5],
    "Noah": [3,2,4,5,3],
    "Emma": [3,4,3,2,4],
    "James": [4,5,4,2,6],
    "Ava": [5,9,7,4,2]
}

for name,numbers in favorite_numbers.items():
    print(f"\n{name}'s favorite number:")
    for n in numbers:
        print(f"\t{n}")