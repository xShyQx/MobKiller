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
    PLAYER_LEFT = "player/player_left.png"
    PLAYER_LEFT2_4 = "player/player_left2-4.png"
    PLAYER_LEFT3 = "player/player_left3.png"
    PLAYER_LEFT6_8 = "player/player_left6-8.png"
    PLAYER_LEFT7 = "player/player_left7.png"
    PLAYER_LEFT_A1 = "player/player_leftA1.png"
    PLAYER_LEFT_A2 = "player/player_leftA2.png"
    PLAYER_LEFT_A3 = "player/player_leftA3.png"
    PLAYER_LEFT_A4 = "player/player_leftA4.png"
    PLAYER_LEFT_A5 = "player/player_leftA5.png"
    PLAYER_LEFT_A6 = "player/player_leftA6.png"
    PLAYER_RIGHT = "player/player_right.png"
    PLAYER_RIGHT2_4 = "player/player_right2-4.png"
    PLAYER_RIGHT3 = "player/player_right3.png"
    PLAYER_RIGHT6_8 = "player/player_right6-8.png"
    PLAYER_RIGHT7 = "player/player_right7.png"
    PLAYER_RIGHT_A1 = "player/player_rightA1.png"
    PLAYER_RIGHT_A2 = "player/player_rightA2.png"
    PLAYER_RIGHT_A3 = "player/player_rightA3.png"
    PLAYER_RIGHT_A4 = "player/player_rightA4.png"
    PLAYER_RIGHT_A5 = "player/player_rightA5.png"
    PLAYER_RIGHT_A6 = "player/player_rightA6.png"

    def __str__(self):
        return str(PREFIX / self.value)

    def __repr__(self):
        return str(PREFIX / self.value)