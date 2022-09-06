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
        Textures.PLAYER_LEFT6_8
    ]
    
    PLAYER_MOVE_RIGHT_ANIMATION = [
        Textures.PLAYER_RIGHT,
        Textures.PLAYER_RIGHT2_4,
        Textures.PLAYER_RIGHT3,
        Textures.PLAYER_RIGHT2_4,
        Textures.PLAYER_RIGHT,
        Textures.PLAYER_RIGHT6_8,
        Textures.PLAYER_RIGHT7,
        Textures.PLAYER_RIGHT6_8
    ]