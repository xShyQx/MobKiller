import pygame
from pygame import Vector2

from random import randint

from mobkiller.game.objects.camera import Camera
from mobkiller.game.objects.background import Background
from mobkiller.game.objects.player import Player
from mobkiller.game.objects.enemy import Enemy
from mobkiller.globals import (
    ENEMY_SIZE,
    WINDOW_CENTER,
    WINDOW_HEIGHT,
    WINDOW_WIDTH
)

class Game:
    def __init__(self):
        self._window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Mob Killer")
        self._clock = pygame.time.Clock()
        self._isRunning = True
        
        self._bg = Background()
        self._player = Player()
        Player.borders = self._bg.rect
        self._enemySprites = pygame.sprite.Group()

        self._camera = Camera(self._bg)
        self._camera.add(self._player)

        for _ in range(20):
            enemy = self.spawnEnemy()
            self._enemySprites.add(enemy)
            self._camera.add(enemy)

    def isRunning(self):
        return self._isRunning

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._isRunning = False

        self._player.update()
        self._camera.centerTarget(self._player)
        self.checkCollisions()

    def render(self):
        self._camera.draw(self._window)
        pygame.display.update()
        
        self._clock.tick(60)

    def reset(self):
        print("haha cringe")
        self._player.reset()

    def spawnEnemy(self):
        randX = randint(int(self._bg.rect.left + (ENEMY_SIZE.x / 2)), int(self._bg.rect.right - (ENEMY_SIZE.x / 2)))
        randY = randint(int(self._bg.rect.top + (ENEMY_SIZE.y / 2)), int(self._bg.rect.bottom - (ENEMY_SIZE.y / 2)))
        return Enemy((randX, randY))

    def checkCollisions(self):
        for sprite in pygame.sprite.spritecollide(self._player, self._enemySprites, False):
            if not self._player.isAttacking:
                self.reset()
                return
                
            if ((self._player.faceDirection == "left"
                and sprite.rect.right >= self._player.rect.left
                and sprite.rect.right <= self._player.rect.right)
                or (self._player.faceDirection == "right"
                and sprite.rect.left <= self._player.rect.right
                and sprite.rect.left >= self._player.rect.left)):
                sprite.kill()
            else:
                self.reset()