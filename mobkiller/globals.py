from pygame import Vector2

from mobkiller.game.textures.animations import Animations

# Window
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
WINDOW_CENTER = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)

# Player
PLAYER_BASE_SPEED = 3
PLAYER_MOVE_FRAMES = len(Animations.PLAYER_MOVE_LEFT_ANIMATION.value)
PLAYER_ATTACK_FRAMES = len(Animations.PLAYER_ATTACK_LEFT_ANIMATION.value)

# Enemy
ENEMY_SIZE = Vector2(48, 48)
ENEMY_BASE_SPEED = 5

# Movement
UP = 1
LEFT = 2
DOWN = 3
RIGHT = 4