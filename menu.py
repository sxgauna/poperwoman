import pygame
import sys

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (50, 100, 255)
ROJO = (200, 50, 50)



def texto_centrado(texto, fuente, color, superficie, x, y):
    render = fuente.render(texto, True, color)
    rect = render.get_rect(center=(x, y))
    superficie.blit(render, rect)

def menu_inicio(ventana, fuente_titulo, fuente_botones):
    en_menu = True
    while en_menu:
        ventana.fill(NEGRO)

        # Título
        texto_centrado("Poperwoman", fuente_titulo, BLANCO, ventana, 640, 200)

        # Botones
        pygame.draw.rect(ventana, AZUL, (490, 300, 300, 80))   # Jugar
        pygame.draw.rect(ventana, AZUL, (490, 400, 300, 80))   # Opciones
        pygame.draw.rect(ventana, ROJO, (490, 500, 300, 80))   # Salir

        # Texto centrado en los botones
        texto_centrado("New Game", fuente_botones, BLANCO, ventana, 640, 340)      # 300 + 40 # Jugar
        texto_centrado("Options", fuente_botones, BLANCO, ventana, 640, 440)   # 400 + 40 # Opciones
        texto_centrado("Quit", fuente_botones, BLANCO, ventana, 640, 540)      # 500 + 40 # Salir


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Solo clic izquierdo
                    x, y = event.pos
                    if 490 <= x <= 790 and 300 <= y <= 380:  # 300 / 340 / 380 # Jugar
                        en_menu = False
                    if 490 <= x <= 790 and 400 <= y <= 480:  # 400 / 440 / 480 # Opciones
                        en_menu = False
                    if 490 <= x <= 790 and 500 <= y <= 580:  # 500 / 540 / 580 # Salir
                        pygame.quit()
                        sys.exit()

        pygame.display.update()
