# make_shirt()函数，接受一个尺码，以及要打印到T恤上的字样
# 应该打印一个句子，说明T恤的尺寸和字样

def make_shirt(size,words):
    print(f"The size of the shirt is {size}, and the words are {words}.")

make_shirt('XXL','Hello')
make_shirt(size='XXL',words='你好')