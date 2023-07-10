import pygame as pg
import numpy as np
from settings import * 





#Création fonction permettant de retourner ligne de grille la plus proche 
def align_grid(x, y):
    return (x // ECHELLE) * ECHELLE, (y // ECHELLE) * ECHELLE


# Début Raycasting
def raycasting(window, player_pos, player_angle, map):
    px, py = player_pos
    xm, ym = align_grid(px, py)
    cur_angle = player_angle - HALF_FOV
    preload_tile = align_grid(1, 1)
    texture_y = map[preload_tile[0]][preload_tile[1]] # placeholder value
    texture_x = map[preload_tile[0]][preload_tile[1]]  # placeholder value
    for ray in range(NUM_RAYS):
        ray_col_x = False
        ray_col_y = False
        sin_a = np.sin(cur_angle)
        cos_a = np.cos(cur_angle)
        sin_a = sin_a if sin_a else 0.000001
        cos_a = cos_a if cos_a else 0.000001
     

     # checks for walls on y axis
        gx, dx = (xm + ECHELLE, 1) if cos_a >= 0 else (xm, -1)
        for count in range(0, MAX_DEPTH, ECHELLE):
            depth_y = (gx - px) / cos_a
            y = py + depth_y * sin_a
            tile_y = align_grid(gx + dx, y)
            if tile_y in map:
                # Ray has intersection with wall
                texture_y = map[tile_y]
                ray_col_y = True
                break
            gx += dx * ECHELLE
       
        # checks for walls on x axis
        gy, dy = (ym + ECHELLE, 1) if sin_a >= 0 else (ym, -1)
        for count in range(0, MAX_DEPTH, ECHELLE):
            depth_x = (gy - py) / sin_a
            x = px + depth_x * cos_a
            tile_x = align_grid(x, gy + dy)
            if tile_x in map:
                # Ray has intersection with wall
                #texture_x = map[tile_x]
                print('tatao')
                ray_col_x = True
                break
            gy += dy * ECHELLE

       
        if ray_col_x or ray_col_y:
            depth, offset, texture = (depth_y, y, texture_y) if depth_y < depth_x else (depth_x, x, texture_x)
            offset = int(offset) % ECHELLE
            depth *= np.cos(player_angle - cur_angle)
            depth = max(depth, 0.00001)
            projected_height = min(int(WALL_HEIGHT / depth), 2 * resY)

            print('toto')
            pg.draw.rect(window, (200,200,200), map[tile_x], map[tile_y], TEXTURE_WIDTH, TEXTURE_HEIGHT)
            #wall_column = textures[texture].subsurface(offset * TEXTURE_SCALE, 0, TEXTURE_SCALE, TEXTURE_HEIGHT)
            #wall_column = pg.transform.scale(wall_column, (SCALE, projected_height))
            #sc.blit(wall_column, (ray * SCALE, HALF_HEIGHT - projected_height // 2))

        cur_angle += DELTA_ANGLE
