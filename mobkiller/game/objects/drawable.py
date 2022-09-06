import pygame
from pygame import Vector2

from mobkiller.globals import (
    UP,
    LEFT,
    DOWN,
    RIGHT
)

class Drawable(pygame.sprite.Sprite):
    def __init__(self, position: Vector2, size: Vector2, texture=None, color=None):
        super().__init__()
        self._center = Vector2(position)
        self._size = size
        self._texture: pygame.Surface

        self.image = pygame.Surface(self._size)
        self.rect = self.image.get_rect()
        self.rect.center = self._center

        if color is None and texture is None:
            self.image.fill((0, 0, 0))
        elif color is None:
            self.texture = texture
        else:
            self.image.fill(color)

    @property
    def texture(self):
        return self._texture
    @texture.setter
    def texture(self, value: pygame.Surface):
        self._texture = value
        self._size = self._texture.get_size()
        self.image = pygame.transform.scale(self._texture, self._size)

    def move(self, direction: int, speed: float):
        if direction == UP:
            self._center.y -= speed
            self.rect.centery = self._center.y

        if direction == LEFT:
            self._center.x -= speed
            self.rect.centerx = self._center.x

        if direction == DOWN:
            self._center.y += speed
            self.rect.centery = self._center.y

        if direction == RIGHT:
            self._center.x += speed
            self.rect.centerx = self._center.x