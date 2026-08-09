import pygame

from settings import BULLET_IMAGE, BULLET_SPEED


class Bullet:
    """从玩家飞机向上飞行的子弹"""

    def __init__(self, center_x, top_y):
        # TODO 3.1：加载子弹图片，并获取其 rect。

        # TODO 3.1：将子弹图片的底部中点放在玩家飞机的顶部中点。
        # 玩家飞机的顶部中点: (center_x, top_y)

        # TODO 3.1：保存子弹的位置和速度。
        
        pass

    def update(self):
        """让子弹向屏幕上方移动"""
        # TODO 3.1：使用 self.speed 更新子弹纵坐标，并同步 rect.y。
        pass

    def is_out_of_screen(self):
        """判断子弹是否已经完全离开屏幕上方"""
        # TODO 3.1：子弹底部越过屏幕上边界时返回 True，否则返回 False。
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)
