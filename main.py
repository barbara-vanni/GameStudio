import pygame as pg
import sys
from player import *
from raycasting import *
from cell import *


size = RES_X, RES_Y
MAP_SIZE = 20
TILE_SIZE = int((RES_X / 2) / MAP_SIZE)

window = pg.display.set_mode((size))


# map = [
#     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
#     [1,0,0,0,0,0,0,0,0,0,0,0,0,3,3,3,0,0,0,1],
#     [1,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
#     [1,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
#     [1,0,0,2,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,1],
#     [1,0,0,2,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,1],
#     [1,0,0,0,0,3,3,0,0,0,0,0,0,0,0,0,0,0,0,1],
#     [1,0,0,0,0,3,3,0,0,0,0,0,0,0,0,0,0,0,0,1],
#     [1,0,0,0,0,3,3,0,0,0,0,0,0,0,0,0,0,0,0,1],
#     [1,0,0,0,0,3,3,0,0,0,0,0,0,0,0,0,0,0,0,1],
#     [1,0,0,0,0,3,3,0,0,0,0,0,0,0,0,0,0,0,0,1],
#     [1,0,0,0,0,3,3,0,0,0,0,0,0,0,0,0,0,0,0,1],
#     [1,0,0,2,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,1],
#     [1,0,0,2,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,1],
#     [1,0,0,0,0,3,3,0,0,0,0,0,0,0,0,0,0,0,0,1],
#     [1,0,0,0,0,3,3,0,0,0,0,0,0,0,0,0,0,0,0,1],
#     [1,0,0,2,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,1],
#     [1,0,0,2,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,1],
#     [1,0,0,0,0,3,3,0,0,0,0,0,0,0,0,0,0,0,0,1],
#     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
#     ]

# map =  [
#     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
#     [1,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,0,0,0,1],
#     [1,1,1,1,1,1,1,0,1,0,1,0,0,0,1,0,1,1,1,1],
#     [1,0,0,0,0,0,1,0,1,0,0,0,1,0,1,0,0,0,0,1],
#     [1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,1,1,1,0,1],
#     [1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1],
#     [1,1,1,0,1,1,1,0,1,1,1,1,1,1,0,1,0,1,0,1],
#     [1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,1,0,1,0,1],
#     [1,1,1,0,1,1,1,0,1,0,1,1,1,1,0,1,0,0,0,1],
#     [1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,1,1,1,1,1],
#     [1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,0,0,0,1],
#     [1,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,1,0,1],
#     [1,0,1,1,1,0,1,0,1,1,1,0,1,1,1,1,1,1,0,1],
#     [1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,1,0,1],
#     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
# ]

map = []


# initialisation
pg.init()


# Sortie et fin de jeu
clock = pg.time.Clock()

player = Player(8,11)

pg.mouse.set_visible(False)

args = sys.argv
if len(args) < 2 :
    map_file = "game_map"
else :
    map_file = args[1]

try:
    file = open(map_file, "r")
except (FileNotFoundError, IOError, OSError) :
    print("Map file not found.")
    exit()
else :
    for line in file:
        new_table = []
        lineCells = line.strip().split(" ")
        for cells in lineCells:
            params = cells.split(":")
            type = int(params[0])
            params.pop(0)
            new_table.append(Cell.create(type)(params))
        map.append(new_table)


while True :
    for event in pg.event.get():
        if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
            pg.quit()
            sys.exit()
    
    window.fill((0,0,0))

    frame_time = clock.tick()
    player.movement(frame_time, map)
    raycasting(window, map, player)      
    pg.display.flip()
    # pg.display.update()
    pg.display.set_caption("GAME STUDIO FPS : " + str(int(clock.get_fps())))

