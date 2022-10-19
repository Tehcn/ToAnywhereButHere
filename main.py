import pygame
from pygame.locals import *

from game import Game
from window import Window
from events.event_handler import EventHandler


def main():
    pygame.init()
    vec = pygame.math.Vector2

    window = Window("ToAnywhereButHere", (800, 600), 60)
    game = Game(window, 0.5, -0.12)

    while game.running:
        EventHandler.handle_all()


if __name__ == "__main__":
    main()
