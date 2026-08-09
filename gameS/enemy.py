import random

import pygame

from settings import ENEMY_IMAGE, ENEMY_SPEED, SCREEN_HEIGHT, SCREEN_WIDTH


class Enemy:
    """从屏幕上方出现并向下移动的敌机"""

    def __init__(self):
        self.image = pygame.image.load(ENEMY_IMAGE).convert_alpha()
        self.rect = self.image.get_rect()

        self.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.y = -self.rect.height
        self.rect.x = self.x
        self.rect.y = self.y

        self.speed = ENEMY_SPEED

    def update(self):
        """更新敌机位置"""
        self.y += self.speed
        self.rect.y = self.y

    def is_out_of_screen(self):
        """判断敌机是否已完全飞出屏幕底部"""
        return self.rect.top > SCREEN_HEIGHT

    def draw(self, screen):
        """绘制敌机"""
        screen.blit(self.image, self.rect)
