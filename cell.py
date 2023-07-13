from settings import *
from enum import Enum
import pygame as pg


class Cell_type(Enum) : 
    FLOOR = 0
    WALL = 1

class Cell :
    def __init__(self, params) :
        pass
    
    @staticmethod
    def create(type) :
        return [subclass for subclass in Cell.__subclasses__() if subclass.type == Cell_type(type)][0]

class Wall(Cell) :
    type = Cell_type.WALL
    def __init__(self, params) : 
        super().__init__(params)
        self.color = colors[0]
        if len(params) > 0 :
            self.color = colors[int(params[0])]   

class Floor(Cell) :
    type = Cell_type.FLOOR
    def __init__(self, params) : 
        super().__init__(params)
        self.color = colors[0]
        if len(params) > 0 :
            self.color = colors[int(params[0])]  


