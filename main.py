import pygame
from pygame.locals import *
from game import Game
from window import Window
from events.event_handler import EventHandler


def main():
    pygame.init()

    window = Window("ToAnywhereButHere", (1280, 720), 60)
    game = Game(window)

    while game.running:
        EventHandler.handle_all()
        game.update()
        window.draw()


if __name__ == "__main__":
    main()
