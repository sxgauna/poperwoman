import pygame
import os

pygame.init()

#Configuracion de ventana
os.environ['SDL_VIDEO_CENTERED'] = '1'
info = pygame.display.Info()
screen_width, screen_height = info.current_w, info.current_h

# Definicion de colores
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255,255,0)
BLACK = (0,0,0)

# Fuente para los textos
font = pygame.font.SysFont(None, 55)

#CHARACTER
#CHAR_WIDTH = 20
#CHAR_HEIGHT = 20
CHAR_ESCALA = 0.8

#WEAPON
WEAPON_ESCALA = 0.3

#CONTROL DE MOVIMIENTO
FPS = 60
SPEED = 10

#COOLDOWN_BALAS
COOLDOWN_BALAS = 500
SPEED_BALAS = 100

#ENEMIES
ENEMY_ESCALA = 1

#CORAZON ENERGIA ESCALA
HEART_ESCALA = 0.1

POTION_ESCALA = 0.15
COIN_ESCALA = 0.25

GRID_SIZE = 50

TILE_SIZE = 50
TILE_TYPES = 108

FILAS = 32
COLUMNAS = 40

LIMITE_PANTALLA = 250


#ENEMIGOS
VELOCIDAD_ENEMIGOS = 3
RANGO = 300
RANGO_ATK = 20 #CUANDO ESTEN MAS CERCA DE 20 ME VAN A ATACAR