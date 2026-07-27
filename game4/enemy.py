import random

import pygame

from settings import ENEMY_IMAGE, ENEMY_SPEED, SCREEN_HEIGHT, SCREEN_WIDTH


class Enemy:
    """敌人飞机"""

    def __init__(self):
        # 加载敌人图片
        self.image = pygame.image.load(str(ENEMY_IMAGE)).convert_alpha()
        self.rect = self.image.get_rect()
        # TODO 4.2：根据带透明通道的敌机图片创建像素碰撞遮罩 mask。
        # self.mask = pygame.mask.from_surface(self.image)

        # 敌人从屏幕顶部随机位置出现
        self.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.y = -self.rect.height

        # 敌人向下移动的速度
        self.speed = ENEMY_SPEED

        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        """更新敌人状态"""
        self.y += self.speed
        self.rect.y = round(self.y)

    def is_out_of_screen(self):
        """判断敌人是否飞出屏幕"""
        return self.rect.top > SCREEN_HEIGHT

    def draw(self, screen):
        """绘制敌人"""
        screen.blit(self.image, self.rect)
