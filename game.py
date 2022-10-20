import pygame
from typing import List
from objects.platform import Platform
from objects.player import Player
from window import Window
from events import event_handlers


class Game:
    def __init__(self, window: Window) -> None:
        self.window = window
        self.running = True
        self.player = Player(window)
        self.platforms: List[Platform] = []
        self.platforms.append(Platform(window))
        event_handlers.register_handlers()

    def update(self):
        self.player.move()
