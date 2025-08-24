import pygame
import random
import sys
from menu import menu_inicio

pygame.init()
ventana = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Poperwoman")
fuente_titulo = pygame.font.Font("assets/fonts/CinemaOutfitDEMO-Regular.otf", 80)
fuente_botones = pygame.font.Font("assets/fonts/CinemaOutfitDEMO-Regular.otf", 40)

#Menú
menu_inicio(ventana, fuente_titulo, fuente_botones)

# Bucle principal del juego
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    pygame.display.update()

    ventana.fill((30,30,30))
    render = fuente_botones.render("Test.", True, (255, 255, 255))
    rect = render.get_rect(center=(ventana.get_width() // 2, ventana.get_height() // 2))
    ventana.blit(render, rect)

    pygame.display.update()

pygame.quit()
sys.exit()