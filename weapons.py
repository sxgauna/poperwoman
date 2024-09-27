import pygame
import constant
import math
import random

class Weapon():
    def __init__(self, image, imagen_bala):
        self.imagen_bala = imagen_bala
        self.flip = True

        self.imagen_original = image
        self.angulo = 0
        self.imagen = pygame.transform.rotate(self.imagen_original, self.angulo)
        self.shape = self.imagen.get_rect()

        #Para evitar disparar tanto con un solo click
        self.disparada = False
        self.ultimo_disparo = pygame.time.get_ticks()

    def update(self, personaje):
        disparo_cooldown = constant.COOLDOWN_BALAS
        bala = None
        self.shape.center = personaje.shape.center
        if personaje.flip == False:
            self.shape.x += (personaje.shape.width/4)
            self.rotar_arma(False)
        else:
            self.shape.x -= (personaje.shape.width/4)
            self.rotar_arma(True)

        #Mover weapon1 con mouse
        mouse_pos = pygame.mouse.get_pos()
        dis_x = mouse_pos[0] - self.shape.centerx
        dis_y = -(mouse_pos[1] - self.shape.centery)

        self.angulo = math.degrees(math.atan2(dis_y,dis_x))

        #DETECTAR CLICK DE MOUSE PARA DISPARO
        if pygame.mouse.get_pressed()[0] and self.disparada == False and (pygame.time.get_ticks() - self.ultimo_disparo >= disparo_cooldown):
            bala = Bullet(self.imagen_bala,self.shape.x, self.shape.y, self.angulo)
            self.disparada = True
            self.ultimo_disparo = pygame.time.get_ticks()
        #RESETEAR EL CLICK DEL MOUSE PARA PODER DISPARAR MÁS DE UNA BALA
        if pygame.mouse.get_pressed()[0] == False:
            self.disparada = False
        return bala

    def rotar_arma(self,rotar):
        if rotar:
            imagen_flip = pygame.transform.flip(self.imagen_original, True, False)
        else:
            imagen_flip = pygame.transform.flip(self.imagen_original, False, False)
        self.imagen = pygame.transform.rotate(imagen_flip, self.angulo)

    def draw(self, interfaz):
        self.imagen = pygame.transform.rotate(self.imagen, self.angulo)
        interfaz.blit(self.imagen, self.shape)
        #HITBOX
        #pygame.draw.rect(interfaz, constant.RED, self.shape, 1)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, image, x, y, angle):
        pygame.sprite.Sprite.__init__(self)
        self.imagen_original = image
        self.angulo = angle
        self.image = pygame.transform.rotate(self.imagen_original, self.angulo)
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.delta_x = math.cos(math.radians(self.angulo)) * constant.SPEED_BALAS
        self.delta_y = -math.sin(math.radians(self.angulo)) * constant.SPEED_BALAS

    def update(self, lista_enemigos, obstaculos_tiles):
        damage = 0
        pos_damage = None
        self.rect.x += self.delta_x
        self.rect.y += self.delta_y

        #VER SI LAS BALAS YA SALIERON DE PANTALLA
        if self.rect.right < 0 or self.rect.left > constant.screen_width or self.rect.bottom < 0 or self.rect.top > constant.screen_height:
            self.kill()

        #Verifica coalición con enemigo
        for enemigo in lista_enemigos:
            if enemigo.shape.colliderect(self.rect):
                damage = 50 + random.randint(-7,7)
                pos_damage = enemigo.shape
                enemigo.energy -= damage
                self.kill()
                break

        #Verifica coalición con paredes
        for obs in obstaculos_tiles:
            if obs[1].colliderect(self.rect):
                self.kill()
                break
        return damage, pos_damage

    def draw(self, interfaz):
        interfaz.blit(self.image, (self.rect.centerx, self.rect.centery))
