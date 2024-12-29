from circleshape import *
from constants import *

# Player class
class Player(CircleShape):
    def __init__(self, x, y):
        # parent class constructor
        super().__init__(x, y, PLAYER_RADIUS)

        # class specific properties
        self.rotation = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        points = self.triangle()
        pygame.draw.polygon(screen, "white", points, 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        """
        Player movement math:
        1. draw a unit vector from (0,0) to (0,1)
        2. Rotate the vector to player's rotation
        3. multiply PLAYER_SPEED * dt (a larger vector means faster movement)
        4. Add vector to current postion
        """
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed() # gets the pressed keys

        if keys[pygame.K_LEFT]:
            # rotate to the left
            self.rotate(-dt)
        if keys[pygame.K_RIGHT]:
            # rotate to the right
            self.rotate(dt)
        if keys[pygame.K_UP]:
            # move forward
            self.move(dt)
        if keys[pygame.K_DOWN]:
            # move backward
            self.move(-dt)
        