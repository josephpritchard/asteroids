from circleshape import *
from constants import *
from logger import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
       super().__init__(x, y, radius)
       self.x = x
       self.y = y

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
        self.dt = dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            rand_angle = random.uniform(20, 50)
            new_vel = self.velocity.rotate(rand_angle)
            new_vel2 = self.velocity.rotate(-rand_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid.velocity = new_vel * 1.2
            new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid2.velocity = new_vel2 * 1.2
