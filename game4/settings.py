import pygame


# 1. 游戏基本设置
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 800
FPS = 60

PLAYER_OFFSET = 15 # 玩家飞机可超出屏幕左右边缘的距离

PLAYER_IMAGE = "assets/player1.png"
PLAYER_SPEED = 10

ENEMY_IMAGE = "assets/enemy1.png"
ENEMY_SPEED = 3

BULLET_IMAGE = "assets/bullet1.png"
BULLET_SPEED = 12

SHOOT_INTERVAL = 200
ADD_ENEMY_INTERVAL = 1200

ADD_ENEMY_EVENT = pygame.USEREVENT + 1
SHOOT_EVENT = pygame.USEREVENT + 2

# TODO 4.1：定义开始、游戏中和游戏结束三种状态常量，状态值依次为 0、1、2。
# STATUS_START = 0
# STATUS_PLAYING = 1
# STATUS_GAME_OVER = 2

BACKGROUND_COLOR = (20, 28, 44)
WHITE = (255, 255, 255)
LIGHT_GRAY = (220, 220, 220)
YELLOW = (255, 220, 120)

# 集中配置中英文界面文本，并设置当前使用的语言。
ZH = "zh"
EN = "en"
# 在这里设置游戏显示语言：中文用 ZH，英文用 EN
CURRENT_LANGUAGE = EN

TEXTS = {
    ZH: {
        "caption": "飞机大战 基础版4",
        "title": "飞机大战",
        "start_prompt": "按任意键开始游戏",
        "game_over": "游戏结束",
        "score": "分数：{score}",
        "final_score": "得分：{score}",
        "restart_prompt": "按任意键重新开始游戏",
    },
    EN: {
        "caption": "Sky Plane Battle Basic 4",
        "title": "Sky Plane Battle",
        "start_prompt": "Press any key to start",
        "game_over": "Game Over",
        "score": "Score: {score}",
        "final_score": "Score: {score}",
        "restart_prompt": "Press any key to restart",
    },
}


def get_text(current_language, key, **kwargs):
    """根据当前语言获取文字"""
    # 获取当前语言对应的文字，并填充 score 等占位符。
    return TEXTS[current_language][key].format(**kwargs)
