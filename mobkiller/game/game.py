import pygame
from pygame import Vector2

from mobkiller.game.objects.camera import Camera
from mobkiller.game.objects.background import Background
from mobkiller.game.objects.player import Player
from mobkiller.globals import (
    PLAYER_BASE_SPEED,
    WINDOW_HEIGHT,
    WINDOW_WIDTH,
    PLAYER_SIZE,
    UP,
    LEFT,
    DOWN,
    RIGHT
)

class Game:
    def __init__(self):
        self._window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self._isRunning = True
        pygame.display.set_caption("Mob Killer")

        self._bg = Background()
        self._player = Player(Vector2(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2), PLAYER_SIZE, (0, 255, 0))
        self._playerSpeed = PLAYER_BASE_SPEED

        self._allSprites = pygame.sprite.Group()
        self._allSprites.add(self._bg)
        self._allSprites.add(self._player)

        self._camera = Camera(self._player, self._bg)
        self._camera.add(self._bg)

    def isRunning(self):
        return self._isRunning

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._isRunning = False

        self._camera.update()

    def render(self):
        self._allSprites.draw(self._window)
        pygame.display.update()