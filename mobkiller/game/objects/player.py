import pygame
from pygame import Vector2

from mobkiller.game.objects.drawable import Drawable

class Player(Drawable):
    def __init__(self, position: Vector2, size: Vector2, color: pygame.Color = (0, 255, 0)):
        super().__init__(position, size, color)
