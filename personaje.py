import pygame
import constant

class Personaje():
    def __init__(self, x, y):
        self.shape = pygame.Rect(0, 0, constant.CHAR_WIDTH, constant.CHAR_HEIGHT)
        self.shape.center = (x,y)

    def move(self, delta_x, delta_y):
        self.shape.x = self.shape.x + delta_x
        self.shape.y = self.shape.y + delta_y

    def draw(self, interfaz):
        pygame.draw.rect(interfaz, constant.YELLOW, self.shape)



