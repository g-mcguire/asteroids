import pygame, random
from constants import *
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20.0, 50.0)
        vector_a = self.velocity.rotate(random_angle)
        vector_b = self.velocity.rotate(random_angle * -1)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        subasteroid_a = Asteroid(self.position.x, self.position.y, new_radius)
        subasteroid_b = Asteroid(self.position.x, self.position.y, new_radius)

        subasteroid_a.velocity = vector_a * SUBASTEROID_ACCEL
        subasteroid_b.velocity = vector_b * SUBASTEROID_ACCEL
