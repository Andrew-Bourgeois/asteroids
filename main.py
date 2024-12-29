# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *

def main():
    pygame.init()

    # create new GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # create Clock object
    clock = pygame.time.Clock()

    # isntantiate player object
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    # create an infinite loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # fill screen with black
        screen.fill("black")

        # check input and update
        player.update(dt)

        # draw player (need to draw this between black fill and updating screen 'flip')
        player.draw(screen)

        # flip the screen (print to screen)
        pygame.display.flip()

        # call the tick() method to wait 1/60th of a second
        # store returned time in milliseconds to dt
        dt = clock.tick(60) / 1000


    # print("Starting asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()