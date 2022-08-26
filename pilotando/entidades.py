import os
import pygame as pg
from pygame.sprite import Sprite
from . import ANCHO, ALTO
"""
1. crear class nave:
- que sea sprite
- que la gestione el método update
2. Situarla con coordenadas y para ello obtener rectángulo
3. Crear método mostrar_nave
4. En el bucle principal llamar a mostrar_nave 
5. si quiero animar la nave:
- función 'animar' con lista imágenes y las muestro en el bucle (lo encontraré en librería pygame)
"""

class Nave (Sprite):
    velocidad = 5

    def __init__(self) -> None:
        super().__init__()  #llamo a la class padre Sprite
        img_nave = os.path.join ("scripts", "images", "NAVE3_redim.png")
        self.image = pg.image.load (img_nave)
        self.rect = self.image.get_rect (midleft = (30, 330))   #espacio que ocupa el objeto

    def update(self):   #obligatorio asignar método update com img y rect
        tecla = pg.key.get_pressed()    #class nave es la responsable de moverse a si misma
        if tecla [pg.K_UP]:
            self.rect.y -= self.velocidad
            if self.rect.top < 0:
                self.rect.top = 0
        if tecla [pg.K_DOWN]:
            self.rect.y += self.velocidad
            if self.rect.bottom > ALTO:
                self.rect.bottom = ALTO
                
            


