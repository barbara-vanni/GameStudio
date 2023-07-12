import numpy as np
import pygame as pg

#Settings
RES_X = 800
RES_Y = 600
HALF_WIDTH = RES_X // 2
HALF_HEIGHT = RES_Y // 2
ECHELLE = 100 

# player settings
PLAYER_POS_INIT = pg.math.Vector2(8,11) # position initiale
player_pos = PLAYER_POS_INIT
player_angle = 0.0
RAY_SPEED = 0.04  #
PLAYER_SPEED = 0.02


# ray casting settings
FOV = 0.6  # Approx 60 Degrees
HALF_FOV = FOV / 2
NUM_RAYS = 800
MAX_DEPTH = 2000
DELTA_ANGLE = FOV / NUM_RAYS
DIST = NUM_RAYS / (2)
WALL_HEIGHT = 4 * DIST * ECHELLE
SCALE = RES_X // NUM_RAYS  # must result in a whole integer number otherwise rendering cutoff happens

# texture settings
TEXTURE_WIDTH = 1000
TEXTURE_HEIGHT = 1000
TEXTURE_SCALE = TEXTURE_WIDTH // ECHELLE

# COLORS

CYAN = (0, 255, 255)
TEAL = (0, 128, 128)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

colors = [
    WHITE,
    CYAN,
    TEAL,
    YELLOW
]