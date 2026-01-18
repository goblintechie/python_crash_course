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
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('alien_invasion/images/ship.bmp')
        self.rect = self.image.get_rect()

        # 对于每艘飞船，都将其置于屏幕底部中央
        self.rect.midbottom = self.screen_rect.midbottom
    
    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)