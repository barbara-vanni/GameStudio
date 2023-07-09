import pygame as pg
import numpy as np

#Ecran
RES_X = 1920
RES_Y = 1080
HALF_WIDTH = RES_X // 2
HALF_HEIGHT = RES_Y // 2


#Gestion du joueur
PLAYER_POS_INIT = pg.math.Vector2(1,1) #Position Initiale du joueur
PLAYER_SPEED = 4    #Vitesse de déplacement du joueur
player_pos = PLAYER_POS_INIT  #Position du joueur actuelle
player_angle = 0     #angle de vue du joueur


#Raycasting settings
FOV = np.pi / 3  # Approx 60 degrès
HALF_FOV = FOV / 2   #Approx 30 degrès
NUM_RAYS = 80   #Nombre de rayons lancées pour le Raycasting
RAY_SPEED = 0.005  #Vitesse de déplacements des rayons (pas vers direction)
SCALE = RES_X // NUM_RAYS  # must result in a whole integer number otherwise rendering cutoff happens

WALL_HEIGHT = 4 * DIST * ECHELLE  #Taille des murs

# texture settings
TEXTURE_WIDTH = 1000
TEXTURE_HEIGHT = 1000
TEXTURE_SCALE = TEXTURE_WIDTH // ECHELLE
