"""
12.6 驾驶飞船

v6：编写代码，在用户按下左或右按键时做出响应
"""

import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """创建一个表示游戏的类，以创建空的pygame的窗口"""
    
    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
    
    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """
        响应按键和鼠标事件
        每当用户按键，都将在pygame中注册一个事件
        事件都是方法pygame.event.get()获取的
        所以需要在_check_events()中指定要检查哪些类型的事件
        每次按键都注册为一个KEYDOWN事件
        """
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        # 向右移动
                        self.ship.rect.x += 1

    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
