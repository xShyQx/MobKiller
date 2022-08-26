import pygame
from pygame import Vector2

class Drawable(pygame.sprite.Sprite):
    def __init__(self, position: Vector2, size: Vector2, group, color: pygame.Color):
        super().__init__(group)
        self._center = position

        self.image = pygame.Surface(size)
        self.rect = self.image.get_rect()
        self.rect.center = self._center

        self.image.fill(color)