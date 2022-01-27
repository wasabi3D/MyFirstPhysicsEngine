import pygame
import sys
from pygame.math import Vector2
from pygame.locals import *


e = 0.854

class TestParticle:
    def __init__(self, mass, position: Vector2, dim):
        self.mass = mass
        self.pos: Vector2 = position
        self.accel: Vector2 = Vector2(0, 0)
        self.old_accel: Vector2 = Vector2(0, 0)
        self.velocity: Vector2 = Vector2(0, 0)
        self.dim = dim

    def update(self, fcs: list[Vector2], delta: float):
        net_force: Vector2 = Vector2(0, 0)
        for f in fcs:
            net_force += f

        if self.pos.x > self.dim[0] or self.pos.x < 0:
            self.pos.x = 0 if self.pos.x < 0 else self.dim[0]
            self.velocity.x = e * self.velocity.x * -1
            print(f"{self.velocity.x=}")
        if self.pos.y > self.dim[1] or self.pos.y < 0:
            self.pos.y = 0 if self.pos.y < 0 else self.dim[1]
            self.velocity.y = e * self.velocity.y * -1
            print(f"{self.velocity.y=}")

        self.old_accel = self.accel
        self.pos += self.velocity * delta + (0.5 * self.old_accel * (delta ** 2))
        self.accel = net_force / self.mass
        average_accel = (self.old_accel + self.accel) / 2
        self.velocity += average_accel * delta

        # self.pos.x = max(0, min(self.dim[0], self.pos.x))
        # self.pos.y = max(0, min(self.dim[1], self.pos.y))

    def draw(self, scr):
        pygame.draw.circle(scr, (50, 50, 50), (self.pos.x, self.pos.y), 10, 4)


d = (800, 800)

screen = pygame.display.set_mode(d)

particle_mass = 15
meter_px = 85
forces: list[Vector2] = [Vector2(0, 9.8 * particle_mass * meter_px)]

particle = TestParticle(particle_mass, Vector2(20, 500), d)

particle.update([Vector2(7800, -9500)], 1)
t = 0
d = 0

while True:
    t = pygame.time.get_ticks()
    screen.fill((230, 230, 230))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == K_UP:
                pass
            elif event.key == K_DOWN:
                pass
            elif event.key == K_RIGHT:
                pass
            elif event.key == K_LEFT:
                pass

    particle.update(forces, d / 1000)
    particle.draw(screen)
    pygame.display.update()
    pygame.time.Clock().tick(120)
    d = pygame.time.get_ticks() - t
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
