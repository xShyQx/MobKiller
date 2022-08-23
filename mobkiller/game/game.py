import pygame

from mobkiller.game.objects.player import Player
from mobkiller.globals import (
    WINDOW_HEIGHT,
    WINDOW_WIDTH,
    PLAYER_SIZE
)

class Game:
    def __init__(self):
        self._window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self._isRunning = True
        pygame.display.set_caption("Mob Killer")

        self._player = Player((WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2), PLAYER_SIZE)

    def isRunning(self):
        return self._isRunning

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._isRunning = False

    def render(self):
        self._window.fill((255, 255, 255))
        self._window.blit(self._player.image, self._player.rect.topleft)
        pygame.display.update()