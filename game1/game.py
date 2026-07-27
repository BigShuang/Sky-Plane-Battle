import pygame

from player import Player
from settings import BACKGROUND_COLOR, FPS, SCREEN_HEIGHT, SCREEN_WIDTH


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Sky Plane Battle v1.1")
    clock = pygame.time.Clock()

    # TODO 1.3：创建玩家对象。
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # TODO 1.3：获取当前按键状态，并用它更新玩家。
        # keys = pygame.key.get_pressed()

        screen.fill(BACKGROUND_COLOR)
        # TODO 1.3：将玩家绘制到游戏窗口中。


        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
