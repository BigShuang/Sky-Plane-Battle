import pygame

from bullet import Bullet
from settings import PLAYER_IMAGE, PLAYER_OFFSET, PLAYER_SPEED, SCREEN_HEIGHT, SCREEN_WIDTH

class Player:
    """玩家飞机"""

    def __init__(self):
        self.image = pygame.image.load(PLAYER_IMAGE).convert_alpha()
        self.rect = self.image.get_rect()

        self.x = (SCREEN_WIDTH - self.rect.width) / 2
        self.y = SCREEN_HEIGHT - self.rect.height
        self.rect.x = round(self.x)
        self.rect.y = round(self.y)
        self.speed = PLAYER_SPEED

    def move(self, keys):
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.x += self.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.y += self.speed

    def stay_in_screen(self):
        """限制飞机不能飞出屏幕"""
        if self.x < -PLAYER_OFFSET:
            self.x = -PLAYER_OFFSET
        if self.x > SCREEN_WIDTH - self.rect.width + PLAYER_OFFSET:
            self.x = SCREEN_WIDTH - self.rect.width + PLAYER_OFFSET
        if self.y < 0:
            self.y = 0
        if self.y > SCREEN_HEIGHT - self.rect.height:
            self.y = SCREEN_HEIGHT - self.rect.height

    def update(self, keys):
        self.move(keys)
        self.stay_in_screen()
        self.rect.x = round(self.x)
        self.rect.y = round(self.y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def shoot(self):
        """从飞机顶部中间发射子弹"""
        # TODO 3.1：根据玩家飞机的顶部中点创建并返回一个 Bullet 对象。
        pass
