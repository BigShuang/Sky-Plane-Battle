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


def draw_text_topright(text, font, color, topright):
    """在指定右上角位置绘制文字"""
    text_image = font.render(text, True, color)
    text_rect = text_image.get_rect(topright=topright)
    screen.blit(text_image, text_rect)


def draw_game_screen(player, enemies, bullets, score):
    """绘制游戏画面"""
    screen.fill(BACKGROUND_COLOR)
    for enemy in enemies:
        enemy.draw(screen)
    for bullet in bullets:
        bullet.draw(screen)
    player.draw(screen)
    draw_text_topright(
        get_text(CURRENT_LANGUAGE, "score", score=score),
        normal_font,
        WHITE,
        (SCREEN_WIDTH - 20, 15),
    )


def reset_game():
    """重新开始一局游戏"""
    return Player(), [], [], 0


def is_mask_collision(sprite1, sprite2):
    """判断两张图片的非透明部分是否碰撞"""
    offset_x = sprite2.rect.x - sprite1.rect.x
    offset_y = sprite2.rect.y - sprite1.rect.y
    return sprite1.mask.overlap(sprite2.mask, (offset_x, offset_y)) is not None


def main():
    # 2. 游戏状态
    player, enemies, bullets, score = reset_game()
    game_state = STATUS_START

    running = True
    while running:
        # 3. 处理退出事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if game_state == STATUS_START or game_state == STATUS_GAME_OVER:
                    player, enemies, bullets, score = reset_game()
                    game_state = STATUS_PLAYING
            if game_state == STATUS_PLAYING and event.type == ADD_ENEMY_EVENT:
                enemies.append(Enemy())
            if game_state == STATUS_PLAYING and event.type == SHOOT_EVENT:
                bullets.append(player.shoot())

        if game_state == STATUS_START:
            draw_game_screen(player, enemies, bullets, score)
            draw_text(get_text(CURRENT_LANGUAGE, "title"), title_font, WHITE, (SCREEN_WIDTH / 2, 300))
            draw_text(
                get_text(CURRENT_LANGUAGE, "start_prompt"),
                normal_font,
                LIGHT_GRAY,
                (SCREEN_WIDTH / 2, 390),
            )
            pygame.display.update()
            clock.tick(FPS)
            continue

        if game_state == STATUS_GAME_OVER:
            draw_game_screen(player, enemies, bullets, score)
            draw_text(get_text(CURRENT_LANGUAGE, "game_over"), title_font, WHITE, (SCREEN_WIDTH / 2, 280))
            draw_text(
                get_text(CURRENT_LANGUAGE, "final_score", score=score),
                normal_font,
                YELLOW,
                (SCREEN_WIDTH / 2, 370),
            )
            draw_text(
                get_text(CURRENT_LANGUAGE, "restart_prompt"),
                normal_font,
                LIGHT_GRAY,
                (SCREEN_WIDTH / 2, 440),
            )
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
                game_state = STATUS_GAME_OVER
                break

        # 7. 绘制画面
        draw_game_screen(player, enemies, bullets, score)
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
