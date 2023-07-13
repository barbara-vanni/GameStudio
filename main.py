import pygame as pg
import sys
from player import *
from cell import *
from game import *

size = RES_X, RES_Y
MAP_SIZE = 20
TILE_SIZE = int((RES_X / 2) / MAP_SIZE)

window = pg.display.set_mode((size))
game = Game()

map = []

# initialisation
pg.init()
pg.mouse.set_visible(False)
pg.event.set_grab(True)    #Pour que la souris ne sorte pas de l'écran

# Sortie et fin de jeu
clock = pg.time.Clock()

player = Player(8,11)
# floor = Floor()



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

while 1 :
    for event in pg.event.get():
        if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
            pg.quit()
            sys.exit()
    
    window.fill((0,0,0))

    frame_time = clock.tick()
    player.movement(frame_time, map)
    game.raycasting(window, map, player)      
    pg.display.flip()
    # pg.display.update()
    pg.display.set_caption("GAME STUDIO FPS : " + str(int(clock.get_fps())))

