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

        self._isMoving = False
        self._isAttacking = False

        self._speed = PLAYER_BASE_SPEED
        self._direction = Vector2()

        self._faceDirection = "left"
        self._centerCamera = Vector2(self.rect.center)
        self._curMoveFrame = 0
        self._moveFrames = PLAYER_MOVE_FRAMES
        self._curAttackFrame = 0
        self._attackFrames = PLAYER_ATTACK_FRAMES

    @property
    def centerCamera(self):
        return self._centerCamera

    def update(self):
        self.move()
        self.attack()

        if self._isAttacking:
            self.attackAnimation()
        elif self._isMoving:
            self.moveAnimation()
        else:
            self.stayAnimation()

        self.keepInside()

    def move(self):
        self._direction.x = 0
        self._direction.y = 0
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self._direction.y = -1
        if keys[pygame.K_a]:
            self._direction.x = -1
            self._faceDirection = "left"
        if keys[pygame.K_s]:
            self._direction.y = 1
        if keys[pygame.K_d]:
            self._direction.x = 1
            self._faceDirection = "right"

        self._isMoving = self._direction.x != 0 or self._direction.y != 0

        self.rect.center += self._direction * self._speed

        if self._isMoving:
            self._centerCamera += self._direction * self._speed

    def keepInside(self):
        if self.rect.top < Player.borders.top:
            self.rect.top = Player.borders.top

        if self.rect.left < Player.borders.left:
            self.rect.left = Player.borders.left

        if self.rect.bottom > Player.borders.bottom:
            self.rect.bottom = Player.borders.bottom

        if self.rect.right > Player.borders.right:
            self.rect.right = Player.borders.right

    def attack(self):
        mouse = pygame.mouse.get_pressed()

        if mouse[0]:
            self._isAttacking = True

    def moveAnimation(self):
        if self._curMoveFrame >= PLAYER_MOVE_FRAMES:
            self._curMoveFrame = 0
        
        if self._isMoving:
            if self._faceDirection == "left":
                self.texture = Animations.PLAYER_MOVE_LEFT_ANIMATION.value[floor(self._curMoveFrame)]
            elif self._faceDirection == "right":
                self.texture = Animations.PLAYER_MOVE_RIGHT_ANIMATION.value[floor(self._curMoveFrame)]
            self._curMoveFrame += 0.5

    def attackAnimation(self):
        self._curMoveFrame = 0
        if self._curAttackFrame >= PLAYER_ATTACK_FRAMES:
            self._isAttacking = False
            self._curAttackFrame = 0

        if self._faceDirection == "left":
            right = self.rect.right
            self.texture = Animations.PLAYER_ATTACK_LEFT_ANIMATION.value[floor(self._curAttackFrame)]
            self.rect.right = right
        elif self._faceDirection == "right":
            left = self.rect.left
            self.texture = Animations.PLAYER_ATTACK_RIGHT_ANIMATION.value[floor(self._curAttackFrame)]
            self.rect.left = left
        self._curAttackFrame += 0.5

    def stayAnimation(self):
        if self._faceDirection == "left":
            self.texture = Textures.PLAYER_LEFT
        elif self._faceDirection == "right":
            self.texture = Textures.PLAYER_RIGHT