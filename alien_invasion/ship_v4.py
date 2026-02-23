"""
12.6.4 调整飞船速度
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

        # 在飞船的属性x中存储小数值
        # 因为self.rect.x只接受整数（像素不存在“半个”）
        self.x = float(self.rect.x)

        # 移动标志
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """根据移动标志调整飞船位置"""
        if self.moving_right:
            self.x += self.settings.ship_speed
        elif self.moving_left:
            self.x -= self.settings.ship_speed
        
        # 使用self.x计算坐标，将计算结果赋值给rect对象
        # 赋值会损失小数精度（精确值还在self.x中）
        self.rect.x = self.x
    
    def blitme(self):
        """将图像绘制到self.rect指定的位置"""
        self.screen.blit(self.image,self.rect)
