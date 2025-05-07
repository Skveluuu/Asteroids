import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0 
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    while True:
        for event in pygame.event.get():
                delta_time = pygame.time.clock.tick(60)
                dt = (delta_time/1000)
                if event.type == pygame.QUIT:
                    return
        screen.fill("black")
        pygame.display.flip()



if __name__ == "__main__":
    main()  