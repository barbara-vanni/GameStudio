import pygame as pg
import numpy as np
from settings import *
from player import *

def raycasting(window, map, player): 
    angle_init = player.angle - HALF_FOV
    start_x = 0
    for ray in range(NUM_RAYS):
        vector_init = pg.math.Vector2(player.position.x, player.position.y)  # vector_init = player_pos #px et py point de départ du rayon 
        sin_a = np.sin(angle_init)      #direction du rayon
        cos_a = np.cos(angle_init)
        sin_a = sin_a if sin_a else 0.000001
        cos_a = cos_a if cos_a else 0.000001
        vector_dir = (pg.math.Vector2(sin_a*RAY_SPEED, cos_a*RAY_SPEED))
        hit = False
        dist = 0 
        # print(vector_init)
        while not hit: 
            vector_init += vector_dir # rayon lancé
            if map[int(vector_init.y)][int(vector_init.x)] == 1:
                hit = True
            dist += RAY_SPEED #rayon à touché = distance parcourue
        corrected_dist = dist * np.cos(angle_init - player.angle)  # Apply fish-eye correction
        projected_height = int(RES_Y / corrected_dist)
        half_projected_height = projected_height // 2
        start_y = HALF_HEIGHT - half_projected_height
        start_x += SCALE
        pg.draw.rect(window, (200,200,200), (start_x, start_y, SCALE, projected_height))
        angle_init += DELTA_ANGLE

    
    
