import pygame

from settings import PLAYER_IMAGE, PLAYER_OFFSET, PLAYER_SPEED, SCREEN_HEIGHT, SCREEN_WIDTH


class Player:
    """玩家飞机"""
    def __init__(self):
        self.image = pygame.image.load(PLAYER_IMAGE).convert_alpha()
        self.rect = self.image.get_rect()

        # self.x、self.y 用于记录与控制飞机的实际位置，对应self.rect.x、self.rect.y
        # self.rect 是一个矩形对象，具有width和height属性，表示飞机的宽度和高度， 
        # self.rect 还有x、y属性表示飞机的左上角坐标， 用于绘制飞机时定位。
        self.x = (SCREEN_WIDTH - self.rect.width) / 2
        self.y = SCREEN_HEIGHT - self.rect.height
        self.rect.x = self.x
        self.rect.y = self.y

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
        self.x = max(-PLAYER_OFFSET, min(self.x, SCREEN_WIDTH - self.rect.width + PLAYER_OFFSET))
        self.y = max(0, min(self.y, SCREEN_HEIGHT - self.rect.height))

    def update(self, keys):
        """接收按键信息，更新玩家飞机：
        依次完成移动、边界限制和位置同步"""
        self.move(keys)
        self.stay_in_screen()

        # 同步 rect 位置, 更新飞机位置
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, screen):
        """绘制玩家飞机"""
        screen.blit(self.image, self.rect)
