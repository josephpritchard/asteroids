import pygame, sys
from constants import *
from player import *
from logger import log_state, log_event
from asteroidfield import AsteroidField
from asteroid import *
from shot import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    af = AsteroidField()

    Shot.containers = (shots, updatable, drawable)

    while True:
        log_state()

        for event in pygame.event.get():
            pass

        screen.fill("black")
        updatable.update(dt)
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()

        for roid in asteroids:
            if Asteroid.collides_with(roid, player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for shot in shots:  
                if Shot.collides_with(roid, shot):
                    log_event("asteroid_shot")
                    roid.split()
                    shot.kill()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
