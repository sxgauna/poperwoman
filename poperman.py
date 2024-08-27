import pygame
import os
import constant
from personaje import Personaje
from weapons import Weapon

#FUNCIONES
def escalar_img(image,scale):
    w = image.get_width()
    h = image.get_height()
    nueva_imagen = pygame.transform.scale(image, (w * scale, h * scale))
    return nueva_imagen

def contar_elementos(directorio):
    return len(os.listdir(directorio))

def nombre_carpetas(directorio):
    return os.listdir(directorio)



pygame.init()
screen = pygame.display.set_mode((constant.screen_width, constant.screen_height), pygame.RESIZABLE)
pygame.display.set_caption("Poperman")


#IMPORTAR IMAGENES

#Personaje
animaciones = []
for i in range (7):
    img = pygame.image.load(f"assets//images//characters//player1//char{i}.png").convert_alpha()
    img = escalar_img(img, constant.CHAR_ESCALA)
    animaciones.append(img)

#Enemigos
directorio_enemigos = "assets//images//characters//enemies"
tipo_enemigos = nombre_carpetas(directorio_enemigos)
animaciones_enemigo = []
for eni in tipo_enemigos:
    lista_temp = []
    ruta_temp = f"assets//images//characters//enemies//{eni}"
    num_animaciones = contar_elementos(ruta_temp)
    for i in range(num_animaciones):
        img_enemigo = pygame.image.load(f"{ruta_temp}//{eni}_{i + 1}.png").convert_alpha()
        img_enemigo = escalar_img(img_enemigo, constant.ENEMY_ESCALA)
        lista_temp.append(img_enemigo)
    animaciones_enemigo.append(lista_temp)


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

#CREAR ENEMIGO 1 DE CLASE PERSONAJE
enemy1 = Personaje(400, 300, animaciones_enemigo[0])

#CREAR ENEMIGO 2 DE CLASE PERSONAJE
enemy2 = Personaje(200, 200, animaciones_enemigo[1])

#LISTA ENEMIGOS
lista_enemigos = []
lista_enemigos.append(enemy1)
lista_enemigos.append(enemy2)

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
    for ene in lista_enemigos:
        ene.update()

    bala = weapon1.update(player1)
    if bala:
        grupo_balas.add(bala)
    for bala in grupo_balas:
        bala.update()
    print(grupo_balas)


    player1.draw(screen)
    for ene in lista_enemigos:
        ene.draw(screen)
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