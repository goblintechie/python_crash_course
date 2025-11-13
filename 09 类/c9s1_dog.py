# 9.1 创建和使用类
# 类几乎可以模拟任何东西

class Dog:
    """一次模拟小狗的简单尝试"""

    # 类中的函数称为方法
    # __init__是个特殊方法，每次创建新实例，Python都会调用它
    def __init__(self,name,age):
        """初始化属性name和age"""
        # 该方法的定义包含三个形参，self,name,age
        # 形参self必不可少，必须位于前面
        # Python调用这个方法创建Dog实例时，将自动传入实参self
        # 每隔与实例相关的方法调用都自动传递该实参
        # 这是一个指向实例本身的引用，让实例能够访问类中的属性和方法
        self.name = name
        self.age = age
        # self为前缀的变量可供类中的所有方法使用
        # 可以通过类的任何实例访问
        # self.name = name获取与形参name相关的值，并将其赋给变量name
        # 然后该变量被关联到当前创建的实例
        # 这种可以通过实例访问的变量称为属性

    def sit(self):
        """模拟小狗收到命令时坐下"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """模拟小狗收到命令打滚"""
        print(f"{self.name} rolled over!")

my_dog = Dog('Willie',6)
# python创建一个名为willie，年龄6岁的小狗
# Python使用实参willie和6调用Dog类的方法__init__()
# 这个方法会创建一个表示小狗的实例，并使用提供的值来设置属性name和age
# 然后Python返回一个表示这个小狗的实例，我们将这个实例赋值给了my_dog

print(f"My dog's name is {my_dog.name}.")
print(f"My dog's age is {my_dog.age}.")
my_dog.sit()
my_dog.roll_over()

# 创建多个实例
your_dog = Dog('Lucy',3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog's age is {my_dog.age}.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.roll_over()
