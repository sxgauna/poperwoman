import pygame
import random
import sys

# 1. Inicializar Pygame
pygame.init()

# 2. Configurar la ventana
ventana = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Poperwoman")

# 3. Bucle principal del juego
game_over = False

while not game_over:
    # 3.1. Procesar eventos (clics, teclas, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # 3.2. Actualizar la pantalla
    # Esta línea es VITAL para que la ventana se refresque y no se congele
    pygame.display.update()

# 4. Salir de Pygame de forma segura
pygame.quit()
sys.exit()