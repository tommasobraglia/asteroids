# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    #Start screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        screen.fill(BLACK)
        pygame.display.flip()
        pygame.time.delay(100)
if __name__ == "__main__":
    main()