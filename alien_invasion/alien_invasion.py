"""
12.3 开始游戏项目

开始开发游戏《外星人入侵》吧！
"""

# 创建一个pygame窗口，用于绘制游戏元素（飞船，外星人）
# 要让游戏响应玩家输入，设置背景颜色，加载飞船图像

# 12.3.1 创建pygame窗口及响应用户输入

import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """管理游戏资源和行为的类"""
    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.bg_color = (self.settings.bg_color)

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            # 监视键盘和鼠标事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            pygame.display.flip()

if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()
