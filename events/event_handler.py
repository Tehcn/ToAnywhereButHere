import pygame
from typing import Callable, List
from typing_extensions import Self


class EventHandler:
    handlers: List[Self] = []

    def __init__(self, event_type, handler: Callable[[pygame.event.Event], None]) -> None:
        self.event_type = event_type
        self.handler = handler
        EventHandler.handlers.append(self)

    @staticmethod
    def handle_all():
        for event in pygame.event.get():
            for handler in EventHandler.handlers:
                if event.type == handler.event_type:
                    handler.handler(event)
