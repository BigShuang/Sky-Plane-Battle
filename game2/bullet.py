import pygame

from settings import BULLET_IMAGE, BULLET_SPEED


class Bullet:
    """玩家子弹"""
    def __init__(self, center_x, top_y):
        # 加载子弹图片
        self.image = pygame.image.load(str(BULLET_IMAGE)).convert_alpha()
        self.rect = self.image.get_rect()

        # 子弹从玩家飞机顶部中间射出
        self.rect.midbottom = (center_x, top_y)
        self.x = self.rect.x
        self.y = self.rect.y

        # 子弹向上移动的速度
        self.speed = BULLET_SPEED

    def update(self):
        """更新子弹状态"""
        self.y -= self.speed
        self.rect.y = round(self.y)

    def is_out_of_screen(self):
        """判断子弹是否飞出屏幕上方"""
        return self.rect.bottom < 0

    def draw(self, screen):
        """绘制子弹"""
        screen.blit(self.image, self.rect)
