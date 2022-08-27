import pygame
from pygame import Vector2

class Drawable(pygame.sprite.Sprite):
    def __init__(self, position: Vector2, size: Vector2, color: pygame.Color = None, texture = None):
        super().__init__()
        self._center = position

        self.image = pygame.Surface(size)
        self.rect = self.image.get_rect()
        self.rect.center = self._center

        if color is None and texture is None:
            self.image.fill((0, 0, 0))
        elif color is None:
            self.image = pygame.transform.scale(pygame.image.load(texture), size)
        else:
            self.image.fill(color)