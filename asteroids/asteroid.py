from circleshape import *
from constants import *
from logger import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, color):
       super().__init__(x, y, radius)
       self.x = x
       self.y = y
       self.color = color

       color = "white"

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
        self.dt = dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            if self.color == "white":
                color = "orange"
            else:
                color = "red"

            log_event("asteroid_split")
            rand_angle = random.uniform(20, 50)
            new_vel = self.velocity.rotate(rand_angle) * 2
            new_vel2 = self.velocity.rotate(-rand_angle) * 2
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid = Asteroid(self.position.x, self.position.y, new_radius, color)
            new_asteroid.velocity = new_vel * 1.2
            new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius, color)
            new_asteroid2.velocity = new_vel2 * 1.2
