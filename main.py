# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys

from constants import *
from player import *
from asteroid import *
from asteroidfield import * 

def main():
    pygame.init()
    fpsclock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT /2

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (updateable, drawable, asteroids)
    AsteroidField.containers = (updateable)
    Shot.containers = (updateable, drawable, shots)

    # Create a list of asteroids
    myplayer = Player(x,y)
    myAsteroidField = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill(pygame.Color("black"))
        # draw player here

        updateable.update(dt)
        
        for asteroid in asteroids:
            if myplayer.collisions(asteroid):
                print("Game over!")
                sys.exit()
                # Handle collision (e.g., end game, reduce health, etc.)
            for shot in shots:
                if shot.collisions(asteroid):
                    asteroid.split()  
        
        for sprite in drawable:
            sprite.draw(screen)
        #myplayer.draw(screen)

        pygame.display.flip()
        dt = fpsclock.tick(60) / 1000
    

if __name__ == "__main__":
    main()