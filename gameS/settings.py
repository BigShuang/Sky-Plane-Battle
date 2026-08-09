import pygame


SCREEN_WIDTH = 500
SCREEN_HEIGHT = 800
FPS = 60

PLAYER_OFFSET = 15 # 玩家飞机可超出屏幕左右边缘的距离


PLAYER_IMAGE = "assets/player1.png"
PLAYER_SPEED = 10

ENEMY_IMAGE = "assets/enemy1.png"
ENEMY_SPEED = 3

# TODO 3.1：设置子弹图片路径和速度（10上下）
BULLET_IMAGE = "assets/bullet1.png"
BULLET_SPEED = 10

ADD_ENEMY_INTERVAL = 1200
SHOOT_INTERVAL = 200  # 子弹射击间隔
ADD_ENEMY_EVENT = pygame.USEREVENT + 1
SHOOT_EVENT = pygame.USEREVENT + 2  # 子弹射击事件

PLAYING = "playing"
BACKGROUND_COLOR = (20, 28, 44)
