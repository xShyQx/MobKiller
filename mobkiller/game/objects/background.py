from mobkiller.game.objects.drawable import Drawable

from mobkiller.game.textures.textures import Textures

from mobkiller.globals import (
    WINDOW_WIDTH,
    WINDOW_HEIGHT
)

class Background(Drawable):
    def __init__(self):
        super().__init__((WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2), (1000, 1000), texture=Textures.BACKGROUND)