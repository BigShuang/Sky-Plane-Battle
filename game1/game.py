import pygame

from player import Player
from settings import BACKGROUND_COLOR, FPS, SCREEN_HEIGHT, SCREEN_WIDTH


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Sky Plane Battle v1.1")
    clock = pygame.time.Clock()

    player = Player()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        player.update(keys)

        screen.fill(BACKGROUND_COLOR)
        player.draw(screen)
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()

