import pygame

class CameraSprites(pygame.sprite.Group):
    def __init__(self):
        super().__init__()

        self._windowSurf = pygame.display.get_surface()

        self._mapSurf = pygame.image.load("bg.png")
        self._mapRect = self._mapSurf.get_rect()

    def update(self):
        super().update()

    def draw(self):
        self._windowSurf.blit(self._mapSurf, self._mapRect)
        super().draw(self._windowSurf)