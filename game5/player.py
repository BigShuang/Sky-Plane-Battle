import pygame

from bullet import Bullet
from settings import PLAYER_IMAGE, PLAYER_SPEED, SCREEN_HEIGHT, SCREEN_WIDTH


class Player:
    """玩家飞机"""

    def __init__(self):
        # 加载飞机图片
        self.image = pygame.image.load(str(PLAYER_IMAGE)).convert_alpha()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

        # 飞机初始位置：屏幕底部中间
        self.x = (SCREEN_WIDTH - self.rect.width) / 2
        self.y = SCREEN_HEIGHT - self.rect.height
        self.rect.x = round(self.x)
        self.rect.y = round(self.y)

        # 飞机速度，数值越大移动越快
        self.speed = PLAYER_SPEED

    def move(self, keys):
        """根据键盘按键移动飞机"""
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
        """更新飞机状态"""
        self.move(keys)
        self.stay_in_screen()
        self.rect.x = round(self.x)
        self.rect.y = round(self.y)

    def draw(self, screen):
        """绘制飞机"""
        screen.blit(self.image, self.rect)

    def shoot(self):
        """从飞机顶部中间发射子弹"""
        return Bullet(self.rect.centerx, self.rect.top)
