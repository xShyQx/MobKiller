from mobkiller.game.objects.drawable import Drawable

from mobkiller.game.textures.textures import Textures

from mobkiller.globals import (
    WINDOW_WIDTH,
    WINDOW_HEIGHT
)

class Background(Drawable):
    def __init__(self):
        super().__init__(texture=Textures.BACKGROUND, topleft=(0, 0))
        print(self._size)