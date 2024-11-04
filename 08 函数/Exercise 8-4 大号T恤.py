# 修改make_shirt()，默认制作“I love Python”字样的大号T恤
# 调用函数，一个印有默认字样的大号T恤，一个印有默认字样的中号T恤，以及其他字样的T恤

def make_shirt(size='XL',words='I love Python'):
    print(f"The size of the shirt is {size}, and the words are {words}.")

make_shirt()
make_shirt(size='M')
make_shirt(size='S',words='I love Swift')