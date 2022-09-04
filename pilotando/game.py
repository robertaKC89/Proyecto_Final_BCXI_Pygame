#creo que en game.py debe ir el código para arrancar juego + bucle principal
import os
import pygame as pg
from pilotando import ALTO, ANCHO
from pilotando.escenas import Portada, Niveluno, Niveldos, Records


class Pilotando:
    def __init__ (self) -> None:
        print ('arranca juego')
        pg.init ()
        self.display = pg.display.set_mode ((ANCHO, ALTO))  #me guardo pantalla
        pg.display.set_caption ("Pilotando")
        icon = pg.image.load (os.path.join ("scripts","images", "Nave2.png")).convert()  #ruta relativa desde carpeta scripts
        pg.display.set_icon (icon)

        #las tres se comportan igual porque heredan de Escena
        #recorro cada una y les meto su bucle_principal
        self.escenas = [ 
            Portada (self.display),
            Niveluno (self.display),
            Niveldos (self.display),
            Records (self.display),
        ]

    def jugando (self): #método con bucle principal        
        #este es el método y aquí voy a recorrer las ESCENAS y a cada una le pondré su bucle principal
        for escena in self.escenas:
            escena.bucle_principal () 