import pygame

from enemy import Enemy
from player import Player
from settings import (
    ADD_ENEMY_EVENT,
    ADD_ENEMY_INTERVAL,
    BACKGROUND_COLOR,
    CURRENT_LANGUAGE,
    FPS,
    LIGHT_GRAY,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    SHOOT_EVENT,
    SHOOT_INTERVAL,
    STATUS_GAME_OVER,
    STATUS_PLAYING,
    STATUS_START,
    WHITE,
    YELLOW,
    get_text,
)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
title_font = pygame.font.SysFont("Microsoft YaHei", 56)
normal_font = pygame.font.SysFont("Microsoft YaHei", 28)
pygame.display.set_caption(get_text(CURRENT_LANGUAGE, "caption"))
pygame.time.set_timer(ADD_ENEMY_EVENT, ADD_ENEMY_INTERVAL)
pygame.time.set_timer(SHOOT_EVENT, SHOOT_INTERVAL)

def draw_text(text, font, color, center):
    """在指定中心位置绘制文字"""
    text_image = font.render(text, True, color)
    text_rect = text_image.get_rect(center=center)
    screen.blit(text_image, text_rect)


def draw_text_topright(text, font, color):
    """在指定右上角位置绘制文字"""
    text_image = font.render(text, True, color)
    text_rect = text_image.get_rect(topright=(SCREEN_WIDTH - 20, 15))
    screen.blit(text_image, text_rect)


def draw_game_screen(player, enemies, bullets, score):
    """绘制游戏画面"""
    screen.fill(BACKGROUND_COLOR)
    for enemy in enemies:
        enemy.draw(screen)
    for bullet in bullets:
        bullet.draw(screen)
    player.draw(screen)
    # TODO 4.3：在 PLAYING 界面的右上角绘制当前分数。
    # score_text = get_text(CURRENT_LANGUAGE, "score", score=score)
    # draw_text_topright(
    #     score_text,
    #     normal_font,
    #     WHITE
    # )


def reset_game():
    """重新开始一局游戏"""
    # TODO 4.1：返回新玩家、空敌机列表、空子弹列表和 0 分。
    pass


def is_mask_collision(sprite1, sprite2):
    """判断两张图片的非透明部分是否碰撞"""
    # 计算 sprite2 相对 sprite1 的位置偏移，
    # 再使用 mask.overlap() 判断非透明部分是否重叠。
    offset_x = sprite2.rect.x - sprite1.rect.x
    offset_y = sprite2.rect.y - sprite1.rect.y
    return sprite1.mask.overlap(sprite2.mask, (offset_x, offset_y)) is not None


def main():
    # 调用 reset_game() 创建首局数据，并将初始状态设为 STATUS_START。
    player, enemies, bullets, score = reset_game()
    game_state = STATUS_START

    running = True
    while running:
        # 3. 处理退出事件
        for event in pygame.event.get():
            # 收到退出事件时结束主循环。
            if event.type == pygame.QUIT:
                running = False

            # TODO 4.1：在开始或游戏结束状态按下任意键时，
            # 重置游戏数据并进入 STATUS_PLAYING。
            # if event.type == pygame.KEYDOWN:
            #     if game_state == STATUS_START or game_state == STATUS_GAME_OVER:
            #         

            # TODO 4.1：仅在 STATUS_PLAYING 状态响应敌机生成和射击事件。
            # if game_state == STATUS_PLAYING and event.type == ADD_ENEMY_EVENT:
            pass

        # TODO 4.3：绘制 START 界面的标题和开始提示，刷新画面并限制帧率；
        # if game_state == ?:
        #     先绘制现有的游戏画面：
        # 
        #     再绘制标题和提示文字。
        #     title_text = ?
        #     prompt_text = ?
        #     draw_text(title_text, title_font, WHITE, (SCREEN_WIDTH / 2, 300))
        #     draw_text(prompt_text, normal_font, LIGHT_GRAY, (SCREEN_WIDTH / 2, 390))
        #     pygame.display.update()
        #     clock.tick(FPS)
        #     continue  # 使用 continue 跳过后续战斗逻辑。

        # TODO 4.3：处理并绘制结束时的画面（即游戏状态为结束），显示游戏结束、最终得分和重新开始提示；
        # 刷新画面、限制帧率，并使用 continue 跳过战斗逻辑。
        

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
        # TODO 4.2：每消灭一架敌机增加 10 分。
        hit_enemies = []
        hit_bullets = []
        for bullet in bullets:
            for enemy in enemies:
                if bullet.rect.colliderect(enemy.rect):
                    hit_bullets.append(bullet)
                    hit_enemies.append(enemy)
                    break
        bullets = [bullet for bullet in bullets if bullet not in hit_bullets]
        enemies = [enemy for enemy in enemies if enemy not in hit_enemies]

        # 6. 检查玩家是否撞到敌人
        # TODO 4.2：遍历敌机并对敌机与玩家飞机进行像素级碰撞检测， 要使用is_mask_collision
        # 玩家与敌机碰撞后立即进入 STATUS_GAME_OVER。

        # 7. 绘制画面
        draw_game_screen(player, enemies, bullets, score)
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
