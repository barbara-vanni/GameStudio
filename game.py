import pygame as pg
import numpy as np
from settings import *
from player import *
from cell import *

class Game:
    def __init__(self):
        self.wall_texture = pg.image.load('image/mur.jpg')
        self.floor_texture = pg.image.load('image/sol.png.webp')
        self.sky_texture = pg.image.load('image/ciel.png')

    def raycasting(self, window, map, player): 
        angle_init = player.angle - HALF_FOV
        start_x = 0
        for ray in range(NUM_RAYS):
            vector_init = pg.math.Vector2(int(player.position.x), int(player.position.y))  # vector_init = player_pos #px et py point de départ du rayon 
            sin_a = np.sin(angle_init)      #direction du rayon
            cos_a = np.cos(angle_init)
            sin_a = sin_a if sin_a else 0.000001
            cos_a = cos_a if cos_a else 0.000001
            vector_dir = (pg.math.Vector2(sin_a, cos_a))
            hit = False 

            delta_x = 10000 if vector_dir.x == 0 else 1/vector_dir.x
            delta_y = 10000 if vector_dir.y == 0 else 1/vector_dir.y
            
            if vector_dir.x < 0 :
                    dx = (player.position.x - vector_init.x) * delta_x
                    step_x = -1
            else:
                    dx = (vector_init.x - player.position.x + 1) * delta_x
                    step_x = 1
            if vector_dir.y < 0 :
                    dy = (player.position.y - vector_init.y) * delta_y
                    step_y = -1
            else:
                    dy = (vector_init.y - player.position.y + 1) * delta_y
                    step_y = 1
            
            while not hit: 
                if dx < dy :
                      side = 0
                      dx += delta_x
                      vector_init.x += step_x
                else :
                      side = 1
                      dy += delta_y
                      vector_init.y += step_y

                
                cell = map[int(vector_init.y)][int(vector_init.x)]
                if cell.type == Cell_type.WALL :
                    hit = True
            if side == 0 :
                      dist = dx - delta_x
            else:
                      dist = dy - delta_y
            
            projected_height = int( RES_Y / dist)
            half_projected_height = projected_height // 2
            start_y = HALF_HEIGHT - half_projected_height
            start_x += SCALE

            # Ajouter la texture du mur
            # wall_column = self.wall_texture.subsurface((0, 0, 1, self.wall_texture.get_height()))
            # wall_column = pg.transform.scale(wall_column, (SCALE, projected_height))
            # window.blit(wall_column, (start_x, start_y))
            
            # # Ajouter la texture du ciel
            # sky_column = pg.transform.scale(self.sky_texture, (SCALE, HALF_HEIGHT))
            # window.blit(sky_column, (start_x, 0))

            # # Ajouter la texture du sol
            # floor_column = pg.transform.scale(self.floor_texture, (SCALE, HALF_HEIGHT))
            # window.blit(floor_column, (start_x, HALF_HEIGHT))
            
            pg.draw.rect(window, cell.color, (start_x, start_y, SCALE, projected_height))
            
            angle_init += DELTA_ANGLE