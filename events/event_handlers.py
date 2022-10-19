import pygame
from typing import Callable
from events.event_handler import EventHandler


class KeyDownHandler(EventHandler):
    def __init__(self, event: pygame.event.Event, handler: Callable[[pygame.event.Event], None]) -> None:
        super().__init__(event, handler)
