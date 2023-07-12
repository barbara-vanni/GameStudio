import pygame as pg
import numpy as np
from settings import *
from player import *

class Game:
    def __init__(self):
        self.wall_texture = pg.image.load('image/mur.jpg')
        self.floor_texture = pg.image.load('image/sol.png.webp')
        self.sky_texture = pg.image.load('image/ciel.png')

    def raycasting(self, window, map, player): 
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
            while not hit: 
                vector_init += vector_dir # rayon lancé
                if map[int(vector_init.y)][int(vector_init.x)] == 1:
                    hit = True
                dist += RAY_SPEED #rayon à touché = distance parcourue
            projected_height = int(RES_Y / dist)
            half_projected_height = projected_height // 2
            start_y = HALF_HEIGHT - half_projected_height
            start_x += SCALE

            # Ajouter la texture du mur
            wall_column = self.wall_texture.subsurface((0, 0, 1, self.wall_texture.get_height()))
            wall_column = pg.transform.scale(wall_column, (SCALE, projected_height))
            window.blit(wall_column, (start_x, start_y))
            
            # Ajouter la texture du ciel
            sky_column = pg.transform.scale(self.sky_texture, (SCALE, HALF_HEIGHT))
            window.blit(sky_column, (start_x, 0))

            # Ajouter la texture du sol
            floor_column = pg.transform.scale(self.floor_texture, (SCALE, HALF_HEIGHT))
            window.blit(floor_column, (start_x, HALF_HEIGHT))
            
            
            angle_init += DELTA_ANGLE