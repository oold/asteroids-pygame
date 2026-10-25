import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float):
        super().__init__(x, y, radius)

    def draw(self, screen) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        new_velocity_1 = self.velocity.rotate(angle)
        new_velocity_2 = self.velocity.rotate(-angle)
        radius = self.radius - ASTEROID_MIN_RADIUS
        a1 = Asteroid(self.position.x, self.position.y, radius)
        a1.velocity = new_velocity_1 * 1.2
        a2 = Asteroid(self.position.x, self.position.y, radius)
        a2.velocity = new_velocity_2 * 1.2
