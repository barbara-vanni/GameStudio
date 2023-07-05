import pygame
import sys
pygame.init()

# Definition ecran
size = 800,600
screen = pygame.display.set_mode(size)



# Sortie et fin de jeu
while True :
    for event in pygame.event.get():
        if event.type == quit:
            pygame.quit()
            sys.exit()
    pygame.display.update()

