import pygame
from pygame import Vector2

from mobkiller.game.objects.drawable import Drawable

class Creature(Drawable):
    def __init__(self, center: Vector2, texture: pygame.Surface = None, color: pygame.color.Color = None, size: Vector2 = None):
        super().__init__(center, texture, color, size)
        self._speed: float

    @property
    def speed(self):
        return self._speed