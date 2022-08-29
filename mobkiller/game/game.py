import pygame
from pygame import Vector2

from random import randint

from mobkiller.game.objects.camera import Camera
from mobkiller.game.objects.background import Background
from mobkiller.game.objects.player import Player
from mobkiller.game.objects.enemy import Enemy
from mobkiller.globals import (
    ENEMY_SIZE,
    WINDOW_HEIGHT,
    WINDOW_WIDTH
)

class Game:
    def __init__(self):
        self._window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self._isRunning = True
        pygame.display.set_caption("Mob Killer")

        self._bg = Background()
        self._player = Player(Vector2(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

        self._allSprites = pygame.sprite.Group()
        self._allSprites.add(self._bg)
        self._allSprites.add(self._player)

        self._camera = Camera(self._player, self._bg)
        self._camera.add(self._bg)

        for _ in range(5):
            self.addEnemy()

    def addEnemy(self):
        enemy = self.spawnEnemy()
        self._allSprites.add(enemy)
        self._camera.add(enemy)

    def spawnEnemy(self):
        randX = randint(int(self._bg.rect.left + (ENEMY_SIZE.x / 2)), int(self._bg.rect.right - (ENEMY_SIZE.x / 2)))
        randY = randint(int(self._bg.rect.top + (ENEMY_SIZE.y / 2)), int(self._bg.rect.bottom - (ENEMY_SIZE.y / 2)))
        return Enemy((randX, randY))

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