import pygame as pg
import numpy as np

#Ecran
RES_X = 1920
RES_Y = 1080
SIZE = RES_X, RES_Y
HALF_WIDTH = RES_X // 2
HALF_HEIGHT = RES_Y // 2


#Gestion du joueur
PLAYER_POS_INIT = pg.math.Vector2(2,5) #Position Initiale du joueur
PLAYER_SPEED = 4    #Vitesse de déplacement du joueur
player_pos = PLAYER_POS_INIT  #Position du joueur actuelle
player_angle = 0     #angle de vue du joueur


#Raycasting settings
FOV = np.pi / 3  # Approx 60 degrès
HALF_FOV = FOV / 2   #Approx 30 degrès
NUM_RAYS = 80   #Nombre de rayons lancées pour le Raycasting
RAY_SPEED = 0.005  #Vitesse de déplacements des rayons (pas vers direction)
SCALE = RES_X // NUM_RAYS  # must result in a whole integer number otherwise rendering cutoff happens

DIST = NUM_RAYS / (2 * np.tan(HALF_FOV)) #Je ne comprends pas trop celle là
WALL_HEIGHT = 4 * DIST * 100  #Taille des murs (100 était avant la constante echelle,
                              #  a voir si on en a vraiment besoin et trouver un bon nommage)

# texture settings
TEXTURE_WIDTH = 1000
TEXTURE_HEIGHT = 1000
TEXTURE_SCALE = TEXTURE_WIDTH // 100 #Pareil que pour wall_height




#Si on veut afficher la map 2D (Pour la minimap)

MAP_SIZE = 20
TILE_SIZE = int((RES_X / 2) / MAP_SIZE)