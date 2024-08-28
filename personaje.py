import pygame
import constant

class Personaje():
    def __init__(self, x, y, animaciones, energy):
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

    def move(self, delta_x, delta_y):
        if delta_x < 0 :
            self.flip = True
        if delta_x > 0 :
            self.flip = False

          #Limites para el jugador. Evitar que se salga de la ventana de juego
        if self.shape.top < 0:
            self.shape.top=0

        if self.shape.bottom > constant.screen_height:
            self.shape.bottom = constant.screen_height

        if self.shape.right > constant.screen_width:
            self.shape.right = constant.screen_width

        if self.shape.left < 0:
            self.shape.left =0



        self.shape.x = self.shape.x + delta_x
        self.shape.y = self.shape.y + delta_y

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




