from pygame import Vector2

from mobkiller.game.objects.drawable import Drawable

class Creature(Drawable):
    def __init__(self, position: Vector2, size: Vector2, color=None, texture=None):
        super().__init__(position, size, color, texture)
        self._speed: float

    @property
    def speed(self):
        return self._speed