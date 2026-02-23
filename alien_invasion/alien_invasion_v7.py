"""
12.6.2 允许持续移动

v7：已经修改了Ship类，通过moving_right属性来移动，现在需要修改_check_events()
在玩家松开时将moving_right设置为False
"""

import sys
import pygame
from settings import Settings
from ship_v2 import Ship

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
            self.ship.update()
            self._update_screen()
            # 飞船位置在检测到键盘事件后更新，位置更新要早于更新屏幕

    def _check_events(self):
        """响应按键和鼠标事件"""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        # 玩家按下右键，修改moving_right属性
                        self.ship.moving_right = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        # 玩家松开右键，修改moving_right属性
                        self.ship.moving_right = False

    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
