import random

import pygame

from settings import ENEMY_IMAGE, ENEMY_SPEED, SCREEN_HEIGHT, SCREEN_WIDTH


class Enemy:
    """从屏幕上方出现并向下移动的敌机"""
    def __init__(self):
        self.image = pygame.image.load(ENEMY_IMAGE).convert_alpha()
        self.rect = self.image.get_rect()

        # TODO 2.1：随机设置敌机的横坐标，保证整张图片都在屏幕宽度内；
        # 同时将敌机放在屏幕上方

        # TODO 2.1：将敌机的初始位置同步到 rect。
        self.rect.x = self.x
        self.rect.y = self.y

        self.speed = ENEMY_SPEED


    def update(self):
        """更新敌机位置"""
        # TODO 2.1：使用 self.speed 让敌机向下移动，并同步 rect.y。
        pass

    def is_out_of_screen(self):
        """判断敌机是否已完全飞出屏幕底部"""
        # TODO 2.1：当敌机顶部越过屏幕底边时返回 True， 否则返回False

    def draw(self, screen):
        screen.blit(self.image, self.rect)
