"""
12.4.1 创建ship类
"""

# 选择了飞船的图像，需要将其显示在屏幕上
# 创建一个ship模块，包含Ship类，管理飞船大部分行为

import pygame

class Ship:
    """管理飞船的类"""

    def __init__(self,ai_game):
        """初始化飞船并设置其初始位置"""

        # self.screen：告知飞船在哪个窗口上绘制
        self.screen = ai_game.screen
        # self.screen_rect：存储窗口的矩形属性，方便后面对齐坐标
        self.screen_rect = ai_game.screen.get_rect()

        # 加载飞船图像
        self.image = pygame.image.load('alien_invasion/images/ship.bmp')
        # self.rect：获取飞船图像的外接矩形
        self.rect = self.image.get_rect()

        # 要让游戏元素居中，可设置相应rect对象的属性center、centerx或centery
        # 要让游戏元素与屏幕边缘对齐，可使用属性top、bottom、left或right
        # 还有一些组合属性：midbottom、midtop、midleft和midright
        # 要调整游戏元素的水平或垂直位置，可使用属性x和y，是矩形左上角x、y坐标

        # 注意，原点(0,0)位于屏幕左上角，向右下方移动时，坐标值会增大
        # 也就是在(1200,800)的屏幕中，右下角坐标为(1200,800)
        # 这些坐标是对游戏窗口而言，不是物理屏幕

        # 对于每艘飞船，都将其置于屏幕底部中央
        self.rect.midbottom = self.screen_rect.midbottom
    
    def blitme(self):
        """将图像绘制到self.rect指定的位置"""
        self.screen.blit(self.image,self.rect)

