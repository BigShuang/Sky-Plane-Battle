import pygame

from settings import PLAYER_IMAGE, PLAYER_SPEED, SCREEN_HEIGHT, SCREEN_WIDTH


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
        """根据方向键或 W/A/S/D 移动飞机"""
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
        if self.x < 0:
            self.x = 0
        if self.x > SCREEN_WIDTH - self.rect.width:
            self.x = SCREEN_WIDTH - self.rect.width
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

