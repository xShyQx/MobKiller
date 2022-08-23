import pygame
from pygame import Vector2

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

        self._allSprites = pygame.sprite.Group()
        self._player = Player(Vector2(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2), PLAYER_SIZE)
        self._allSprites.add(self._player)

    def isRunning(self):
        return self._isRunning

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._isRunning = False

        self._allSprites.update()

    def render(self):
        self._window.fill((255, 255, 255))
        self._allSprites.draw(self._window)
        pygame.display.update()