import pygame
import os
import constant
import sys
pygame.init()

screen = pygame.display.set_mode((constant.screen_width, constant.screen_height - 50), pygame.RESIZABLE)
pygame.display.set_caption("Mermelada")

#DEF para dibujar texto
def draw_text(text, font, color, surface, x, y):
    textobj = constant.font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

#DEF para dibujar botones
def draw_button(text, color, rect, surface):
    pygame.draw.rect(surface, color, rect)
    draw_text(text, constant.font, constant.WHITE, surface, rect.centerx, rect.centery)

def button_click(pos, rect):
    return rect.collidepoint(pos)

def main_menu():
    run = True
    while run:
        # Rectangulo principal
        rect_width_percentage = 0.8
        rect_height_percentage = 0.2
        rect_x_percentage = 0.1
        rect_y_percentage = 0.1
        rect_width = int(constant.screen_width * rect_width_percentage)
        rect_height = int(constant.screen_height * rect_height_percentage)
        rect_x = int(constant.screen_width * rect_x_percentage)
        rect_y = int(constant.screen_height * rect_y_percentage)
        pygame.draw.rect(screen, 'ORANGE', [rect_x, rect_y, rect_width, rect_height])

        # Rectangulo boton 1
        b1_rect_width_percentage = 0.33
        b1_rect_height_percentage = 0.1
        b1_rect_x_percentage = 0.33
        b1_rect_y_percentage = 0.5
        b1_rect_width = int(constant.screen_width * b1_rect_width_percentage)
        b1_rect_height = int(constant.screen_height * b1_rect_height_percentage)
        b1_rect_x = int(constant.screen_width * b1_rect_x_percentage)
        b1_rect_y = int(constant.screen_height * b1_rect_y_percentage)
        play_button_rect = pygame.Rect(b1_rect_x, b1_rect_y, b1_rect_width, b1_rect_height)

        # Rectangulo boton 2
        b2_rect_width_percentage = 0.33
        b2_rect_height_percentage = 0.1
        b2_rect_x_percentage = 0.33
        b2_rect_y_percentage = 0.6
        b2_rect_width = int(constant.screen_width * b2_rect_width_percentage)
        b2_rect_height = int(constant.screen_height * b2_rect_height_percentage)
        b2_rect_x = int(constant.screen_width * b2_rect_x_percentage)
        b2_rect_y = int(constant.screen_height * b2_rect_y_percentage)
        quit_button_rect = pygame.Rect(b2_rect_x, b2_rect_y, b2_rect_width, b2_rect_height)

        # Dibujar botones
        draw_button('JUGAR', constant.BLUE, play_button_rect, screen)
        draw_button('SALIR DEL JUEGO', constant.RED, quit_button_rect, screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if button_click(mouse_pos, play_button_rect):
                    print("Jugar clicado")  # Aquí podrías empezar el juego
                elif button_click(mouse_pos, quit_button_rect):
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()

# Ejecutar el menú principal
main_menu()

pygame.quit()