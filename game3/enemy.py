import random

import pygame

from settings import ENEMY_IMAGE, ENEMY_SPEED, SCREEN_HEIGHT, SCREEN_WIDTH


class Enemy:
    """敌人飞机"""

    def __init__(self):
        self.image = pygame.image.load(ENEMY_IMAGE).convert_alpha()
        self.rect = self.image.get_rect()

        self.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.y = -self.rect.height
        self.speed = ENEMY_SPEED

        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.y += self.speed
        self.rect.y = round(self.y)

    def is_out_of_screen(self):
        return self.rect.top > SCREEN_HEIGHT

    def draw(self, screen):
        screen.blit(self.image, self.rect)

