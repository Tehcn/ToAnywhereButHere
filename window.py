import pygame
from typing import Tuple
from objects.game_object import GameObject


class Window:
    def __init__(self, name: str, resolution: Tuple[int, int], target_fps: int) -> int:
        self.resolution = resolution
        self.WIDTH = resolution[0]
        self.HEIGHT = resolution[1]
        self.display = pygame.display.set_mode((resolution[0], resolution[1]))
        self.target_fps = target_fps
        self.cfps = pygame.time.Clock()
        pygame.display.set_caption(name)

    def draw(self):
        self.display.fill((0, 0, 0))

        for game_object in GameObject.game_objects:
            self.display.blit(game_object.surface, game_object.rect)

        pygame.display.update()
        self.cfps.tick(self.target_fps)
        # print(self.cfps.get_fps())
