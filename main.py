import pygame
import sys
from logger import log_state, log_event
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def print_startup():
    print("Hello from asteroids!")
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


def initialize_game():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    return screen


def run_loop(screen):
    #
    clock = pygame.time.Clock()
    dt = 0 # delta time
    fps = 60
    #
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    #
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    Player.containers = (updatable, drawable)
    #
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill('black')
        # update objects
        for obj in updatable: obj.update(dt)
        for obj in drawable: obj.draw(screen)
        # check for collision to player
        for ast in asteroids:
            if ast.collides_with(player):
                log_event("player_hit")
                print("Game Over!")
                sys.exit(0)
            for shot in shots:
                if shot.collides_with(ast):
                    log_event("asteroid_shot")
                    shot.kill()
                    ast.split()
        #
        pygame.display.flip()
        dt = clock.tick(fps) / 1000


def main():
    print_startup()
    screen = initialize_game()
    run_loop(screen)


if __name__ == "__main__":
    main()
