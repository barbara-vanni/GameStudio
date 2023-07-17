import pygame as pg
import numpy as np
from settings import *
from cell import *

class Player : 
    def __init__(self, x, y) :
        self.position = pg.Vector2(x, y)
        self._angle = 0
        self.speed = 0.002
        self.rotation = 0.003
        self.update_cos_sin()
        self.vector_dir = self.update_dir ()
        self.perpendicular_dir = self.update_perpendicular_dir()
        

    def movement (self, frame_time, map) :   #CONFIG POUR WASD, pour azerty : 
        KEYS = pg.key.get_pressed()
        mouse = pg.mouse.get_rel()
        rotation = (self.rotation * frame_time)

        if KEYS[pg.K_UP] or KEYS[ord('z')] :   #w par z
            self.move_forward (frame_time, map)
        if KEYS[pg.K_DOWN] or KEYS[ord('s')] :
            self.move_back (frame_time, map) 
        if KEYS[ord('q')]:                      #a par q
            self.move_left(frame_time,map)
        if KEYS[ord('d')]: 
            self.move_right(frame_time,map)
        
        if KEYS[pg.K_LEFT] or mouse[0] < 0 : 
            self.rotate_left (rotation)
        if KEYS[pg.K_RIGHT] or mouse[0] > 0:
            self.rotate_right (rotation)
    
    def update_cos_sin(self):
        self.sin_a = np.sin(self.angle)      
        self.cos_a = np.cos(self.angle)
        self.sin_a = self.sin_a if self.sin_a else 0.000001
        self.cos_a = self.cos_a if self.cos_a else 0.000001

    def update_dir (self) :
        return pg.Vector2(self.sin_a, self.cos_a)
    
    def update_perpendicular_dir(self):
        return pg.Vector2(- self.cos_a, self.sin_a)


    def verify_wall_ancien(self, distance_max, map):
        hit = False
        distance_x = 0
        distance_y = 0
        hit_x = False
        hit_y = False
        step = 0.1
        step_x = self.vector_dir.x * step
        step_y = self.vector_dir.y * step
        projected_ray = self.position.copy()
        
        while not hit and distance_x < distance_max.x and distance_y < distance_max.y:
            projected_ray.x += step_x
            distance_x += step
            cell = map[int(projected_ray.y)][int(projected_ray.x)]
            if cell.type == Cell_type.WALL :
                hit_x = True
            self.position.x = projected_ray.x
        
            projected_ray.y += step_y
            distance_y += step
            cell = map[int(projected_ray.y)][int(projected_ray.x)]
            if cell.type == Cell_type.WALL :
                hit_y = True
            self.position.y = projected_ray.y
 


    def move_forward (self, frame_time, map) :
        #self.verify_wall(self.vector_dir * self.speed * frame_time, map)
        if map[int(self.position.x + self.vector_dir.x * self.speed * frame_time)][int(self.position.y)].type == Cell_type.FLOOR :
            self.position.x += self.vector_dir.x * self.speed * frame_time
        if map[int(self.position.x)][int(self.position.y + self.vector_dir.y * self.speed * frame_time)].type == Cell_type.FLOOR :
            self.position.y += self.vector_dir.y * self.speed * frame_time
            
        
    
    def move_back (self, frame_time, map) :
        #self.verify_wall(-self.vector_dir * self.speed * frame_time, map)  
        if map[int(self.position.x - self.vector_dir.x * self.speed * frame_time)][int(self.position.y)].type == Cell_type.FLOOR :
            self.position.x -= self.vector_dir.x * self.speed * frame_time
        if map[int(self.position.x)][int(self.position.y - self.vector_dir.y * self.speed * frame_time)].type == Cell_type.FLOOR :
            self.position.y -= self.vector_dir.y * self.speed * frame_time
    
    #Pour move left et right on calcule le vector dir +- 90° donc ça perpendiculaire positive et négative
    def move_left(self, frame_time, map):    
        pass

    def move_right(self, frame_time, map):
        pass

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
        self.update_cos_sin()
        self.vector_dir = self.update_dir ()
        self.perpendicular_dir = self.update_perpendicular_dir()
    
    