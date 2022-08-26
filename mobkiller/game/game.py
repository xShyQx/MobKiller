import pygame
from pygame import Vector2

from mobkiller.game.objects.cameraSprites import CameraSprites
from mobkiller.game.objects.player import Player
from mobkiller.globals import (
    WINDOW_HEIGHT,
    WINDOW_WIDTH,
    PLAYER_SIZE
)

class Game:
    def __init__(self):
        self._window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self._bg = pygame.image.load("bg.png")
        self._isRunning = True
        pygame.display.set_caption("Mob Killer")

        self._cameraSprites = CameraSprites()
        self._player = Player(Vector2(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2), PLAYER_SIZE, self._cameraSprites, (0, 255, 0))

    def isRunning(self):
        return self._isRunning

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._isRunning = False

        self._cameraSprites.update()

    def render(self):
        self._cameraSprites.draw()
        pygame.display.update()