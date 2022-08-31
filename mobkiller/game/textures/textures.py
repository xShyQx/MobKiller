import pygame
from enum import Enum, EnumMeta
from pathlib import Path
from functools import lru_cache

PREFIX = Path("mobkiller/game/textures/pictures").resolve()

class TexturesMeta(EnumMeta):
    def __getattribute__(cls, img: pygame.Surface | Path) -> pygame.Surface:
        texture = super().__getattribute__(img)
        if isinstance(texture, cls):
            texture = TexturesMeta.cached_texture(cls, PREFIX / texture.value)
        return texture
    
    @lru_cache
    def cached_texture(self, path: Path) -> pygame.Surface:
        if isinstance(path, Path):
            try:
                texture = pygame.image.load(path)
            except Exception as ex:
                print("ERR" + ex)
        else:
            raise FileNotFoundError("Invalid path to texture")

        return texture

class Textures(Enum, metaclass=TexturesMeta):
    BACKGROUND = "bg.png"
    PLAYER_LEFT = "player_left.png"
    PLAYER_RIGHT = "player_right.png"

    def __str__(self):
        return str(PREFIX / self.value)

    def __repr__(self):
        return str(PREFIX / self.value)