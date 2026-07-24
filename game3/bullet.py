import pygame

from settings import BULLET_IMAGE, BULLET_SPEED


class Bullet:
    """从玩家飞机向上飞行的子弹"""

    def __init__(self, center_x, top_y):
        self.image = pygame.image.load(BULLET_IMAGE).convert_alpha()
        self.rect = self.image.get_rect()

        self.rect.midbottom = (center_x, top_y)
        self.x = self.rect.x
        self.y = self.rect.y
        self.speed = BULLET_SPEED

    def update(self):
        self.y -= self.speed
        self.rect.y = round(self.y)

    def is_out_of_screen(self):
        return self.rect.bottom < 0

    def draw(self, screen):
        screen.blit(self.image, self.rect)

