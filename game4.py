import random

import pygame

# 1. 游戏基本设置
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 800
FPS = 60

PLAYER_IMAGE = "assets/player1.png"
PLAYER_SPEED = 10
ENEMY_IMAGE = "assets/enemy1.png"
ENEMY_SPEED = 3
BULLET_IMAGE = "assets/bullet1.png"
BULLET_SPEED = 12
SHOOT_INTERVAL = 200
ADD_ENEMY_EVENT = pygame.USEREVENT + 1
SHOOT_EVENT = pygame.USEREVENT + 2
START = "start"
PLAYING = "playing"
GAME_OVER = "game_over"

class Player:
    """玩家飞机"""
    def __init__(self):
        # 加载飞机图片
        self.image = pygame.image.load(PLAYER_IMAGE).convert_alpha()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

        # 飞机初始位置：屏幕底部中间
        self.x = (SCREEN_WIDTH - self.rect.width) / 2
        self.y = SCREEN_HEIGHT - self.rect.height

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


class Enemy:
    """敌人飞机"""
    def __init__(self):
        # 加载敌人图片
        self.image = pygame.image.load(ENEMY_IMAGE).convert_alpha()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

        # 敌人从屏幕顶部随机位置出现
        self.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.y = -self.rect.height

        # 敌人向下移动的速度
        self.speed = ENEMY_SPEED

        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        """更新敌人状态"""
        self.y += self.speed
        self.rect.y = round(self.y)

    def is_out_of_screen(self):
        """判断敌人是否飞出屏幕"""
        return self.rect.top > SCREEN_HEIGHT

    def draw(self, screen):
        """绘制敌人"""
        screen.blit(self.image, self.rect)


class Bullet:
    """玩家子弹"""
    def __init__(self, center_x, top_y):
        # 加载子弹图片
        self.image = pygame.image.load(BULLET_IMAGE).convert_alpha()
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


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("飞机大战 基础版4")
clock = pygame.time.Clock()
title_font = pygame.font.SysFont("Microsoft YaHei", 56)
normal_font = pygame.font.SysFont("Microsoft YaHei", 28)
pygame.time.set_timer(ADD_ENEMY_EVENT, 1200)
pygame.time.set_timer(SHOOT_EVENT, SHOOT_INTERVAL)

def draw_text(text, font, color, center):
    """在指定中心位置绘制文字"""
    text_image = font.render(text, True, color)
    text_rect = text_image.get_rect(center=center)
    screen.blit(text_image, text_rect)


def reset_game():
    """重新开始一局游戏"""
    return Player(), [], [], 0


def is_mask_collision(sprite1, sprite2):
    """判断两张图片的非透明部分是否碰撞"""
    offset_x = sprite2.rect.x - sprite1.rect.x
    offset_y = sprite2.rect.y - sprite1.rect.y
    return sprite1.mask.overlap(sprite2.mask, (offset_x, offset_y)) is not None


# 2. 游戏状态
player, enemies, bullets, score = reset_game()
game_state = START

running = True
while running:
    # 3. 处理退出事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if game_state == START or game_state == GAME_OVER:
                player, enemies, bullets, score = reset_game()
                game_state = PLAYING
        if game_state == PLAYING and event.type == ADD_ENEMY_EVENT:
            enemies.append(Enemy())
        if game_state == PLAYING and event.type == SHOOT_EVENT:
            bullets.append(player.shoot())

    if game_state == START:
        screen.fill((20, 28, 44))
        draw_text("飞机大战", title_font, (255, 255, 255), (SCREEN_WIDTH / 2, 300))
        draw_text("按任意键开始游戏", normal_font, (220, 220, 220), (SCREEN_WIDTH / 2, 390))
        pygame.display.update()
        clock.tick(FPS)
        continue

    if game_state == GAME_OVER:
        screen.fill((20, 28, 44))
        draw_text("游戏结束", title_font, (255, 255, 255), (SCREEN_WIDTH / 2, 280))
        draw_text(f"得分：{score}", normal_font, (255, 220, 120), (SCREEN_WIDTH / 2, 370))
        draw_text("按任意键重新开始游戏", normal_font, (220, 220, 220), (SCREEN_WIDTH / 2, 440))
        pygame.display.update()
        clock.tick(FPS)
        continue

    # 4. 获取键盘按键，并更新飞机
    keys = pygame.key.get_pressed()
    player.update(keys)
    for enemy in enemies:
        enemy.update()
    for bullet in bullets:
        bullet.update()
    enemies = [enemy for enemy in enemies if not enemy.is_out_of_screen()]
    bullets = [bullet for bullet in bullets if not bullet.is_out_of_screen()]

    # 5. 检查子弹和敌人的碰撞
    hit_enemies = []
    hit_bullets = []
    for bullet in bullets:
        for enemy in enemies:
            if bullet.rect.colliderect(enemy.rect):
                hit_bullets.append(bullet)
                hit_enemies.append(enemy)
                score += 10
                break
    bullets = [bullet for bullet in bullets if bullet not in hit_bullets]
    enemies = [enemy for enemy in enemies if enemy not in hit_enemies]

    # 6. 检查玩家是否撞到敌人
    for enemy in enemies:
        if is_mask_collision(player, enemy):
            game_state = GAME_OVER
            break

    # 7. 绘制画面
    screen.fill((20, 28, 44))
    for enemy in enemies:
        enemy.draw(screen)
    for bullet in bullets:
        bullet.draw(screen)
    player.draw(screen)
    draw_text(f"分数：{score}", normal_font, (255, 255, 255), (70, 30))
    pygame.display.update()
    clock.tick(FPS)


pygame.quit()
