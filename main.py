import pygame
import sys



# Definition ecran (constante)

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 600
size = SCREEN_WIDTH, SCREEN_HEIGHT
MAP_SIZE = 15
TILE_SIZE = int((SCREEN_WIDTH / 2) / MAP_SIZE)

# Variables du jeu
#player_x = (SCREEN_WIDTH / 2) / 2
#player_y = (SCREEN_WIDTH / 2) / 2

# Map


win = pygame.display.set_mode((size))



def draw_map():
    # loop over map rows
    for row in range(20):
        # loop over map columns
        for col in range(20):
            # calculate square index
            square = row * MAP_SIZE + col
            
            # draw map in the game window
            pygame.draw.rect(
                win,
                colortable[int(map[square])],

                #(200, 200, 200) if map[square] == '1' else (100, 100, 100),
                (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE - 2, TILE_SIZE - 2)
            )


colortable = [
    (255,85,51),
    (200,200,200),
    (100,100,100),
    (76,0,230)
]

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
pygame.init()



# Sortie et fin de jeu
while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    draw_map()      

    pygame.display.update()

