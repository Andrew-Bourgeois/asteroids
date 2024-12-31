from circleshape import *
from constants import *
# import random

# colors = ["blue", "red", "white", "green", "yellow", "orange", "purple"]

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt