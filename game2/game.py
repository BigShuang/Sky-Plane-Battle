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
    # 按照配置的时间间隔注册敌机生成事件。
    pygame.time.set_timer(ADD_ENEMY_EVENT, ADD_ENEMY_INTERVAL)

    player = Player()
    # TODO 2.2：创建用于管理所有敌机的列表。
    # enemies = []
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # TODO 2.2：收到敌机生成事件时，创建一个 Enemy 并加入敌机列表。
            # if event.type == ADD_ENEMY_EVENT:
            #     do something

        keys = pygame.key.get_pressed()
        player.update(keys)

        # TODO 2.2：逐一更新所有敌机的位置。

        # TODO 2.2：过滤敌机列表，清理已经完全飞出屏幕底部的敌机。
        # enemies = [enemy for enemy in enemies if ... ]

        screen.fill(BACKGROUND_COLOR)
        # TODO 2.2：逐一绘制敌机列表中的所有敌机。


        player.draw(screen)
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
