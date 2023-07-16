import pygame as pg
import numpy as np
from settings import *
from player import *
from cell import *

class Game:
    def __init__(self):
        self.size_text = 512
        self.wall_texture = []
        self.wall_texture.append (pg.image.load('image/wall.jpg').convert())
        self.wall_texture.append (pg.image.load('image/murs.jpg').convert())
        self.wall_texture.append (pg.image.load('image/mur.jpg').convert())
        self.wall_texture.append (pg.image.load('image/murw.jpg').convert())         
       
        self.sky_texture = pg.image.load('image/ciel.png').convert()
        # self.floor_texture = pg.image.load('image/sol.png.webp').convert()
        self.wall_texture[0] = pg.transform.scale(self.wall_texture[0], (self.size_text, self.size_text))
        self.wall_texture[1] = pg.transform.scale(self.wall_texture[1], (self.size_text, self.size_text))
        self.wall_texture[2] = pg.transform.scale(self.wall_texture[2], (self.size_text, self.size_text))
        self.wall_texture[3] = pg.transform.scale(self.wall_texture[3], (self.size_text, self.size_text))
        self.sky_texture = pg.transform.scale(self.sky_texture, (RES_X, HALF_HEIGHT))
        # self.floor_texture = pg.transform.scale(self.floor_texture, (RES_X, HALF_HEIGHT))
        
    
    # self.floor_texture = pg.surfarray.array3d(self.floor_texture)/255

    def raycasting(self, window, map, player): 
        angle_init = player.angle - HALF_FOV
        start_x = 0
        
        window.blit(self.sky_texture, (start_x, 0))
        # window.blit(self.floor_texture, (start_x, 0))
       
        for ray in range(NUM_RAYS):
            vector_init = pg.math.Vector2(int(player.position.x), int(player.position.y))  # vector_init = player_pos #px et py point de départ du rayon 
            sin_a = np.sin(angle_init)      #direction du rayon
            cos_a = np.cos(angle_init)
            sin_a = sin_a if sin_a else 0.000001
            cos_a = cos_a if cos_a else 0.000001
            vector_dir = (pg.math.Vector2(sin_a, cos_a))
            hit = False 

            delta_x = 10000 if vector_dir.x == 0 else abs(1 / vector_dir.x)
            delta_y = 10000 if vector_dir.y == 0 else abs(1 / vector_dir.y)
            
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
                if player.position.x > vector_init.x :
                       side = 2
                dist = dx - delta_x
            else:
                if player.position.y > vector_init.y:
                       side = 3
                dist = dy - delta_y
           
            # Position 0 = EST, 1 = NORD, 2 = OUEST 3 = SUD
            projected_height = int( RES_Y / dist)
            half_projected_height = projected_height // 2
            start_y = HALF_HEIGHT - half_projected_height
            start_x += SCALE     
            
        # Ajouter la texture du mur
            
            # différenciation des différents cotés du mur
            
            if side == 0 or side == 2:
                  texture_x = player.position.y + dist * vector_dir.y
            else :
                  texture_x = player.position.x + dist * vector_dir.x
            
            # Récupérer la portion décimale de la position du rayon
            
            dec_text_x = texture_x - int(texture_x)

            wall_column = self.wall_texture[0].subsurface((int(dec_text_x * self.size_text), 0, 1, self.size_text))
            wall_column = pg.transform.scale(wall_column, (SCALE, projected_height))
            window.blit(wall_column, (start_x, start_y))
            
            angle_init += DELTA_ANGLE