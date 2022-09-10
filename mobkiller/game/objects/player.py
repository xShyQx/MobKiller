import pygame
from pygame import Vector2
from math import floor

from mobkiller.game.objects.creature import Creature

from mobkiller.game.textures.textures import Textures
from mobkiller.game.textures.animations import Animations

from mobkiller.globals import (
    PLAYER_BASE_SPEED,
    PLAYER_MOVE_FRAMES,
    PLAYER_ATTACK_FRAMES,
    WINDOW_HEIGHT,
    WINDOW_WIDTH,
)

class Player(Creature):
    borders: pygame.Rect

    def __init__(self):
        super().__init__((WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2), Textures.PLAYER_LEFT)

        self._curFrame = 0
        self._moveFrames = PLAYER_MOVE_FRAMES
        self._attackFrames = PLAYER_ATTACK_FRAMES

        self._finishedAttacking = True

        self._speed = PLAYER_BASE_SPEED
        self._direction = Vector2()

    def update(self):
        self.move()
        self.keepInside()

    def move(self):
        self._direction.x = 0
        self._direction.y = 0
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self._direction.y = -1
        if keys[pygame.K_a]:
            self._direction.x = -1
        if keys[pygame.K_s]:
            self._direction.y = 1
        if keys[pygame.K_d]:
            self._direction.x = 1

        self.rect.center += self._direction * self._speed

    def keepInside(self):
        if self.rect.top < Player.borders.top:
            self.rect.top = Player.borders.top

        if self.rect.left < Player.borders.left:
            self.rect.left = Player.borders.left

        if self.rect.bottom > Player.borders.bottom:
            self.rect.bottom = Player.borders.bottom

        if self.rect.right > Player.borders.right:
            self.rect.right = Player.borders.right