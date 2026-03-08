"""
13.3.2 创建一行外星人

v19：我们要在屏幕两边减去边距，边距是一个飞碟宽度，因此中间剩余的空间：
available_space_x = settings.screen_width - (2 * alien_width)

两个飞碟的间距是一个飞碟宽度，因此一个飞碟的实际宽度就是飞碟宽度的2倍
中间剩余可以放下的飞碟数量：
number_aliens_x = available_space_x // (2 * alien_width)

然后改造_create_fleet()，使其能创建一行外星人

"""

import sys
import pygame
from settings_v4 import Settings
from ship_v5 import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """创建一个表示游戏的类，以创建空的pygame的窗口"""
    
    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
    
    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bulltes()
            self._update_screen()

    def _update_bulltes(self):
        """更新子弹的位置并删除消失的子弹"""
        self.bullets.update()
        # 删除消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        # print(len(self.bullets))

    def _check_events(self):
        """响应按键和鼠标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
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
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    
    def _check_keyup_events(self,event):
        """响应按键：上"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    
    def _fire_bullet(self):
        """创建一颗子弹，将其加入到编组bullets中"""
        # 如果子弹数量小于限制就创建新子弹
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # bullets.sprites()返回一个列表，包含编组bullets中所有精灵
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        pygame.display.flip()

    def _create_fleet(self):
        """创建外星人"""
        alien = Alien(self)
        alien_width = alien.rect.width
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        for alien_number in range(number_aliens_x):
            alien = Alien(self)
            alien.x = alien_width + 2 * alien_width * alien_number
            alien.rect.x = alien.x
            self.aliens.add(alien)

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
