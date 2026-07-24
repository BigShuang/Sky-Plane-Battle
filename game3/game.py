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
    pygame.time.set_timer(SHOOT_EVENT, SHOOT_INTERVAL)

    player = Player()
    enemies = []
    bullets = []
    game_state = PLAYING
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if game_state == PLAYING and event.type == ADD_ENEMY_EVENT:
                enemies.append(Enemy())
            if game_state == PLAYING and event.type == SHOOT_EVENT:
                bullets.append(player.shoot())

        keys = pygame.key.get_pressed()
        player.update(keys)

        for enemy in enemies:
            enemy.update()
        for bullet in bullets:
            bullet.update()

        enemies = [enemy for enemy in enemies if not enemy.is_out_of_screen()]
        bullets = [bullet for bullet in bullets if not bullet.is_out_of_screen()]

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

        screen.fill(BACKGROUND_COLOR)
        for enemy in enemies:
            enemy.draw(screen)
        for bullet in bullets:
            bullet.draw(screen)
        player.draw(screen)
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()

