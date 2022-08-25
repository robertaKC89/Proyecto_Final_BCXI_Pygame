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
    def __init__(self) -> None:
        super().__init__()  #llamo a la class padre Sprite
        img_nave = os.path.join ("scripts", "images", "NAVE3_redim (2).png")
        self.image = pg.image.load (img_nave)
        self.rect = self.image.get_rect (midleft = (30, 330))   #espacio que ocupa el objeto
    def update(self) -> None:   #obligatorio asignar método update com img y rect
        pass