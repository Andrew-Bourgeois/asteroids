from circleshape import *
from constants import *
import random
# import random

# colors = ["blue", "red", "white", "green", "yellow", "orange", "purple"]

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def split(self):
        # kill current asteroid
        self.kill()

        # if min radius then return, else spawn (@) asteroids the next size down
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            new_angle = random.uniform(20, 50)
            asteroid_1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            asteroid_1.velocity = self.velocity.rotate(new_angle) * 2
            
            asteroid_2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            asteroid_2.velocity = self.velocity.rotate(-new_angle) * 2


    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)


    def update(self, dt):
        self.position += self.velocity * dt
