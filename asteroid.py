import pygame
import random
from logger import log_event
from constants import * 
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
       self.position += self.velocity * dt 

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        smaller_radius = self.radius - ASTEROID_MIN_RADIUS
        ast_1 = Asteroid(self.position.x, self.position.y, smaller_radius)
        ast_2 = Asteroid(self.position.x, self.position.y, smaller_radius)
        #
        rand_angle = random.uniform(20, 50)
        ast_1_velocity = self.velocity.rotate(rand_angle)
        ast_2_velocity = self.velocity.rotate(-rand_angle)
        #
        ast_1.velocity = 1.2 * ast_1_velocity
        ast_2.velocity = 1.2 * ast_2_velocity


