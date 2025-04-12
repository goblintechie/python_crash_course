"""
编写一个名为favorite_book()的函数
其中包含名为title的形参
打印一条消息：
One of my favorite books is Alice in Wonderland.
调用这个函数，并将一本书的名称作为实参传递给它。
"""

def favorite_book(title):
    """打印最喜欢的书名"""
    print(f"One of my favorite books is {title.title()}.")

favorite_book('elon musk')
