import pygame
import os
import constant
import csv
from text import DamageText
from personaje import Personaje
from weapons import Weapon
from items import Item
from world import Mundo

def escalar_img(image,scale):
    w = image.get_width()
    h = image.get_height()
    nueva_imagen = pygame.transform.scale(image, (w * scale, h * scale))
    return nueva_imagen

def contar_elementos(directorio):
    return len(os.listdir(directorio))

def nombre_carpetas(directorio):
    return os.listdir(directorio)

def vida_jugador():
    c_mitad_dibujado = False
    for i in range(4):
        if player1.energy >= ((i+1)*25):
            screen.blit(corazon_lleno, (5+i*50,15))
        elif player1.energy % 25 > 0:
            screen.blit(corazon_mitad, (5+i*50,15))
            c_mitad_dibujado = True
        else:
            screen.blit(corazon_vacio, (5+i*50,15))

def resetear_mundo():
    screen.fill(constant.BLACK)
    grupo_damage_text.empty()
    grupo_balas.empty()
    grupo_items.empty()

    player1.score = 0
    player1.energy = 100

    data = []
    for fila in range(constant.FILAS):
        filas = [2] * constant.COLUMNAS
        data.append(filas)
    return data


def dibujar_texto(texto, fuente, color, x, y):
    img = fuente.render(texto, True, color)
    screen.blit(img, (x,y))

def pantalla_inicio():
    screen.fill(constant.BLACK)
    dibujar_texto("Midnight Popcorn", font_titulo, constant.RED,
            constant.screen_width / 2 - font_titulo.size("Midnight Popcorn")[0] / 2,
            constant.screen_height / 2 - 300)
    pygame.draw.rect(screen, constant.ROJO_OSCURO, boton_jugar)
    pygame.draw.rect(screen, constant.ROJO_OSCURO, boton_salir)
    screen.blit(texto_boton_jugar, (boton_jugar.x + 50, boton_jugar.y + 10))
    screen.blit(texto_boton_salir, (boton_salir.x + 50, boton_salir.y + 10))
    pygame.display.update()

def pantalla_fin():
    pause = True
    screen.fill(constant.BLACK)
    dibujar_texto("Epic! You won!", font_titulo, constant.RED,
            constant.screen_width / 2 - font_titulo.size("Epic! You won!")[0] / 2,
            constant.screen_height / 2 - 300)
    pygame.display.update()

def pantalla_muerte():
    screen.fill(constant.ROJO_OSCURO)
    text_rect = game_over_text.get_rect(center=(constant.screen_width / 2, constant.screen_height / 2 - 300))

    pygame.draw.rect(screen, constant.BLACK, boton_reinicio)
    pygame.draw.rect(screen, constant.BLACK, boton_salir)

    screen.blit(game_over_text, text_rect)
    screen.blit(texto_boton_reinicio, (boton_reinicio.x + 50, boton_reinicio.y + 10))
    screen.blit(texto_boton_salir, (boton_salir.x + 50, boton_salir.y + 10))
    pygame.display.update()

#INIT
pygame.init()
pygame.mixer.init()

font = pygame.font.Font("assets//fonts//font1.otf", 35)
font_game_over = pygame.font.Font("assets//fonts//font1.otf", 80)
font_reinicio = pygame.font.Font("assets//fonts//font1.otf", 30)
font_inicio = pygame.font.Font("assets//fonts//font1.otf",30)
font_titulo = pygame.font.Font("assets//fonts//font2.ttf",80)

game_over_text = font_game_over.render('YOU ARE DEAD!', True, constant.WHITE)
texto_boton_reinicio = font_reinicio.render('RESET', True, constant.WHITE)
texto_boton_jugar = font_inicio.render('PLAY', True, constant.WHITE)
texto_boton_salir = font_inicio.render('QUIT', True, constant.WHITE)


#BUTTONS
boton_jugar = pygame.Rect(constant.screen_width / 2 - 100,
                            constant.screen_height/2 - 50, 200, 50)

boton_salir = pygame.Rect(constant.screen_width/2 - 100,
                             constant.screen_height/2 + 50, 200,50)

