"""
练习9-3：用户　创建一个名为User的类，
其中包含属性first_name和last_name，以及用户简介通常会存储的其他几个属性。
在类User中定义一个名为describe_user()的方法，用于打印用户信息摘要。
再定义一个名为greet_user()的方法，用于向用户发出个性化的问候。
创建多个表示不同用户的实例，并对每个实例调用上述两个方法。
"""

class User:
    """创建一个用户类"""

    def __init__(self,first_name,last_name):
        """定义用户类"""
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        """描述用户"""
        print(f"User's full name is {self.first_name.title()} {self.last_name.title()}.")

    def greet_user(self):
        """问候用户"""
        print(f"Hello, {self.first_name.title()} {self.last_name.title()}.")

user1 = User('bob','bao')
user2 = User('alice','ai')
user1.describe_user()
user1.greet_user()
