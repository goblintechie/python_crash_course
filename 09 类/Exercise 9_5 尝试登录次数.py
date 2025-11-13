"""
练习9-5：尝试登录次数
在为完成练习9-3而编写的User类中，添加一个名为login_attempts的属性。
编写一个名为increment_login_attempts()的方法，将属性login_attempts的值加1。
再编写一个名为reset_login_attempts()的方法，将属性login_attempts的值重置为0。

根据User类创建一个实例，再调用方法increment_login_attempts()多次。
打印属性login_attempts的值，确认它被正确地递增。
然后，调用方法reset_login_attempts()，并再次打印属性login_attempts的值，确认它被重置为0。
"""

class User:
    """创建一个用户类"""

    def __init__(self,first_name,last_name):
        """定义用户类"""
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        """描述用户"""
        print(f"User's full name is {self.first_name.title()} {self.last_name.title()}.")

    def greet_user(self):
        """问候用户"""
        print(f"Hello, {self.first_name.title()} {self.last_name.title()}.")

    def increment_login_attempts(self):
        """将尝试登录次数加1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """重置登录次数为0"""
        self.login_attempts = 0

user1 = User('bob','bao')
user2 = User('alice','ai')
user1.describe_user()
user1.greet_user()

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(f"Login times is {user1.login_attempts}.")

user1.reset_login_attempts()
print(f"Login times is {user1.login_attempts}.")
