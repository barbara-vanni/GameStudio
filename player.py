import pygame as pg
import numpy as np
from settings import *
from cell import *

class Player : 
    def __init__(self, x, y) :
        self.position = pg.Vector2(x, y)
        self._angle = 0
        self.speed = 0.002
        self.rotation = 0.001 
        self.vector_dir = self.update_dir ()
        

    def movement (self, frame_time, map) :
        KEYS = pg.key.get_pressed()
        mouse = pg.mouse.get_rel()
        rotation = (self.rotation * frame_time)
        if KEYS[pg.K_LEFT] or KEYS[ord('q')] or mouse[0] < 0 : 
            self.rotate_left (rotation)  
        if KEYS[pg.K_RIGHT] or KEYS[ord('d')] or mouse[0] > 0: 
            self.rotate_right (rotation)
        if KEYS[pg.K_UP] or KEYS[ord('z')] :
            self.move_forward (frame_time, map)
        if KEYS[pg.K_DOWN] or KEYS[ord('s')] :
            self.move_back (frame_time, map) 
     
    def update_dir (self) :
        sin_a = np.sin(self.angle)      
        cos_a = np.cos(self.angle)
        sin_a = sin_a if sin_a else 0.000001
        cos_a = cos_a if cos_a else 0.000001
        return (pg.math.Vector2(sin_a, cos_a))
    
    def verify_wall (self, new_position, map) :
        if map[int(new_position.y)][int(new_position.x)].type == Cell_type.FLOOR:
            self.position = new_position

    def move_forward (self, frame_time, map) :
        new_position = self.position + self.speed * self.vector_dir * frame_time
        self.verify_wall (new_position, map)
        # self.position.x += self.speed * self.vector_dir.x * frame_time
        # self.position.y += self.speed * self.vector_dir.y * frame_time

    
    def move_back (self, frame_time, map) :
        new_position = self.position - self.speed * self.vector_dir * frame_time
        self.verify_wall (new_position, map)
        # self.position.x -= self.speed * self.vector_dir.x * frame_time
        # self.position.y -= self.speed * self.vector_dir.y * frame_time

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
