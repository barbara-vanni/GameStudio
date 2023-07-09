import pygame as pg
import numpy as np

#Ecran
RES_X = 1920
RES_Y = 1080
HALF_WIDTH = RES_X // 2
HALF_HEIGHT = RES_Y // 2
ECHELLE = 100

#Gestion du joueur
PLAYER_POS_INIT = pg.math.Vector2(1,1) #Position Initiale du joueur
PLAYER_SPEED = 4
player_pos = PLAYER_POS_INIT
player_angle = 0


#Raycasting settings
FOV = np.pi / 3  # Approx 60 Degrees
HALF_FOV = FOV / 2
NUM_RAYS = 80

WALL_HEIGHT = 4 * DIST * ECHELLE

import numpy as np
import pygame as pg




# ray casting settings


MAX_DEPTH = 2000
DELTA_ANGLE = FOV / NUM_RAYS
DIST = NUM_RAYS / (2 * np.tan(HALF_FOV))

SCALE = RES_X // NUM_RAYS  # must result in a whole integer number otherwise rendering cutoff happens

# texture settings
TEXTURE_WIDTH = 1000
TEXTURE_HEIGHT = 1000
TEXTURE_SCALE = TEXTURE_WIDTH // ECHELLE
