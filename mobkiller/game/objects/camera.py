import pygame

from mobkiller.game.objects.player import Player
from mobkiller.game.objects.background import Background
from mobkiller.globals import (
    UP,
    LEFT,
    DOWN,
    RIGHT,
    WINDOW_HEIGHT,
    WINDOW_WIDTH
)

class Camera(pygame.sprite.Group):
    def __init__(self, player: Player, bg: Background):
        super().__init__()
        self._player = player
        self._isMoving: bool
        self._playerMoveDirections: list
        self._bg = bg

    def update(self, isPlayerAttacking: bool):
        keys = pygame.key.get_pressed()
        self._isMoving = False
        self._playerMoveDirections = []

        if keys[pygame.K_w]:
            self._isMoving = True
            if self._bg.rect.top == 0 or self._player.rect.centery > WINDOW_HEIGHT / 2:
                self._playerMoveDirections.append(UP)
            else:
                for sprite in self.sprites():
                    sprite.move(DOWN, self._player.speed)

        if keys[pygame.K_a]:
            self._isMoving = True
            self._player.direction = LEFT

            if self._bg.rect.left == 0 or self._player.rect.centerx > WINDOW_WIDTH / 2:
                self._playerMoveDirections.append(LEFT)
            else:
                for sprite in self.sprites():
                    sprite.move(RIGHT, self._player.speed)

        if keys[pygame.K_s]:
            self._isMoving = True
            if self._bg.rect.bottom == WINDOW_HEIGHT or self._player.rect.centery < WINDOW_HEIGHT / 2:
                self._playerMoveDirections.append(DOWN)
            else:
                for sprite in self.sprites():
                    sprite.move(UP, self._player.speed)

        if keys[pygame.K_d]:
            self._isMoving = True
            self._player.direction = RIGHT

            if self._bg.rect.right == WINDOW_WIDTH or self._player.rect.centerx < WINDOW_WIDTH / 2:
                self._playerMoveDirections.append(RIGHT)
            else:
                for sprite in self.sprites():
                    sprite.move(LEFT, self._player.speed)

        self._player.update(self._playerMoveDirections, self._isMoving, isPlayerAttacking)

    def draw(self, surf: pygame.Surface):
        super().draw(surf)
        surf.blit(self._player.image, self._player.rect.topleft)