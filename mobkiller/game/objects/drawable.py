import pygame
from pygame import Vector2

from mobkiller.globals import (
    UP,
    LEFT,
    DOWN,
    RIGHT
)

class Drawable(pygame.sprite.Sprite):
    def __init__(self, texture=None, color=None, size: Vector2 = None, topleft: Vector2 = None, center: Vector2 = None):
        super().__init__()

        if texture is None and size is None:
            raise NotImplementedError
        if topleft is None and center is None:
            raise NotImplementedError

        if texture is not None:
            self.texture = texture
        else:
            self._size = size
            self.image = pygame.Surface(self._size)
            if color is None:
                self.image.fill((0, 0, 0))
            else:
                self.image.fill(color)

        if center is None:
            self._center = topleft + Vector2(self._size.x / 2, self._size.y / 2)
        else:
            self._center = center

        self.rect = self.image.get_rect()
        self.rect.centerx = self._center.x
        self.rect.centery = self._center.y

    @property
    def texture(self):
        return self._texture
    @texture.setter
    def texture(self, value: pygame.Surface):
        self._texture = value
        self._size = Vector2(self._texture.get_size())
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