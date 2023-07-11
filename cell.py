from settings import *
from enum import Enum


class Cell_type(Enum) : 
    FLOOR = 0,
    WALL = 1

class Cell :
    def __init__(self, params) : 
        pass
    
    @staticmethod
    def create(type) :
        return [subclass for subclass in Cell.__subclasses__() if subclass._type == Cell_type(type)][0]

class Wall(Cell) :
    type = 1
    def __init__(self, params) : 
        super(params)
        self.color = colors[0]
        if len(params) > 0 :
            self.color = colors[int(params[0])]   

class Floor(Cell) :
    type = 0 
    def __init__(self, params) : 
        super(params)
        


