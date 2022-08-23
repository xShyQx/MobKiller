import pygame
from pygame import Vector2

class Drawable(pygame.sprite.Sprite):
    def __init__(self, position: Vector2, size: Vector2, color: pygame.Color):
        super().__init__()

        self.image = pygame.Surface(size)
        self.rect = self.image.get_rect()
        self.rect.center = position

        self.image.fill(color)