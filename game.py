from window import Window


class Game:
    def __init__(self, window: Window, acceleration: int, friction: int) -> None:
        self.window = window
        self.acceleration = acceleration
        self.friction = friction
        self.running = True
