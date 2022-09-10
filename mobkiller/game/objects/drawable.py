import pygame
from pygame import Vector2

from mobkiller.globals import (
    UP,
    LEFT,
    DOWN,
    RIGHT
)

class Drawable(pygame.sprite.Sprite):
    def __init__(self, center: Vector2, texture: pygame.Surface = None, color: pygame.color.Color = None, size: Vector2 = None):
        super().__init__()

        if texture is None and size is None:
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

        self.rect = self.image.get_rect(center = center)

    @property
    def texture(self):
        return self._texture
    @texture.setter
    def texture(self, value: pygame.Surface):
        self._texture = value
        self._size = Vector2(self._texture.get_size())
        self.image = pygame.transform.scale(self._texture, self._size)