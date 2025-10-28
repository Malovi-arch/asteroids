# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import *
from player import *

def main():
    pygame.init()

    x = SCREEN_WIDTH / 2

    y = SCREEN_HEIGHT / 2

    player1 = Player(x, y, 2)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    BLACK = (0, 0, 0)

    fps_clock = pygame.time.Clock()

    dt = 0

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(BLACK)

        player1.draw(screen)

        pygame.display.flip()

        fps_clock.tick(60)

        dt = (fps_clock.get_time() / 1000)

if __name__ == "__main__":
    main()
