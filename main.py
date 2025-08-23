import pygame
import random
import sys

pygame.init()
ventana = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Poperwoman")

# Bucle principal del juego
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    pygame.display.update()

pygame.quit()
sys.exit()