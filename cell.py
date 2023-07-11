from settings import *


class Cell :
    def __init__(self, type, params) : 
        self.type = type
        self.color = colors[0]
        if len(params) > 0 :
            self.color = colors[int(params[0])]



