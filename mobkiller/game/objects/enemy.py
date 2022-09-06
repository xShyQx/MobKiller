from pygame import Vector2

from mobkiller.game.objects.creature import Creature
from mobkiller.globals import (
    ENEMY_BASE_SPEED,
    ENEMY_SIZE
)

class Enemy(Creature):
    def __init__(self, position: Vector2):
        super().__init__(position, color=(255, 0, 0), size=ENEMY_SIZE)
        self._speed = ENEMY_BASE_SPEED