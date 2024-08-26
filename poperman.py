import pygame
import os
import constant
from personaje import Personaje
from weapons import Weapon

pygame.init()
screen = pygame.display.set_mode((constant.screen_width, constant.screen_height), pygame.RESIZABLE)
pygame.display.set_caption("Poperman")

def escalar_img(image,scale):
    w = image.get_width()
    h = image.get_height()
    nueva_imagen = pygame.transform.scale(image, (w * scale, h * scale))
    return nueva_imagen

#IMPORTAR IMAGENES

#Personaje
animaciones = []
for i in range (7):
    img = pygame.image.load(f"assets//images//characters//player1//char{i}.png").convert_alpha()
    img = escalar_img(img, constant.CHAR_ESCALA)
    animaciones.append(img)

#Weapon
imagen_pistola = pygame.image.load(f"assets//images//weapons//weapon1.png").convert_alpha()
imagen_pistola = escalar_img(imagen_pistola, constant.WEAPON_ESCALA)

#Bullets
imagen_bala = pygame.image.load(f"assets//images//weapons//pop.png").convert_alpha()
imagen_bala = escalar_img(imagen_bala, constant.WEAPON_ESCALA)



#CREAR ARMA DE CLASE WEAPON
weapon1 = Weapon(imagen_pistola, imagen_bala)

#CREAR GRUPO DE SPRITES PARA BALAS
grupo_balas = pygame.sprite.Group()


#CREAR JUGADOR DE CLASE PERSONAJE
player1 = Personaje(200, 500, animaciones)

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
    player1.move(delta_x, delta_y)

    player1.update()
    bala = weapon1.update(player1)
    if bala:
        grupo_balas.add(bala)
    for bala in grupo_balas:
        bala.update()
    print(grupo_balas)


    player1.draw(screen)
    weapon1.draw(screen)

    for bala in grupo_balas:
        bala.draw(screen)


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