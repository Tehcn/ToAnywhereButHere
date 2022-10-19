import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.surface = pygame.Surface((30, 30))
        self.surface.fill((0, 119, 255))
