from enum import Enum
from pathlib import Path

PREFIX = Path("mobkiller/game/textures/pictures").resolve()

class Textures(Enum):
    BACKGROUND = "bg.png"
    PLAYER_LEFT = "player_left.png"
    PLAYER_RIGHT = "player_right.png"

    def __str__(self):
        return str(PREFIX / self.value)

    def __repr__(self):
        return str(PREFIX / self.value)