import pygame
from pygame import Vector2

from mobkiller.game.objects.drawable import Drawable
from mobkiller.globals import (
    PLAYER_BASE_SPEED,
    WINDOW_HEIGHT,
    WINDOW_WIDTH
)

class Player(Drawable):
    def __init__(self, position: Vector2, size: Vector2, color: pygame.Color = (0, 255, 0)):
        super().__init__(position, size, color)
        self._speed = PLAYER_BASE_SPEED

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self._center.x -= self._speed
            self.rect.centerx = self._center.x
        if keys[pygame.K_RIGHT] and self.rect.right < WINDOW_WIDTH:
            self._center.x += self._speed
            self.rect.centerx = self._center.x
        if keys[pygame.K_UP] and self.rect.top > 0:
            self._center.y -= self._speed
            self.rect.centery = self._center.y
        if keys[pygame.K_DOWN] and self.rect.bottom < WINDOW_HEIGHT:
            self._center.y += self._speed
            self.rect.centery = self._center.y

    def update(self):
        self.move()
