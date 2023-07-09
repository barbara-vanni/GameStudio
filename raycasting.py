import pygame as pg
import numpy as np
from settings import *

def raycasting(window, map):
    ray_angle = player_angle - HALF_FOV
    start_x = 0
    for ray in range(NUM_RAYS):
        ray_vector = pg.Vector2(player_pos.x, player_pos.y)
        sin_a = np.sin(ray_angle)
        cos_a = np.cos(ray_angle)
        sin_a = sin_a if sin_a else 0.000001
        cos_a = cos_a if cos_a else 0.000001
        direction_vector = pg.Vector2(sin_a * RAY_SPEED, cos_a * RAY_SPEED)
        hit = False
        distance = 0
        while not hit:
            ray_vector += direction_vector
            distance += RAY_SPEED
            if map[int(ray_vector.y)][int(ray_vector.x)] == 1:
                hit = True
        projected_height = int(WALL_HEIGHT / distance)    
        half_projected_height = projected_height // 2
        start_y = HALF_HEIGHT - half_projected_height
        start_x += SCALE
        pg.draw.rect(window, (200,200,200), (start_x, start_y, SCALE, projected_height))
