import pygame

from enemy import Enemy
from player import Player
from settings import (
    ADD_ENEMY_EVENT,
    ADD_ENEMY_INTERVAL,
    BACKGROUND_COLOR,
    FPS,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
)


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Sky Plane Battle v1.2")
    clock = pygame.time.Clock()
    pygame.time.set_timer(ADD_ENEMY_EVENT, ADD_ENEMY_INTERVAL)

    player = Player()
    enemies = []
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == ADD_ENEMY_EVENT:
                enemies.append(Enemy())

        keys = pygame.key.get_pressed()
        player.update(keys)

        for enemy in enemies:
            enemy.update()
        enemies = [enemy for enemy in enemies if not enemy.is_out_of_screen()]

        screen.fill(BACKGROUND_COLOR)
        for enemy in enemies:
            enemy.draw(screen)
        player.draw(screen)

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
