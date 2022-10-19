import pygame
from typing import Callable, List
from typing_extensions import Self


class EventHandler:
    handlers: List[Self] = []

    def __init__(self, event: pygame.event.Event, handler: Callable[[pygame.event.Event], None]) -> None:
        self.event = event
        self.handler = handler
        EventHandler.handlers.append(self)

    def handle_all():
        for event in pygame.event.poll():
            pass
