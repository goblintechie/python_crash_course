"""
12.6.8 全屏游戏

v12：在macOS系统中使用全屏模式会提升游戏表现（比如飞船移动更快）
要在全屏模式下运行，要修改__init__()方法
"""

import sys
import pygame
from settings_v2 import Settings
from ship_v5 import Ship

class AlienInvasion:
    """创建一个表示游戏的类，以创建空的pygame的窗口"""
    
    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        self.settings = Settings()
        # 参数（0,0）和FULLSCREEN生成一个覆盖显示器的屏幕
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        # 因为不知道屏幕的宽度和高度（显示器可能不同），所以创建屏幕后用屏幕的rect宽高属性更新一下settings
        # 虽然游戏进入全屏了，但是飞船的边界判断还是根据settings的属性来的，所以要赋值回去，即硬件约束软件
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
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
            # 先判断按键类型（type），然后再看是哪个方向
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self,event):
        """响应按键：下"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
    
    def _check_keyup_events(self,event):
        """响应按键：上"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
