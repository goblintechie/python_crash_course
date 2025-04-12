# 创建多个表示宠物的字典，每个字典都包含宠物的类型及其主人的名字。
# 将这些字典存储在一个名为pets的列表中，再遍历该列表，并将有关每个宠物的所有信息都打印出来。

# names = ["Emily", "Jack", "Sophia", "Liam", "Isabella"]

pets = [
    {
        'kind':'Labrador Retriever',
        'master_name':'Emily'
    },
    {
        'kind':'German Shepherd',
        'master_name':'Jack'
    },
    {
        'kind':'Golden Retriever',
        'master_name':'Sophia'
    },
    {
        'kind':'Bulldog',
        'master_name':'Liam'
    },
    {
        'kind':'Beagle',
        'master_name':'Isabella'
    },
]

for pet in pets:
    print("\nPets' information:")
    print(f"\tPet: {pet['kind']}, \n\tMaster's name: {pet['master_name']}")