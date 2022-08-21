import pygame

from mobkiller.globals import (
    WINDOW_HEIGHT,
    WINDOW_WIDTH
)

class Game:
    def __init__(self):
        self._window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self._isRunning = True
        pygame.display.set_caption("Mob Killer")

    def isRunning(self):
        return self._isRunning

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._isRunning = False

    def render(self):
        pygame.display.update()