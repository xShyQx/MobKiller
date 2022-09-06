from pygame import Vector2
from math import floor

from mobkiller.game.objects.creature import Creature

from mobkiller.game.textures.textures import Textures
from mobkiller.game.textures.animations import Animations

from mobkiller.globals import (
    PLAYER_BASE_SPEED,
    PLAYER_MOVE_FRAMES,
    PLAYER_ATTACK_FRAMES,
    PLAYER_SIZE,
    WINDOW_HEIGHT,
    WINDOW_WIDTH,
    LEFT,
    RIGHT
)

class Player(Creature):
    def __init__(self, position: Vector2):
        super().__init__(position, PLAYER_SIZE, Textures.PLAYER_LEFT)

        self._curFrame = 0
        self._moveFrames = PLAYER_MOVE_FRAMES
        self._attackFrames = PLAYER_ATTACK_FRAMES

        self._speed = PLAYER_BASE_SPEED
        self._direction = LEFT

    @property
    def direction(self):
        return self._direction
    @direction.setter
    def direction(self, value):
        self._direction = value

    def update(self, moveDirections: list, isRunning: bool, isAttacking: bool):
        for direction in moveDirections:
            super().move(direction, self._speed)
        self.keepInside()

        if isRunning:
            self.updateMove()
        elif isAttacking:
            self.updateAttack()
        else:
            self._curFrame = 0
            if self.direction == LEFT:
                self.texture = Textures.PLAYER_LEFT
            elif self.direction == RIGHT:
                self.texture = Textures.PLAYER_RIGHT

    def keepInside(self):
        if self.rect.top < 0:
            self.rect.top = 0

        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.bottom > WINDOW_HEIGHT:
            self.rect.bottom = WINDOW_HEIGHT

        if self.rect.right > WINDOW_WIDTH:
            self.rect.right = WINDOW_WIDTH

    def updateMove(self):
        if self._curFrame >= PLAYER_MOVE_FRAMES:
            self._curFrame = 0

        if self.direction == LEFT:
            self.texture = Animations.PLAYER_MOVE_LEFT_ANIMATION.value[floor(self._curFrame)]
        elif self.direction == RIGHT:
            self.texture = Animations.PLAYER_MOVE_RIGHT_ANIMATION.value[floor(self._curFrame)]
        self._curFrame += 0.005 

    def updateAttack(self):
        pass
