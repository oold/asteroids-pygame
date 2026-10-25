import sys
from typing import cast

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from logger import log_event, log_state
from player import Player
from shot import Shot


def main():
    pygame.init()
    clock =pygame.time.Clock()
    dt = 0.0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    Shot.containers = (updatable, drawable, shots)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for asteroid in asteroids:
            asteroid = cast(Asteroid, asteroid)
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for shot in shots:
                shot = cast(Shot, shot)
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
