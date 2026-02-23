"""
12.6.5 限制飞船的活动范围
如果一直按着一个方向键不松手，飞船就会飞出屏幕之外
我们要限制飞船的活动范围，在它到达屏幕边缘的时候停止移动
所以要修改update()方法
"""
import pygame

class Ship:
    """管理飞船的类"""

    def __init__(self,ai_game):
        """初始化飞船并设置其初始位置"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load('alien_invasion/images/ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """根据移动标志调整飞船位置"""
        # self.rect.right返回飞船外接矩形右边缘的x坐标，如果小于屏幕右边缘，则未到达右边
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        # self.rect.left返回飞船外接矩形左边缘的x坐标，如果大于0，则未到达左边
        elif self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x
    
    def blitme(self):
        """将图像绘制到self.rect指定的位置"""
        self.screen.blit(self.image,self.rect)
