import pygame as pg
import sys
from player import *
from raycasting import *
from cell import *
from numba import njit


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
pg.mouse.set_visible(False)
pg.event.set_grab(True)    #Pour que la souris ne sorte pas de l'écran


# Sortie et fin de jeu
clock = pg.time.Clock()

player = Player(8,11)



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
            new_table.append(Cell(type, params))
        map.append(new_table)
print (map)

while 1 :
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

@njit()
def new_frame(posx, posy, rot, frame, hres, floor, sky, halfvres, mod, maph, size):
    for i in range(hres):
        rot_i = rot + np.deg2rad(i/mod - 30)
        sin, cos, cos2 = np.sin(rot_i), np.cos(rot_i), np.cos(np.deg2rad(i/mod - 30))
        frame[i][:] = sky[int(np.rad2deg(rot_i)%359)][:]/255
        for j in range(halfvres):
            n = (halfvres/(halfvres-j))/cos2
            x, y = posx + cos*n, posy + sin*n
            scaler = 30/5
            xx, yy = int(x/scaler%1*100), int (y/scaler%1*100)

            shade = 0.2 + 0.8*(1-j/halfvres)

            if maph[int(x)%(size-1)][int(y)%(size-1)]:
                h = halfvres - j
                c = shade*np.ones(3)
                for k in range(h*2):
                    frame[i][halfvres - h +k] = c
                break
            
            else:
                frame[i][halfvres*2-j-1] = shade*floor[xx][yy]/255

    return frame