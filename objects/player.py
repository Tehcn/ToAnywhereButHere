import pygame
from pygame.locals import K_w, K_a, K_s, K_d, K_LEFT, K_RIGHT, K_SPACE, K_LCTRL
from constants import ACCELERATION, FRICTION

from objects.game_object import GameObject
from window import Window
from type_aliases import vec


class Player(GameObject):
    def __init__(self, window: Window) -> None:
        self.color = (0, 119, 255)
        super().__init__()
        self.window = window
        self.surface = pygame.Surface((30, 30))
        self.surface.fill(self.color)
        self.rect = self.surface.get_rect(center=(30, 420))

        self.pos = vec(10, 385)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def move(self):
        self.acc = vec(0, 0)

        pressed_keys = pygame.key.get_pressed()

        # left
        if pressed_keys[K_a] or pressed_keys[K_LEFT]:
            self.acc.x -= ACCELERATION
        if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
            self.acc.x += ACCELERATION

        self.acc.x += self.vel.x * FRICTION
        self.vel += self.acc
        self.pos += self.vel + ACCELERATION * self.acc

        # TODO: Make a scrolling camera
        if self.pos.x > self.window.WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = self.window.WIDTH

        self.rect.midbottom = self.pos
