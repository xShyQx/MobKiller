from tkinter.tix import WINDOW
import pygame
from pygame import Vector2

from mobkiller.game.objects.creature import Creature
from mobkiller.globals import (
    PLAYER_BASE_SPEED,
    PLAYER_SIZE,
    WINDOW_HEIGHT,
    WINDOW_WIDTH
)

class Player(Creature):
    def __init__(self, position: Vector2):
        super().__init__(position, PLAYER_SIZE, (0, 255, 0))
        self._speed = PLAYER_BASE_SPEED

    def move(self, direction: int, speed: float):
        super().move(direction, speed)
        self.keepInside()

    def keepInside(self):
        if self.rect.top < 0:
            self.rect.top = 0

        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.bottom > WINDOW_HEIGHT:
            self.rect.bottom = WINDOW_HEIGHT

        if self.rect.right > WINDOW_WIDTH:
            self.rect.right = WINDOW_WIDTH
