import os
import pygame as pg
from . import ANCHO, ALTO, COLOR_SMS, FONDO_PORTADA, FPS
from . entidades import Nave

#todas las pantallas deben tener su bucle principal
class Escena:
    def __init__ (self, pantalla: pg.Surface):
        self.pantalla = pantalla    #dentro de la class creo referencia para guardar
        self.reloj = pg.time.Clock ()

    def bucle_principal (self):
        """debe ser implementado por cada una de las escenas en función de lo que esperen hasta la salida
        """
        pass

class Portada (Escena): #hereda de escena con el correspondiente constructor que se la guarda 
    def __init__(self, pantalla: pg.Surface):
        super().__init__(pantalla)  #la recojo para pasarla al constructor padre que la guarda  
        self.logo = pg.image.load (os.path.join ("scripts", "images","spaceship.jpg"))
        font_file = os.path.join ("scripts", "fonts", "CabinSketch-Bold.ttf")
        self.tipografia = pg.font.Font (font_file, 40)  #cargo archivo como tipografía

    def bucle_principal(self):
        salir = False
        while not salir:
            for event in pg.event.get():    #detecto eventos para que no se me caiga surface
                if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                    salir = True
                if event.type == pg.QUIT:   #QUIT es pulsar 'x'
                    pg.quit ()
            self.pantalla.fill (FONDO_PORTADA)  
            self.pintar_logo ()
            self.pintar_texto ()
            pg.display.flip ()

    def pintar_logo (self): #refactorizo y me traigo el método pintar fuera para más pulcritud de código
        ancho_logo = self.logo.get_width()
        pos_x = (ANCHO - ancho_logo) / 2
        pos_y = ALTO / 8
        self.pantalla.blit (self.logo,(pos_x, pos_y))

    def pintar_texto (self):
        sms = "¡Pulsa espacio para empezar a divertirte!"
        texto = self.tipografia.render (sms, True, COLOR_SMS)   #renderizo como tipografía y me genera superficie pintada
        ancho_texto = texto.get_width ()
        pos_x = (ANCHO - ancho_texto) /2 
        pos_y = .80 * ALTO
        self.pantalla.blit (texto, (pos_x, pos_y)) 

"""
en Niveles debo: 
- cargar img de fondo en memoria
- crear funcion de pintar_fondo
- llamar a esta función para que el fondo se pinte en bucle principal de Juego

"""
class Niveluno (Escena):
    def __init__(self, pantalla: pg.Surface):
        super().__init__(pantalla)
        galaxia_fondo = os.path.join ("scripts", "images", "galaxia.png")   
        self.fondo = pg.image.load (galaxia_fondo)  #cargada img de fondo en memoria
        self.jugador = Nave ()

    def bucle_principal(self):
        salir = False
        while not salir:
            self.reloj.tick (FPS) 
            for event in pg.event.get():    
                if event.type == pg.QUIT:
                    pg.quit ()
            self.pantalla.fill ((0, 0, 66))  
            self.pinto_fondo ()
            self.jugador.update ()  # actualiza el estado de sprite nave todo el rato y luego la pinta
            self.pantalla.blit (self.jugador.image, self.jugador.rect)  #pinto nave en pantalla
            pg.display.flip ()

    def pinto_fondo (self):
        self.pantalla.blit (self.fondo, (0, 0))


class Niveldos (Escena):
    def __init__(self, pantalla: pg.Surface):
        super().__init__(pantalla)
        galaxia_fondo_dos = os.path.join ("scripts", "images", "galaxia2.png")   
        self.fondo = pg.image.load (galaxia_fondo_dos)  #cargada img de fondo en memoria
        self.jugador = Nave ()

    def bucle_principal(self):
        salir = False
        while not salir:
            self.reloj.tick (FPS) 
            for event in pg.event.get():    
                if event.type == pg.QUIT:
                    pg.quit ()
            self.pantalla.fill ((0, 0, 66))  
            self.pinto_fondo ()
            self.jugador.update ()  # actualiza el estado de sprite nave todo el rato y luego la pinta
            self.pantalla.blit (self.jugador.image, self.jugador.rect)  #pinto nave en pantalla
            pg.display.flip ()

    def pinto_fondo (self):
        self.pantalla.blit (self.fondo, (0, 0))

class Records (Escena):
    def bucle_principal(self):
        salir = False
        while not salir:
            for event in pg.event.get():    
                if event.type == pg.QUIT:
                    pg.quit ()
            self.pantalla.fill ((0, 0, 99))  #NECESITO METER OTRO FONDo + IMGS
            pg.display.flip ()

