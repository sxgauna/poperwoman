import pygame
import os
import constant
from personaje import Personaje

pygame.init()
screen = pygame.display.set_mode((constant.screen_width, constant.screen_height - 50), pygame.RESIZABLE)
player1 = Personaje(50, 50)
pygame.display.set_caption("Poperman")

#Definimos variables movimiento del jugador
move_up = False
move_down = False
move_right = False
move_left = False
clock = pygame.time.Clock()

run = True

while run:
    clock.tick(constant.FPS)
    screen.fill(constant.BLACK)

    #Movimiento del jugador
    delta_x = 0
    delta_y = 0

    if move_right:
        delta_x = constant.SPEED

    if move_left:
        delta_x = -constant.SPEED

    if move_up:
        delta_y = -constant.SPEED

    if move_down:
        delta_y = constant.SPEED

    #MOVER AL JUGADOR
    print(f"{delta_x},{delta_y}")
    player1.move(delta_x, delta_y)
    player1.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                move_left = True
            if event.key == pygame.K_d:
                move_right = True
            if event.key == pygame.K_w:
                move_up = True
            if event.key == pygame.K_s:
                move_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                move_left = False
            if event.key == pygame.K_d:
                move_right = False
            if event.key == pygame.K_w:
                move_up = False
            if event.key == pygame.K_s:
                move_down = False
    pygame.display.update()


pygame.quit()