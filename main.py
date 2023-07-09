import pygame
import sys
from raycasting import *
from settings import *
from map import *


# Definition ecran (constante)
window = pygame.display.set_mode(SIZE)

# initialisation
pygame.init()

# Sortie et fin de jeu
while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()
    raycasting(window, map)      
    pygame.display.update()

