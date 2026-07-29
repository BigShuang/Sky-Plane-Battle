import pygame

from enemy import Enemy
from player import Player
from settings import (
    ADD_ENEMY_EVENT,
    ADD_ENEMY_INTERVAL,
    BACKGROUND_IMAGE,
    BACKGROUND_SPEED,
    CURRENT_LANGUAGE,
    ENEMY_EXPLOSION_SOUND,
    ENEMY_EXPLOSION_VOLUME,
    FPS,
    GAME_MUSIC,
    GAME_MUSIC_VOLUME,
    LIGHT_GRAY,
    PLAYER_EXPLOSION_SOUND,
    PLAYER_EXPLOSION_VOLUME,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    SHOOT_EVENT,
    SHOOT_INTERVAL,
    START_MUSIC,
    START_MUSIC_VOLUME,
    STATUS_GAME_OVER,
    STATUS_PLAYING,
    STATUS_START,
    WHITE,
    YELLOW,
    get_text,
)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background_image = pygame.image.load(BACKGROUND_IMAGE).convert()
background_y = 0
clock = pygame.time.Clock()
title_font = pygame.font.SysFont("Microsoft YaHei", 56)
normal_font = pygame.font.SysFont("Microsoft YaHei", 28)
pygame.display.set_caption(get_text(CURRENT_LANGUAGE, "caption"))
pygame.time.set_timer(ADD_ENEMY_EVENT, ADD_ENEMY_INTERVAL)
pygame.time.set_timer(SHOOT_EVENT, SHOOT_INTERVAL)

enemy_explosion_sound = pygame.mixer.Sound(ENEMY_EXPLOSION_SOUND)
player_explosion_sound = pygame.mixer.Sound(PLAYER_EXPLOSION_SOUND)
enemy_explosion_sound.set_volume(ENEMY_EXPLOSION_VOLUME)
player_explosion_sound.set_volume(PLAYER_EXPLOSION_VOLUME)


def play_music(filename, volume):
    """循环播放背景音乐"""
    pygame.mixer.music.load(filename)
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play(-1)


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
    height = background_image.get_height()
    screen.blit(background_image, (0, background_y))
    screen.blit(background_image, (0, background_y - height))
    for enemy in enemies:
        enemy.draw(screen)
    for bullet in bullets:
        bullet.draw(screen)
    player.draw(screen)
    score_text = get_text(CURRENT_LANGUAGE, "score", score=score)
    draw_text_topright(
        score_text,
        normal_font,
        WHITE
    )


def reset_game():
    """重新开始一局游戏"""
    return Player(), [], [], 0


def is_mask_collision(sprite1, sprite2):
    """精细碰撞判定： 判断两张图片的非透明部分是否碰撞"""
    offset_x = sprite2.rect.x - sprite1.rect.x
    offset_y = sprite2.rect.y - sprite1.rect.y
    return sprite1.mask.overlap(sprite2.mask, (offset_x, offset_y)) is not None


def main():
    global background_y
    # 调用 reset_game() 创建首局数据，并将初始状态设为 STATUS_START。
    player, enemies, bullets, score = reset_game()
    game_state = STATUS_START
    play_music(START_MUSIC, START_MUSIC_VOLUME)

    running = True
    while running:
        if game_state != STATUS_GAME_OVER:
            background_y += BACKGROUND_SPEED
            if background_y >= background_image.get_height():
                background_y = 0

        # 3. 处理退出事件
        for event in pygame.event.get():
            # 收到退出事件时结束主循环。
            if event.type == pygame.QUIT:
                running = False

            # 重置游戏数据并进入 STATUS_PLAYING。
            if event.type == pygame.KEYDOWN:
                if game_state == STATUS_START or game_state == STATUS_GAME_OVER:
                    play_music(GAME_MUSIC, GAME_MUSIC_VOLUME)
                    player, enemies, bullets, score = reset_game()
                    game_state = STATUS_PLAYING
            if game_state == STATUS_PLAYING and event.type == ADD_ENEMY_EVENT:
                enemies.append(Enemy())
            if game_state == STATUS_PLAYING and event.type == SHOOT_EVENT:
                bullets.append(player.shoot())

        if game_state == STATUS_START:
            draw_game_screen(player, enemies, bullets, score)
            title_text = get_text(CURRENT_LANGUAGE, "title")
            prompt_text = get_text(CURRENT_LANGUAGE, "start_prompt")
            draw_text(title_text, title_font, WHITE, (SCREEN_WIDTH / 2, 300))
            draw_text(prompt_text, normal_font, LIGHT_GRAY, (SCREEN_WIDTH / 2, 390))
            pygame.display.update()
            clock.tick(FPS)
            continue  # 使用 continue 跳过后续战斗逻辑。

        # TODO 4.3：处理并绘制结束时的画面（即游戏状态为结束），显示游戏结束、最终得分和重新开始提示；
        # 刷新画面、限制帧率，并使用 continue 跳过战斗逻辑。
        if game_state == STATUS_GAME_OVER:
            draw_game_screen(player, enemies, bullets, score)
            game_over_text = get_text(CURRENT_LANGUAGE, "game_over")
            final_score_text = get_text(CURRENT_LANGUAGE, "final_score", score=score)
            restart_text = get_text(CURRENT_LANGUAGE, "restart_prompt")
            draw_text(game_over_text, title_font, WHITE, (SCREEN_WIDTH / 2, 300))
            draw_text(final_score_text, normal_font, LIGHT_GRAY, (SCREEN_WIDTH / 2, 390))
            draw_text(restart_text, normal_font, YELLOW, (SCREEN_WIDTH / 2, 450))
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
                if enemy in hit_enemies:
                    continue
                if bullet.rect.colliderect(enemy.rect):
                    hit_bullets.append(bullet)
                    hit_enemies.append(enemy)
                    score += 10
                    enemy_explosion_sound.play()
                    break
        bullets = [bullet for bullet in bullets if bullet not in hit_bullets]
        enemies = [enemy for enemy in enemies if enemy not in hit_enemies]

        # 6. 检查玩家是否撞到敌人
        for enemy in enemies:
            if is_mask_collision(player, enemy):
                player_explosion_sound.play()
                pygame.mixer.music.stop()
                game_state = STATUS_GAME_OVER
                break

        # 7. 绘制画面
        draw_game_screen(player, enemies, bullets, score)
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
