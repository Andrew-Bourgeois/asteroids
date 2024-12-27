# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    pygame.init()

    # create new GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # create an infinite loop
    while True:
        screen.fill("black")
        pygame.display.flip()

    # print("Starting asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()