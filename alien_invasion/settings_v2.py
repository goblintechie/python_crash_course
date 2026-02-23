"""
12.6.4 调整飞船速度

目前飞船移动速度是一次1像素
在Settings类中添加ship_speed属性，控制飞船速度
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
        self.ship_speed = 5

        # 将速度设置为小数值，可以更加细致地控制飞船速度
        # 但是rect的x灯属性只能存储整数值，所以要修改Ship类
