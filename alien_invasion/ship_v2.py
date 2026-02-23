"""
12.6.2 允许持续移动

在alien_invasion_v6中，只有按下一次右箭头，飞船才会移动一个像素
我们希望在按下按键时，飞船可以持续移动，直到松开按键为止
要检测玩家松开按键，就要检测pygame.KEYUP事件
结合使用KEYDOWN和KEYUP事件，以及名为moving_right的标志来实现持续移动
当moving_right标志为False时，停止移动
按下向右箭头时，标志为True，松开时标志重新设置为False
飞船的属性由Ship控制，给这个类增加一个moving_right的属性，一个名为update()的方法
update()用来检查moving_right状态
我们将在while循环中调用这个方法
"""
import pygame

class Ship:
    """管理飞船的类"""

    def __init__(self,ai_game):
        """初始化飞船并设置其初始位置"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load('alien_invasion/images/ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        # 移动标志
        self.moving_right = False
    
    def update(self):
        """根据移动标志调整飞船位置"""
        if self.moving_right:
            self.rect.x += 1
    
    def blitme(self):
        """将图像绘制到self.rect指定的位置"""
        self.screen.blit(self.image,self.rect)

