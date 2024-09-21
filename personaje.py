import pygame
import constant
import math

class Personaje():
    def __init__(self, x, y, animaciones, energy, tipo):
        self.score = 0
        self.energy = energy
        self.vivo = True
        self.flip = False #La idea es que el personaje se voltee si camina hacia la izquierda

        self.animaciones = animaciones
        #Imagen de animación que se muestra actualmente
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.image = animaciones[self.frame_index]

        self.shape = self.image.get_rect()
        self.shape.center = (x,y)
        self.tipo = tipo

        self.golpe = False
        self.ultimo_golpe = pygame.time.get_ticks()


    def actualizar_coordinadas(self,tupla):
        self.shape.center = (tupla[0], tupla[1])

    def move(self, delta_x, delta_y, obstaculos_tiles, exit_tile):
        posicion_pantalla = [0, 0]
        nivel_completado = False

        if delta_x < 0 :
            self.flip = True
        if delta_x > 0 :
            self.flip = False

        self.shape.x = self.shape.x + delta_x
        for obstacle in obstaculos_tiles:
            if obstacle[1].colliderect(self.shape):
                if delta_x > 0:
                    self.shape.right = obstacle[1].left
                if delta_x < 0:
                    self.shape.left = obstacle[1].right

        self.shape.y = self.shape.y + delta_y
        for obstacle in obstaculos_tiles:
            if obstacle[1].colliderect(self.shape):
                if delta_y > 0:
                    self.shape.bottom = obstacle[1].top
                if delta_y < 0:
                    self.shape.top = obstacle[1].bottom


        #Mueve la cámara de acuerdo a la posición del personaje
        if self.tipo == 1:
            #chequea colision con tile de salida.
            if exit_tile is not None and len(exit_tile) > 1 and exit_tile[1].colliderect(self.shape):
                nivel_completado = True

            # Verificar límite derecho
            if self.shape.right > (constant.screen_width - constant.LIMITE_PANTALLA):
                posicion_pantalla[0] = (constant.screen_width - constant.LIMITE_PANTALLA) - self.shape.right
                self.shape.right = constant.screen_width - constant.LIMITE_PANTALLA

            # Verificar límite izquierdo
            if self.shape.left < constant.LIMITE_PANTALLA:
                posicion_pantalla[0] = constant.LIMITE_PANTALLA - self.shape.left
                self.shape.left = constant.LIMITE_PANTALLA

            # Verificar límite inferior
            if self.shape.bottom > (constant.screen_height - constant.LIMITE_PANTALLA):
                posicion_pantalla[1] = (constant.screen_height - constant.LIMITE_PANTALLA) - self.shape.bottom
                self.shape.bottom = constant.screen_height - constant.LIMITE_PANTALLA

            # Verificar límite superior
            if self.shape.top < constant.LIMITE_PANTALLA:
                posicion_pantalla[1] = constant.LIMITE_PANTALLA - self.shape.top
                self.shape.top = constant.LIMITE_PANTALLA
            return posicion_pantalla, nivel_completado

    def enemigos(self, jugador, obstaculos_tiles, posicion_pantalla, exit_tile):
        clipped_line = []
        ene_dx = 0
        ene_dy = 0

        self.shape.x += posicion_pantalla[0]
        self.shape.y += posicion_pantalla[1]

        #LINEA DE VISION
        linea_de_vision = ((self.shape.centerx, self.shape.centery),
                            (jugador.shape.centerx, jugador.shape.centery))

        #CHEQUEO SI HAY OBSTACULO ENTRE LINEA DE VISION
        for obs in obstaculos_tiles:
            if obs[1].clipline(linea_de_vision):
                clipped_line = obs[1].clipline(linea_de_vision)

        #DISTANCIA CON EL JUGADOR
        distancia = math.sqrt(((self.shape.centerx - jugador.shape.centerx)**2) +
                             ((self.shape.centery - jugador.shape.centery)**2))

        if not clipped_line and distancia < constant.RANGO:
            if self.shape.centerx > jugador.shape.centerx:
                ene_dx = -constant.VELOCIDAD_ENEMIGOS
            if self.shape.centerx < jugador.shape.centerx:
                ene_dx = constant.VELOCIDAD_ENEMIGOS
            if self.shape.centery > jugador.shape.centery:
                ene_dy = -constant.VELOCIDAD_ENEMIGOS
            if self.shape.centery < jugador.shape.centery:
                ene_dy = constant.VELOCIDAD_ENEMIGOS

        self.move(ene_dx, ene_dy,obstaculos_tiles, exit_tile)

        #atacar al jugador
        if distancia < constant.RANGO_ATK and jugador.golpe == False:
            jugador.energy -= 10
            jugador.golpe = True
            jugador.ultimo_golpe = pygame.time.get_ticks()


    def update(self):
        if self.energy <= 0:
            self.energy = 0
            self.vivo = False
            #self.kill no funciona todavia porque hay que armarlo


        # CD para volver a recibir daño
        golpe_cooldown = 1000
        if self.tipo ==1:
            if self.golpe == True:
                if pygame.time.get_ticks() - self.ultimo_golpe > golpe_cooldown:
                    self.golpe = False


        cooldown_animation = 100 #milisegundos
        self.image = self.animaciones[self.frame_index]
        if pygame.time.get_ticks() - self.update_time >= cooldown_animation:
            self.frame_index = self.frame_index + 1
            self.update_time = pygame.time.get_ticks()
        if self.frame_index >= len(self.animaciones):
            self.frame_index = 0



    def draw(self, interfaz):
        imagen_flip = pygame.transform.flip(self.image, self.flip, False)
        interfaz.blit(imagen_flip, self.shape)
        #HITBOX
        #pygame.draw.rect(interfaz, constant.YELLOW, self.shape, 1)




