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
        self._bg = bg

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            if self._bg.rect.top == 0 or self._player.rect.centery > WINDOW_HEIGHT / 2:
                self._player.move(UP, self._player.speed)
            else:
                for sprite in self.sprites():
                    sprite.move(DOWN, self._player.speed)

        if keys[pygame.K_a]:
            if self._bg.rect.left == 0 or self._player.rect.centerx > WINDOW_WIDTH / 2:
                self._player.move(LEFT, self._player.speed)
            else:
                for sprite in self.sprites():
                    sprite.move(RIGHT, self._player.speed)

        if keys[pygame.K_s]:
            if self._bg.rect.bottom == WINDOW_HEIGHT or self._player.rect.centery < WINDOW_HEIGHT / 2:
                self._player.move(DOWN, self._player.speed)
            else:
                for sprite in self.sprites():
                    sprite.move(UP, self._player.speed)

        if keys[pygame.K_d]:
            if self._bg.rect.right == WINDOW_WIDTH or self._player.rect.centerx < WINDOW_WIDTH / 2:
                self._player.move(RIGHT, self._player.speed)
            else:
                for sprite in self.sprites():
                    sprite.move(LEFT, self._player.speed)