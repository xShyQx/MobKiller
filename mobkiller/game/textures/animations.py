from enum import Enum
from mobkiller.game.textures.textures import Textures

class Animations(Enum):
    PLAYER_MOVE_LEFT_ANIMATION = [
        Textures.PLAYER_LEFT,
        Textures.PLAYER_LEFT2_4,
        Textures.PLAYER_LEFT3,
        Textures.PLAYER_LEFT2_4,
        Textures.PLAYER_LEFT,
        Textures.PLAYER_LEFT6_8,
        Textures.PLAYER_LEFT7,
        Textures.PLAYER_LEFT6_8,
        Textures.PLAYER_LEFT
    ]

    PLAYER_MOVE_RIGHT_ANIMATION = [
        Textures.PLAYER_RIGHT,
        Textures.PLAYER_RIGHT2_4,
        Textures.PLAYER_RIGHT3,
        Textures.PLAYER_RIGHT2_4,
        Textures.PLAYER_RIGHT,
        Textures.PLAYER_RIGHT6_8,
        Textures.PLAYER_RIGHT7,
        Textures.PLAYER_RIGHT6_8,
        Textures.PLAYER_RIGHT
    ]

    PLAYER_ATTACK_LEFT_ANIMATION = [
        Textures.PLAYER_LEFT,
        Textures.PLAYER_LEFT_A1,
        Textures.PLAYER_LEFT_A2,
        Textures.PLAYER_LEFT_A3,
        Textures.PLAYER_LEFT_A4,
        Textures.PLAYER_LEFT_A5,
        Textures.PLAYER_LEFT_A6,
        Textures.PLAYER_LEFT
    ]

    PLAYER_ATTACK_RIGHT_ANIMATION = [
        Textures.PLAYER_RIGHT,
        Textures.PLAYER_RIGHT_A1,
        Textures.PLAYER_RIGHT_A2,
        Textures.PLAYER_RIGHT_A3,
        Textures.PLAYER_RIGHT_A4,
        Textures.PLAYER_RIGHT_A5,
        Textures.PLAYER_RIGHT_A6,
        Textures.PLAYER_RIGHT
    ]