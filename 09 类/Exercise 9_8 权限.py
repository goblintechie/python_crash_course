"""
练习9-8:权限 编写一个名为Privileges的类,
它只有一个属性privileges,其中存储了练习9-7所述的字符串列表。
将方法show_privileges()移到这个类中。
在Admin类中,将一个Privileges实例用作其属性。
创建一个Admin实例,并使用方法show_privileges()来显示其权限。
"""

class Privileges:
    """该类只有一个属性privileges,存储了9-7的所有字符串列表"""
    def __init__(self):
        """定义privileges属性"""
        self.privileges = ["can add post","can delete post","can ban user"]

    def show_privileages(self):
        """显示权限的方法"""
        print("管理员拥有的权限包括：")
        for privilege in self.privileges:
            print(f"- {privilege}")

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
        # python创建一个Privileges实例，将这个实例存储在privileges属性中
        self.privileges = Privileges()

new_admin = Admin("admin","test")
# Python在实例new_admin中查找属性privileges
# 因为Privileges实例存储在这个属性中
# 因此可以调用Privileges实例的方法show_privileges()
new_admin.privileges.show_privileages()
