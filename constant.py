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
CHAR_ESCALA = 1.1

#WEAPON
WEAPON_ESCALA = 0.3

#CONTROL DE MOVIMIENTO
FPS = 60
SPEED = 15

#COOLDOWN_BALAS
COOLDOWN_BALAS = 500
SPEED_BALAS = 30