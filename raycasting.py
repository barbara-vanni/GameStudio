import pygame as pg
import numpy as np

#Settings
resX = 1920
resY = 1080
HALF_WIDTH = resX // 2
HALF_HEIGHT = resY // 2
ECHELLE = 100 

# player settings
player_pos = (1, 1)
player_angle = 0
vitesse = 4

# ray casting settings
FOV = np.pi / 3  # Approx 60 Degrees
HALF_FOV = FOV / 2
NUM_RAYS = 80
MAX_DEPTH = 2000
DELTA_ANGLE = FOV / NUM_RAYS
DIST = NUM_RAYS / (2 * np.tan(HALF_FOV))
WALL_HEIGHT = 4 * DIST * ECHELLE
SCALE = resX // NUM_RAYS  # must result in a whole integer number otherwise rendering cutoff happens




#Création fonction permettant de retourner ligne de grille la plus proche 
def align_grid(x, y):
    return (x // ECHELLE) * ECHELLE, (y // ECHELLE) * ECHELLE


# Début Raycasting
def raycasting(sc, player_pos, player_angle, textures):
    px, py = player_pos
    xm, ym = align_grid(px, py)
    cur_angle = player_angle - HALF_FOV
    preload_tile = align_grid(1, 1)
    texture_y = map[preload_tile]  # placeholder value
    texture_x = map[preload_tile]  # placeholder value
    for ray in range(NUM_RAYS):
        ray_col_x = False
        ray_col_y = False
        sin_a = np.sin(cur_angle)
        cos_a = np.cos(cur_angle)
        sin_a = sin_a if sin_a else 0.000001
        cos_a = cos_a if cos_a else 0.000001
