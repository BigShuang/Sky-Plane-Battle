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
        # TODO 1.1：读取方向键和 W/A/S/D 的状态，使用 self.speed
        # 分别修改 self.x、self.y，并允许同时按两个方向键进行斜向移动。
        # if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        #     self.x -= self.speed

    def stay_in_screen(self):
        """限制飞机不能飞出屏幕"""
        # TODO 1.2：限制玩家飞机的上下左右边界，要使用界面的长度和宽度来计算
        # 计算右边界和下边界时， 需要分别考虑飞机矩形对象的宽度和高度。
        # 飞机矩形对象： self.rect, 具有width和height属性
        # if self.x < ?: 
        # if self.y < ?:
        
        # 飞机中间射出炮弹，左右两侧可以适当超出屏幕一定范围，对应 PLAYER_OFFSET

    def update(self, keys):
        """接收按键信息，更新玩家飞机：
        依次完成移动、边界限制和位置同步"""
        # TODO 1.2：按照“移动 -> 边界限制 -> ”的顺序更新玩家。

        # 同步 rect 位置, 更新飞机位置
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, screen):
        """绘制玩家飞机"""
        screen.blit(self.image, self.rect)