screen = pygame.display.set_mode((constant.screen_width, constant.screen_height), pygame.RESIZABLE)
pygame.display.set_caption("Midnight Popcorn")
posicion_pantalla = [0, 0]
nivel = 1

#ITEMS
tile_list = []
for i in range (constant.TILE_TYPES):
    tile_image = pygame.image.load(f"assets//images//tiles//tile ({ i }).png")
    tile_image = pygame.transform.scale(tile_image, (constant.TILE_SIZE, constant.TILE_SIZE))
    tile_list.append(tile_image)


poti_roja = pygame.image.load("assets//images//items//potion//p1.png")
poti_roja = escalar_img(poti_roja, 0.05)
coin_images = []
ruta_img = "assets//images//items//coins"
num_coin_images = contar_elementos(ruta_img)
for i in range(num_coin_images):
    img = pygame.image.load(f"assets//images//items//coins//c{i+1}.png")
    img = escalar_img(img, 0.1)
    coin_images.append(img)

item_imagenes = [coin_images, [poti_roja]]

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

#WORLD
world_data = []

#TILE DEFAULT
for fila in range(constant.FILAS):
    filas =  [5] * constant.COLUMNAS
    world_data.append(filas)

with open("assets//images//levels//level1.csv", newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for x, fila in enumerate(reader):
        for y, columna in enumerate(fila):
            world_data[x][y] = int(columna)

world = Mundo()
world.process_data(world_data, tile_list, item_imagenes, animaciones_enemigo)

#SPRITES
animaciones = []
for i in range (7):
    img = pygame.image.load(f"assets//images//characters//player1//char{i}.png").convert_alpha()
    img = escalar_img(img, constant.CHAR_ESCALA)
    animaciones.append(img)



imagen_pistola = pygame.image.load(f"assets//images//weapons//weapon1.png").convert_alpha()
imagen_pistola = escalar_img(imagen_pistola, constant.WEAPON_ESCALA)

imagen_bala = pygame.image.load(f"assets//images//weapons//pop.png").convert_alpha()
imagen_bala = escalar_img(imagen_bala, constant.WEAPON_ESCALA)

corazon_vacio = pygame.image.load(f"assets//images//items//h0.png").convert_alpha()
corazon_vacio = escalar_img(corazon_vacio, constant.HEART_ESCALA)
corazon_mitad = pygame.image.load(f"assets//images//items//h1.png").convert_alpha()
corazon_mitad = escalar_img(corazon_mitad, constant.HEART_ESCALA)
corazon_lleno = pygame.image.load(f"assets//images//items//h2.png").convert_alpha()
corazon_lleno = escalar_img(corazon_lleno, constant.HEART_ESCALA)


#GROUPS

grupo_damage_text = pygame.sprite.Group() # TEXTO - DAMAGE TEXT
grupo_balas = pygame.sprite.Group()
grupo_items = pygame.sprite.Group()

for item in world.lista_item:
    grupo_items.add(item)


#CLASSES
weapon1 = Weapon(imagen_pistola, imagen_bala)
player1 = Personaje(150, 150, animaciones, 100, 1)

lista_enemigos = []
for ene in world.lista_enemigo:
    lista_enemigos.append(ene)


#MOVE
move_up = False
move_down = False
move_right = False
move_left = False
clock = pygame.time.Clock()

boton_reinicio = pygame.Rect(constant.screen_width / 2 - 100,
                            constant.screen_height/2 - 50, 200, 50)

#MUSIC

pygame.mixer.music.load("assets/music/Level1.mp3")
pygame.mixer.music.play(-1)

sonido_disparo = pygame.mixer.Sound("assets/sounds/s1.mp3")


#RUN

mostrar_inicio = True
pause = False

run = True
while run:
    if mostrar_inicio:
        pantalla_inicio()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if boton_jugar.collidepoint(event.pos):
                    mostrar_inicio = False
                if boton_salir.collidepoint(event.pos):
                    run = False


        clock.tick(constant.FPS)
        screen.fill(constant.BLACK)

    else:

        if player1.vivo:
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

            posicion_pantalla, nivel_completado = player1.move(delta_x, delta_y, world.obstaculos_tiles, world.exit_tile) #MOVER AL JUGADOR

            # U P D A T E
            world.update(posicion_pantalla)

            player1.update()

            for ene in lista_enemigos:
                ene.enemigos(player1, world.obstaculos_tiles, posicion_pantalla, world.exit_tile)
                ene.update()

            bala = weapon1.update(player1)


            if bala:
                grupo_balas.add(bala)
                sonido_disparo.play()
            for bala in grupo_balas:
                damage, pos_damage = bala.update(lista_enemigos, world.obstaculos_tiles)
                if damage:
                    if damage <= 53:
                        damage_text = DamageText(pos_damage.centerx, pos_damage.centery, "-" + str(damage), font, constant.YELLOW)
                    else:
                        damage_text = DamageText(pos_damage.centerx, pos_damage.centery, "-" + str(damage) + " CRITICAL HIT ", font, constant.RED)
                    grupo_damage_text.add(damage_text)
            grupo_damage_text.update(posicion_pantalla)
            grupo_items.update(posicion_pantalla, player1)

        #DRAW

        world.draw(screen)

        player1.draw(screen)

        for ene in lista_enemigos:
            if ene.energy ==0:
                lista_enemigos.remove(ene)
            if ene.energy >0:
                ene.draw(screen)



        weapon1.draw(screen)
        for bala in grupo_balas:
            bala.draw(screen)
        grupo_damage_text.draw(screen)

        vida_jugador()

        dibujar_texto(f"Score: {player1.score}", font, constant.BLUE, 1000, 5 )
        grupo_items.draw(screen)

        #CHEQUEA SI EL NIVEL ESTÁ COMPLETADO
        if nivel_completado == True:
            if nivel < constant.NIVEL_MAXIMO:
                nivel += 1
                dibujar_texto(f"Nivel: " + str(nivel), font, constant.WHITE, constant.screen_width /2, 5)
                world_data = resetear_mundo()

                #CARGA MUNDO LUEGO DE RESETEO
                with open(f"assets//images//levels//level{nivel}.csv", newline='') as csvfile:
                    reader = csv.reader(csvfile, delimiter=',')
                    for x, fila in enumerate(reader):
                        for y, columna in enumerate(fila):
                            world_data[x][y] = int(columna)
                world = Mundo()
                screen.fill(constant.BLACK)
                world.process_data(world_data, tile_list, item_imagenes, animaciones_enemigo)
                player1.actualizar_coordinadas((constant.COORDENADAS_SPAWN[str(nivel)]))

                lista_enemigos = []
                for ene in world.lista_enemigo:
                    lista_enemigos.append(ene)
                for item in world.lista_item:
                     grupo_items.add(item)
            else:
                pantalla_fin()

        #REVISAR

        if player1.vivo == False:
            pantalla_muerte()


        # E V E N T S
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            elif (pause == False) and (event.type == pygame.KEYDOWN):
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    move_left = True
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    move_right = True
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    move_up = True
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    move_down = True
                if event.key == pygame.K_e:
                    world.cambiar_puerta(player1, tile_list)

            elif (pause == False) and (event.type == pygame.KEYUP):
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    move_left = False
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    move_right = False
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    move_up = False
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    move_down = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Solo el botón izquierdo del ratón
                    if boton_reinicio.collidepoint(event.pos) and not player1.vivo:
                        player1.vivo =True
                        player1.energy = 100
                        player1.score =0
                        nivel = 1
                        world_data = resetear_mundo()

                        #CARGA MUNDO LUEGO DE RESETEO
                        with open(f"assets//images//levels//level{nivel}.csv", newline='') as csvfile:
                            reader = csv.reader(csvfile, delimiter=',')
                        for x, fila in enumerate(reader):
                            for y, columna in enumerate(fila):
                                world_data[x][y] = int(columna)

                                world = Mundo()
                                world.process_data(world_data, tile_list, item_imagenes, animaciones_enemigo)
                                player1.actualizar_coordinadas(constant.COORDENADAS_SPAWN[str(nivel)])

                        # Reinicia la lista de enemigos y objetos
                        lista_enemigos = []
                        for ene in world.lista_enemigo:
                            lista_enemigos.append(ene)
                        grupo_items.empty()  # Limpia el grupo antes de agregar nuevos items
                        for item in world.lista_item:
                            grupo_items.add(item)
        pygame.display.update()

pygame.quit()