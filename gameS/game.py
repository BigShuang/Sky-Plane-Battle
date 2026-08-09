import pygame

from enemy import Enemy
from player import Player
from settings import (
    ADD_ENEMY_EVENT,
    ADD_ENEMY_INTERVAL,
    BACKGROUND_COLOR,
    FPS,
    PLAYING,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    SHOOT_EVENT,
    SHOOT_INTERVAL,
)


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Sky Plane Battle v1.3")
    clock = pygame.time.Clock()
    pygame.time.set_timer(ADD_ENEMY_EVENT, ADD_ENEMY_INTERVAL)
    # TODO 3.2：按照配置的时间间隔注册自动射击事件。
    pygame.time.set_timer(SHOOT_EVENT, SHOOT_INTERVAL)

    player = Player()
    enemies = []
    # TODO 3.2：创建用于管理所有子弹的列表。
    bullets = []
    game_state = PLAYING
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # 仅在 PLAYING 状态下响应敌机生成事件。
            if game_state == PLAYING and event.type == ADD_ENEMY_EVENT:
                enemies.append(Enemy())

            # TODO 3.2：仅在 PLAYING 状态下响应射击事件，
            # 调用 player.shoot() 产生子弹对象，并将返回的子弹加入列表。
            if game_state == PLAYING and event.type == SHOOT_EVENT:
                bullets.append(player.shoot())

        keys = pygame.key.get_pressed()
        player.update(keys)

        for enemy in enemies:
            enemy.update()

        # TODO 3.2：逐一更新所有子弹的位置。
        for bullet in bullets:
            bullet.update()

        enemies = [enemy for enemy in enemies if not enemy.is_out_of_screen()]

        # TODO 3.2：过滤子弹列表，清理已经完全飞出屏幕上方的子弹。
        bullets = [bullet for bullet in bullets if not bullet.is_out_of_screen()]

        # TODO 3.3：使用矩形碰撞检测子弹与敌机，记录命中的子弹和敌机
        hit_enemies = []
        hit_bullets = []
        for bullet in bullets:
            for enemy in enemies:
                # 检查 bullet 的矩形对象 碰撞到了 enemy 的矩形对象
                # 如果碰撞到了，就记录到对应的列表中，并停止检测该子弹。
                if enemy not in hit_enemies and bullet.rect.colliderect(enemy.rect):
                    hit_bullets.append(bullet)
                    hit_enemies.append(enemy)
                    break


        # TODO 3.3：统一过滤列表，使命中的子弹和敌机消失。
        bullets = [bullet for bullet in bullets if bullet not in hit_bullets]
        enemies = [enemy for enemy in enemies if enemy not in hit_enemies]

        screen.fill(BACKGROUND_COLOR)
        for enemy in enemies:
            enemy.draw(screen)

        # TODO 3.2：逐一绘制子弹列表中的所有子弹。
        for bullet in bullets:
            bullet.draw(screen)


        player.draw(screen)
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
