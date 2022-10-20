import pygame
from pygame.locals import KEYDOWN, QUIT
from typing import Callable
from events.event_handler import EventHandler


def register_handlers():
    # def keydown_handler_func(event: pygame.event.Event) -> None:
    #     print(f"key pressed: {event.unicode}")

    # EventHandler(KEYDOWN, keydown_handler_func)

    def quit_handler(event: pygame.event.Event) -> None:
        import sys
        pygame.quit()
        sys.exit()

    EventHandler(QUIT, quit_handler)
