from pygame import Vector2

from mobkiller.game.objects.drawable import Drawable

class Creature(Drawable):
    def __init__(self, center: Vector2, texture=None, color=None, size: Vector2 = None):
        super().__init__(texture, color, size, center)
        self._speed: float

    @property
    def speed(self):
        return self._speed