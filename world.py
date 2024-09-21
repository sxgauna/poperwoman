import pygame
import constant
from items import Item
from personaje import Personaje

obstaculos = [0, 2, 72, 19, 20, 21, 22, 23, 24,28,
90,91,92,93,94,95,96,97,6, 7,
79,61,72,43,25,7,72,54,36,18 ]

puertas_cerradas = [28]


class Mundo():
    def __init__(self):
        self.map_tiles = []
        self.obstaculos_tiles = []

        self.lista_item = []
        self.lista_enemigo = []
        self.puertas_cerradas_tiles = []
        self.exit_tile = []

    def process_data(self, data, tile_list, item_imagenes, animaciones_enemigo):
        self.level_lenght = len(data)
        for y, row in enumerate(data):
            for x, tile in enumerate(row):
                image = tile_list[tile]
                image_rect = image.get_rect()
                image_x = x * constant.TILE_SIZE
                image_y = y * constant.TILE_SIZE
                image_rect.center = (image_x, image_y)
                tile_data = [image, image_rect, image_x, image_y, tile]
                if tile in obstaculos:
                    self.obstaculos_tiles.append(tile_data)

                if tile in obstaculos:
                    self.puertas_cerradas_tiles.append(tile_data)
                elif tile == 29:
                    self.exit_tile = tile_data

            #MONEDA
                elif tile == 8:
                    moneda = Item(image_x, image_y, 0, item_imagenes[0])
                    tile_data[0] = tile_list[56]
                    self.lista_item.append(moneda)
            #POTI ROJA
                elif tile == 16:
                    pocion_roja = Item(image_x, image_y, 0, item_imagenes[1])
                    tile_data[0] = tile_list[56]
                    self.lista_item.append(pocion_roja)
            #ENEMIGO1
                elif tile == 27:
                    ene1 = Personaje(image_x, image_y, animaciones_enemigo[1], 100, 2)
                    tile_data[0] = tile_list[56]
                    self.lista_enemigo.append(ene1)



                self.map_tiles.append(tile_data)

    def cambiar_puerta(self, jugador, tile_list):
        buffer = 50
        proximidad_rect = pygame.Rect(jugador.shape.x - buffer, jugador.shape.y - buffer,
                                        jugador.shape.width + 2 * buffer, jugador.shape.height + 2 * buffer)
        for tile_data in self.map_tiles:
            image, rect, x, y, tile_type = tile_data
            if proximidad_rect.colliderect(rect):
                if tile_type in puertas_cerradas:
                    if tile_type == 28:
                        new_tile_type = 56

                    tile_data[4] = new_tile_type
                    tile_data[0] = tile_list[new_tile_type]
                    if tile_data in self.obstaculos_tiles:
                        self.obstaculos_tiles.remove(tile_data)


                    return True
        return False



    def update(self, posicion_pantalla):
        for tile in self.map_tiles:
            tile[2] += posicion_pantalla[0]
            tile[3] += posicion_pantalla[1]
            tile[1].center = (tile[2], tile[3])

    def draw(self, surface):
        for tile in self.map_tiles:
            surface.blit(tile[0], tile[1])