import pygame.sprite

class Item(pygame.sprite.Sprite):
    def __init__(self, x, y, item_type, animation_list):
        pygame.sprite.Sprite.__init__(self)
        self.item_type = item_type #0= coin, 1 = potion
        self.animation_list = animation_list
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.image = self.animation_list[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

    def update(self, posicion_pantalla, personaje):
        self.rect.x += posicion_pantalla[0]
        self.rect.y += posicion_pantalla[1]
        #Compruebo colisión entre personaje e item
        if self.rect.colliderect(personaje.shape):
            if self.item_type == 0:
                personaje.score +=1
            elif self.item_type == 1 and personaje.energy <= 75:
                personaje.energy +=25
            self.kill()

        cooldown_animacion = 20 #miliseconds
        self.image = self.animation_list[self.frame_index]
        if pygame.time.get_ticks() - self.update_time > cooldown_animacion:
            self.frame_index += 1
            self.update_time = pygame.time.get_ticks()
        if self.frame_index >= len(self.animation_list):
            self.frame_index = 0
