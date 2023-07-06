import pygame
import numpy
import sys
from pygame.locals import *




# Variables du jeu
#player_x = (SCREEN_WIDTH / 2) / 2
#player_y = (SCREEN_WIDTH / 2) / 2

# Map




map = ( 
    '11111111111111111111'
    '10000000000003330001'
    '10011100000000000001'
    '10030000000000000001'
    '10020000000000300001'
    '10020001110000000001'
    '10000330000000000001'
    '10000330000000000001'
    '10000330000000000001'
    '10000330000000000001'
    '10000330000000000001'
    '10000330000000000001'
    '10020000000000300001'
    '10020001110000000001'
    '10000330000000000001'
    '10000330000000000001'
    '10020000000000300001'
    '10020001110000000001'
    '10000330000000000001'
    '11111111111111111111')

# initialisation
def main():
    pygame.init()

    # Definition ecran (constante)

    SCREEN_HEIGHT = 800
    SCREEN_WIDTH = 600
    size = SCREEN_WIDTH, SCREEN_HEIGHT
    MAP_SIZE = 15
    TILE_SIZE = int((SCREEN_WIDTH / 2) / MAP_SIZE)


    screen = pygame.display.set_mode((size))

    # Defines starting position and direction
    positionX = 3.0
    positionY = 7.0

    directionX = 1.0
    directionY = 0.0

    planeX = 0.0
    planeY = 0.66


    # Movement constants   
    ROTATIONSPEED = 0.02
    MOVESPEED = 0.03

    # Trigeometric tuples + variables for index
    TGM = (math.cos(ROTATIONSPEED), math.sin(ROTATIONSPEED))
    ITGM = (math.cos(-ROTATIONSPEED), math.sin(-ROTATIONSPEED))
    COS, SIN = (0,1)



    # Sortie et fin de jeu
    while True :
        for event in pygame.event.get():
             if event.type == QUIT:
                 pygame.quit()
                 sys.exit()
     
        pygame.display.update()

