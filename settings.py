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
player_pos = PLAYER_POS_INIT
player_angle = 0
velocity = 4


FOV = np.pi / 3
HALF_FOV = FOV / 2

WALL_HEIGHT = 4 * DIST * ECHELLE