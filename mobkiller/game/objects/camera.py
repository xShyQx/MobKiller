import pygame
from pygame import Vector2

from mobkiller.game.objects.player import Player
from mobkiller.game.objects.background import Background
from mobkiller.globals import (
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    WINDOW_CENTER
)

class Camera(pygame.sprite.Group):
    def __init__(self, bg: Background):
        super().__init__()
        self._bg = bg
        self._offset = Vector2()

    def centerTarget(self, target: Player):
        self._offset.x = target.rect.centerx - WINDOW_CENTER[0]
        if self._offset.x < self._bg.rect.left:
            self._offset.x = self._bg.rect.left
        if self._offset.x > self._bg.rect.right - WINDOW_WIDTH:
            self._offset.x = self._bg.rect.right - WINDOW_WIDTH

        self._offset.y = target.rect.centery - WINDOW_CENTER[1]
        if self._offset.y < self._bg.rect.top:
            self._offset.y = self._bg.rect.top
        if self._offset.y > self._bg.rect.bottom - WINDOW_HEIGHT:
            self._offset.y = self._bg.rect.bottom - WINDOW_HEIGHT

    def draw(self, surf: pygame.Surface):
        surf.blit(self._bg.image, self._bg.rect.topleft - self._offset)
        for sprite in self.sprites():
            surf.blit(sprite.image, sprite.rect.topleft - self._offset)