from typing_extensions import Self
from typing import List
import pygame


class GameObject(pygame.sprite.Sprite):
    game_objects: List[Self] = []

    def __init__(self) -> None:
        super().__init__()
        self.color = self.color if self.color else (255, 255, 255)
        GameObject.game_objects.append(self)
