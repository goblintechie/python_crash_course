"""
12.8 射击
玩家在按下空格时会发射矩形子弹，子弹在抵达屏幕上边缘时会消失

12.8.1 添加子弹设置
在方法__init__()末尾存储新类型所需的值

"""

class Settings:
    """存储游戏的所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 800
        self.screen_height = 450
        self.bg_color = (230,230,230)

        # 飞船设置
        self.ship_speed = 1.5

        # 子弹设置
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
