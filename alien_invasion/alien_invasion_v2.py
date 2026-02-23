"""
12.3.3 创建设置类

v2：引入了settings的版本
"""

import sys
import pygame
from settings import Settings

class AlienInvasion:
    """创建一个表示游戏的类，以创建空的pygame的窗口"""
    
    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        # 导入Settings类，调用pygame.init()
        # 创建一个Settings实例并将其赋值给self.settings
        self.settings = Settings()
        # 创建屏幕时使用了self.settings的属性
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
    
    def run_game(self):
        """开始游戏的主循环"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # 每次循环时都重绘屏幕
            self.screen.fill(self.settings.bg_color)
            # 让最近绘制的屏幕可见
            pygame.display.flip()

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
