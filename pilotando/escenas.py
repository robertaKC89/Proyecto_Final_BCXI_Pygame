import os
import pygame as pg
from . import ANCHO, ALTO, COLOR_SMS

#todas las pantallas deben tener su bucle principal
class Escena:
    def __init__ (self, pantalla: pg.Surface):
        self.pantalla = pantalla    #dentro de la class creo referencia para guardar

    def bucle_principal (self):
        """
        método que debe ser implementado por cada una de las escenas en función de lo que esperen hasta salida
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
                if event.type == pg.QUIT:   #QUIT es pulsar 'x'
                    salir = True
            self.pantalla.fill ((21, 67, 96))  
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



    
        

class Juego (Escena):
    def bucle_principal(self):
        #screen = pg.display.set_mode ([800, 650])   #NO FUNCIONA AUN!!!
        #fondodos = pg.image.load (os.path.join ("scripts", "ASTEROIDE1.png")).convert()
        salir = False
        while not salir:
            for event in pg.event.get():    
                if event.type == pg.QUIT:
                    salir = True
            self.pantalla.fill ((0, 99, 0))  #NECESITO METER OTRO FONDO + IMGS
            pg.display.flip ()

class Records (Escena):
    def bucle_principal(self):
        #screen = pg.display.set_mode ([800, 650])   #FUNCIONA!!!
        #fondotres = pg.image.load (os.path.join ("scripts", "EXPLOSION2.png")).convert()
        salir = False
        while not salir:
            for event in pg.event.get():    
                if event.type == pg.QUIT:
                    salir = True
            self.pantalla.fill ((0, 0, 99))  #NECESITO METER OTRO FONDo + IMGS
            pg.display.flip ()

