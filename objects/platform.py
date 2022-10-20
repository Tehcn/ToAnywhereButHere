import pygame

from objects.game_object import GameObject
from window import Window


class Platform(GameObject):
    def __init__(self, window: Window) -> None:
        self.color = (255, 50, 50)
        super().__init__()
        self.window = window
        self.surface = pygame.Surface((self.window.WIDTH, 20))
        self.surface.fill(self.color)
        self.rect = self.surface.get_rect(
            center=(self.window.WIDTH / 2, self.window.HEIGHT - 10))
