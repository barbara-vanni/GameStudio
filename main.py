import pygame
import sys
from player import *
from raycasting2 import *


# Definition ecran (constante)

# SCREEN_HEIGHT = 800
# SCREEN_WIDTH = 800
size = RES_X, RES_Y
MAP_SIZE = 20
TILE_SIZE = int((RES_X / 2) / MAP_SIZE)

window = pygame.display.set_mode((size))


map = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,3,3,3,0,0,0,1],
    [1,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,2,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,1],
    [1,0,0,2,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,3,3,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,3,3,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,3,3,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,3,3,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,3,3,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,3,3,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,2,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,1],
    [1,0,0,2,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,3,3,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,3,3,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,2,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,1],
    [1,0,0,2,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,3,3,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    ]




# initialisation
pygame.init()


# Sortie et fin de jeu
clock = pygame.time.Clock()

while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()
    
    window.fill((100,100,100))
    pygame.display.flip()

    frame_time = clock.tick()
    movement(player_angle, player_pos, frame_time)
    raycasting(window, map)      

    pygame.display.update()

