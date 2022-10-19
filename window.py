import pygame
from typing import Tuple


class Window:
    def __init__(self, name: str, resolution: Tuple[int, int], target_fps: int) -> int:
        self.resolution = resolution
        self.display = pygame.display.set_mode((resolution[0], resolution[1]))
        self.target_fps = target_fps
        self.cfps = pygame.time.Clock()
        pygame.display.set_caption(name)
