<<<<<<< Updated upstream
import pygame
from pygame.locals import QUIT

pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption('Basic Pygame program')


# Initialise screen
while True :
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
=======
>>>>>>> Stashed changes
