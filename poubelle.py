import pygame as pg
import numpy as np
from settings import *

def raycassting(window, map): 
    angle_init = player_angle - HALF_FOV
    start_x = 0
    for ray in range(NUM_RAYS):
        vector_init = pg.math.Vector2(player_pos.x, player_pos.y)
        # vector_init = player_pos #px et py point de départ du rayon 
        sin_a = np.sin(angle_init)      #direction du rayon
        cos_a = np.cos(angle_init)
        sin_a = sin_a if sin_a else 0.000001
        cos_a = cos_a if cos_a else 0.000001
        vector_dir = (pg.math.Vector2(sin_a*velocity/ECHELLE, cos_a*velocity/ECHELLE)) #erreur
        hit = False
        dist = 0 
        while not hit: 
            vector_init += vector_dir # rayon lancé
            if map[int(vector_init.y)][int(vector_init.x)] == 1:
                hit = True
            dist += velocity #rayon à touché = distance parcourue       ERREUR
        projected_height = int(WALL_HEIGHT / dist)
        half_projected_height = projected_height // 2
        start_y = HALF_HEIGHT - half_projected_height
        print(start_y)
        start_x += SCALE
        pg.draw.rect(window, (100,200,100), (start_x, start_y, SCALE, projected_height))

    
    