import pygame
import sys
from asteroidfield import *
from constants import *
from asteroid import *
from player import *
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids ,updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots,updatable,drawable)
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField() 
    

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    while True:

        
        dt = (clock.tick()/(1000))
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.check_collision(player):
                print("Game Over")
                sys.exit()
            for shot in shots:
                if shot.check_collision(asteroid):
                    asteroid.split()
             
             
        screen.fill("black")
        for draw in drawable:
            draw.draw(screen)
        
      
        pygame.display.flip()




if __name__ == "__main__":
    main()  