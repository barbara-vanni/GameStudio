import pygame as pg
import numpy as np
from settings import *


class Player : 
    def __init__(self, x, y) :
        self.position = pg.Vector2(x, y)
        self._angle = 0
        self.speed = 0.002
        self.rotation = 0.002
        self.vector_dir = self.update_dir ()
        

    def movement (self, frame_time, map) :   #CONFIG POUR WASD, pour azerty : 
        KEYS = pg.key.get_pressed()
        mouse = pg.mouse.get_rel()
        pg.mouse.set_visible(False)
        pg.event.set_grab(True)    #Pour que la souris ne sorte pas de l'écran
        rotation = (self.rotation * frame_time)

        if KEYS[pg.K_UP] or KEYS[ord('w')] :   #w par z
            self.move_forward (frame_time, map)
        if KEYS[pg.K_DOWN] or KEYS[ord('s')] :
            self.move_back (frame_time, map) 
        if KEYS[ord('a')]:                      #a par q
            self.move_left(frame_time,map)
        if KEYS[ord('d')]: 
            self.move_right(frame_time,map)
        
        if KEYS[pg.K_LEFT] or mouse[0] < 0 : 
            self.rotate_left (rotation)
        if KEYS[pg.K_RIGHT] or mouse[0] > 0:
            self.rotate_right (rotation)

    def update_dir (self) :
        sin_a = np.sin(self.angle)      
        cos_a = np.cos(self.angle)
        sin_a = sin_a if sin_a else 0.000001
        cos_a = cos_a if cos_a else 0.000001
        return (pg.Vector2(sin_a, cos_a))
    
    def verify_wall (self, new_position, map) :
        if map[int(new_position.y)][int(new_position.x)] == 0:
            self.position = new_position

    def move_forward (self, frame_time, map) :
        new_position = self.position + self.speed * self.vector_dir * frame_time
        self.verify_wall (new_position, map)

    def move_back (self, frame_time, map) :
        new_position = self.position - self.speed * self.vector_dir * frame_time
        self.verify_wall (new_position, map)
    
    #Pour move left et right on calcule le vector dir +- 90° donc ça perpendiculaire positive et négative
    def move_left(self, frame_time, map):    
        perpendicular_dir = pg.Vector2(-self.vector_dir.y, self.vector_dir.x)
        new_position = self.position + perpendicular_dir * self.speed * frame_time
        self.verify_wall(new_position, map)

    def move_right(self, frame_time, map):
        perpendicular_dir = pg.Vector2(self.vector_dir.y, -self.vector_dir.x)
        new_position = self.position + perpendicular_dir * self.speed * frame_time
        self.verify_wall(new_position, map)

    def rotate_left (self, rotation) :
        self.angle -= rotation
        

    def rotate_right (self, rotation) :
        self.angle += rotation

    @property
    def angle(self):
        return self._angle
    
    @angle.setter
    def angle(self,value):
        self._angle = value
        self.vector_dir = self.update_dir ()
