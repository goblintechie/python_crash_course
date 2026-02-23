"""
12.3.1 开始游戏项目

开始开发游戏《外星人入侵》吧！

v1：没有引入settings的版本
"""

# 创建一个pygame窗口，用于绘制游戏元素（飞船，外星人）
# 要让游戏响应玩家输入，设置背景颜色，加载飞船图像

# 12.3.1 创建pygame窗口及响应用户输入

import sys
import pygame

# 导入sys和pygame，模块pygame中包含开发所需的功能
# 退出时需要用到sys中的QUIT工具

class AlienInvasion:
    """创建一个表示游戏的类，以创建空的pygame的窗口"""
    def __init__(self):
        """初始化游戏并创建游戏资源"""
        # 在AlienInvasion类的方法__init__()中，调用函数pygame.init()来初始化背景
        pygame.init() 
        # 调用pygame.display.set_mode()创建一个显示窗口
        # 游戏的所有图形元素都在这个窗口中绘制
        # 将这个窗口赋值给属性self.screen，这个类中的所有方法都可以使用它
        self.screen = pygame.display.set_mode((1200,800))
        # 赋值给属性self.screen的对象是一个surface
        # 在pygame中surface是屏幕一部分，每个元素都是一个surface
        # display.set_mode()返回的surface表示整个游戏窗口
        pygame.display.set_caption("Alien Invasion")
        self.bg_lolor = (230,230,230)
    
    # 这个游戏由方法run_game()控制
    def run_game(self):
        """开始游戏的主循环"""
        while True:
            # 监视键盘和鼠标事件
            # 事件循环，事件是玩家玩游戏时执行的操作
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # 每次循环执行重绘屏幕
            self.screen.fill(self.bg_lolor)

            # 让最近绘制的屏幕可见
            # 每次执行while循环时都会一个空屏幕，并擦去旧屏幕
            # 使得只有最新屏幕可见
            pygame.display.flip()

if __name__ == "__main__":
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()
