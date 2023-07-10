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
FOV = np.pi / 3  # Approx 60 Degrees
HALF_FOV = FOV / 2
NUM_RAYS = 800
MAX_DEPTH = 2000
DELTA_ANGLE = FOV / NUM_RAYS
DIST = NUM_RAYS / (2 * np.tan(HALF_FOV))
WALL_HEIGHT = 4 * DIST * ECHELLE
SCALE = RES_X // NUM_RAYS  # must result in a whole integer number otherwise rendering cutoff happens

# texture settings
TEXTURE_WIDTH = 1000
TEXTURE_HEIGHT = 1000
TEXTURE_SCALE = TEXTURE_WIDTH // ECHELLE
