import pygame
import constant

class Personaje():
    def __init__(self, x, y, animaciones, energy, type):
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
        self.type = type

    def move(self, delta_x, delta_y):
        posicion_pantalla = [0, 0]

        if delta_x < 0 :
            self.flip = True
        if delta_x > 0 :
            self.flip = False

        self.shape.x = self.shape.x + delta_x
        self.shape.y = self.shape.y + delta_y

        #Mueve la cámara de acuerdo a la posición del personaje
        if self.type == 1:
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
            return posicion_pantalla

    def enemigos(self, posicion_pantalla):
        self.shape.x += posicion_pantalla[0]
        self.shape.y += posicion_pantalla[1]

    def update(self):
        if self.energy <= 0:
            self.energy = 0
            self.vivo = False
            #self.kill no funciona todavia porque hay que armarlo


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




