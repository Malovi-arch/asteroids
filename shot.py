import pygame

from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y):
        radius = SHOT_RADIUS
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
    
    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)