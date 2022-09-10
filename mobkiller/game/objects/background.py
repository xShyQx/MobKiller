from mobkiller.game.objects.drawable import Drawable

from mobkiller.game.textures.textures import Textures

from mobkiller.globals import (
    WINDOW_CENTER
)

class Background(Drawable):
    def __init__(self):
        super().__init__(WINDOW_CENTER, texture=Textures.BACKGROUND)