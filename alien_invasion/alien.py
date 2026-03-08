"""
13.2 外星人来了

在屏幕上边缘创建一个外星人，再生成一群外星人
外星人向两边和下方移动，删除被击中的外星人
在玩家的飞船用完之后结束游戏

在屏幕左上角添加外星人，指定合适的边距
根据一个外星人的边距和屏幕尺寸，计算可以容纳多少个外星人
使用循环来创建一系列外星人，使屏幕上半部分填满

让外星人向两边和下方移动，直到它们全部被消灭、撞到玩家或抵达屏幕底部
如果外星人全部被击落，将再创建一群外星人
如果有外星人撞到玩家或抵达底部，将销毁飞船并再创建一群外星人

限制玩家飞船的数量，当飞船用完，游戏结束

13.2.1 创建Alien类

"""

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """表示单个外星人的类"""

    def __init__(self, ai_game):
        """初始化外星人并设置起始位置"""
        super().__init__()
        self.screen = ai_game.screen

        # 加载外星人图像并设置rect属性
        self.image = pygame.image.load('alien_invasion/images/alien.bmp')
        self.rect = self.image.get_rect()

        # 每个外星人最初都在屏幕左上方
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人精确的水平位置
        self.x = float(self.rect.x)
        
        
