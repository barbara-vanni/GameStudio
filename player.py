import pygame as pg
import numpy as np
from settings import *
import settings





def movement(player_angle, player_pos, frame_time) :
    KEYS = pg.key.get_pressed()
    rotation = 0.001 * frame_time

    sin_a = np.sin(player_angle)      
    cos_a = np.cos(player_angle)
    sin_a = sin_a if sin_a else 0.000001
    cos_a = cos_a if cos_a else 0.000001
    vector_dir = (pg.math.Vector2(sin_a*player_angle, cos_a*player_angle))

    if KEYS[pg.K_LEFT] or KEYS[ord('q')] : 
        player_angle -= rotation
        print('test left')
    if KEYS[pg.K_RIGHT] or KEYS[ord('d')] : 
        player_angle += rotation

    if KEYS[pg.K_UP] or KEYS[ord('z')] : 
        player_pos += PLAYER_SPEED * vector_dir * frame_time

    if KEYS[pg.K_DOWN] or KEYS[ord('s')] : 
        player_pos -= PLAYER_SPEED * vector_dir * frame_time

    return player_pos, player_angle

