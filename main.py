# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys

from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    background_image = pygame.image.load("./stockvault-space199150.jpg").convert()
    background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

    fps_clock = pygame.time.Clock()

    dt = 0
    player_score = 0
    player_lives = 3
    player_status = "alive"

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    player1 = Player(x, y, 2)

    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable)

    Shot.containers = (shots, updatable, drawable)

    field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = fps_clock.tick(60) / 1000.0

        screen.blit(background_image, (0, 0))
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collision(player1):
                player1.kill()
                player_status = "dead"
                player_lives -= 1
                if player_status == "dead" and player_lives == 0:
                    print("Game over!")
                    print(f"Your score was {player_score}!")
                    sys.exit()
                else:
                    player_status = "alive"
                    player1 = Player(x, y, 2)
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collision(shot):
                    asteroid.split()
                    shot.kill()
                    player_score += 10
        for member in drawable:
            if member in shots:
                continue
            if member.position.x > SCREEN_WIDTH:
                member.position.x = 0
            elif member.position.x < 0:
                member.position.x = SCREEN_WIDTH
        for member in drawable:
            if member in shots:
                continue
            if member.position.y > SCREEN_WIDTH:
                member.position.y = 0
            elif member.position.y < 0:
                member.position.y = SCREEN_WIDTH
        for member in drawable:
            member.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()
