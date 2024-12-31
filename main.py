# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

# ------------- Groups ------------
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()

Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable)
Shot.containers = (shots, updatable, drawable)

def main():
    pygame.init()

    # create new GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # create Clock object
    clock = pygame.time.Clock()

    # instantiate player object
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # create new asteroid field
    asteroid_field = AsteroidField()

    dt = 0 # delta time

    # create an infinite loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # fill screen with black
        screen.fill("black")

        for _ in updatable:
            # check player input and update any groups
            # provide the dt argument
            _.update(dt)

        # check for collisions
        for asteroid in asteroids:
            if asteroid.check_collisions(player):
                exit("GAME OVER!!")
            for shot in shots:
                if asteroid.check_collisions(shot):
                    asteroid.split()
                    shot.kill()


        for _ in drawable:
            # draw any drawables to the screen
            _.draw(screen)

        # flip the screen (print to/update screen)
        pygame.display.flip()

        # call the tick() method to wait 1/60th of a second
        # store returned time in milliseconds to dt
        dt = clock.tick(60) / 1000


    # print("Starting asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()