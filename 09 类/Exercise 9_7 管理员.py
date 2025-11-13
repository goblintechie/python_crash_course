"""
练习9-7:管理员 管理员是一种特殊的用户。
编写一个名为Admin的类,让它继承为完成练习9-3或练习9-5而编写的User类。
添加一个名为privileges的属性,
用于存储一个由字符串（如"can add post"、"can delete post"、"can ban user"等）组成的列表。
编写一个名为show_privileges()的方法，显示管理员的权限。
创建一个Admin实例,并调用这个方法。
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

class Admin(User):
    """继承User类"""
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges =  ["can add post","can delete post","can ban user"]

    def show_privileages(self):
        """显示权限的方法"""
        print("管理员拥有的权限包括：")
        for privilege in self.privileges:
            print(f"- {privilege}")

new_admin = Admin("admin","test")
new_admin.describe_user()
new_admin.show_privileages()
