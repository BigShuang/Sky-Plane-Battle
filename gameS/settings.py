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

# TODO 5.3：配置开始界面音乐、游戏音乐、两种碰撞音效及其音量。音乐文件用于循环播放，音效文件用于单次播放；
# START_MUSIC = "assets/audio/space_adventure_clip.ogg"
# GAME_MUSIC = 
# ENEMY_EXPLOSION_SOUND = 
# PLAYER_EXPLOSION_SOUND = 
# START_MUSIC_VOLUME = 0.15
# GAME_MUSIC_VOLUME =
# ENEMY_EXPLOSION_VOLUME =
# PLAYER_EXPLOSION_VOLUME =

# TODO 5.4：按播放顺序配置 5 张爆炸图片，并设置每张图片持续显示的游戏帧数。
# 图片应按照 explosion1.png～explosion5.png 排列；切帧间隔越大，动画播放得越慢。
# EXPLOSION_IMAGES = []
# EXPLOSION_FRAME_INTERVAL = 

# 定义开始、游戏中和游戏结束三种状态常量，状态值依次为 0、1、2。
STATUS_START = 0
STATUS_PLAYING = 1
STATUS_GAME_OVER = 2

BACKGROUND_COLOR = (20, 28, 44)
# TODO 5.1：配置游戏背景图片路径。
# BACKGROUND_IMAGE = "assets/bg1.png"

# TODO 5.2：配置背景每个游戏帧向下移动的速度。
# BACKGROUND_SPEED = 1

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
