#creo que en game.py debe ir el código para arrancar juego + bucle principal

import pygame
from pilotando import ALTO, ANCHO


class Pilotando:
    def __init__ (self) -> None:
        print ('arranca juego')
        pygame.init ()
        self.display = pygame.display.set_mode ((ANCHO, ALTO))  #me guardo pantalla

    def jugando (self): #método con bucle principal
        salir = False
        while not salir:
            for event in pygame.event.get():    #detecto eventos
                if event.type == pygame.QUIT:
                    salir = True
            self.display.fill ((99,99,99))
            pygame.display.flip ()

                 

'''
class Pilotando: #necesitaré:

#este alto y ancho aquí no van y lo se, pero ya veremos....
    _ALTO = 600
    _ANCHO = 800
    _MARGEN_LATERAL = 30
    _ANCHO_NAVE = 10
    _ALTO_NAVE = _ALTO /10

    def __init__(self): #constructor
        pygame.init ()  #inicializo pygame
        self.pantalla = pygame.display.set_mode ((self._ANCHO, self._ALTO))   #me genero pantalla aquí
        self.jugador = Nave #nave esta dentro de juegoNave como class y la tendré all timE
        (self._MARGEN_LATERAL,              #coordenada x (left)
        (self._ALTO-self._ALTO_NAVE)/2,     #coordenada y (top)--> arranca en el centro
        self._ANCHO_NAVE,                   #ancho (width)
        self._ALTO_NAVE)                    #alto (height)

    def bucle_principal (self): #siempre en todos los juegos pygame donde se controlan cambios
        print ('estoy en el bucle principal')
        while True:
            for evento in pygame.event.get ():  #para que me detecte eventos y no se quede colgado
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:   #cuando pulses esto salimos
                        return 
                    if evento.key == pygame.QUIT:
                        return 
            pygame.draw.rect (self.pantalla, (255, 255, 255), self.jugador)          
            pygame.display.flip ()  #por ahora simplemente compruebo refresh pantalla con objeto display
            time.sleep (3)

if __name__ == "__main__":  #compruebo si el nombre del módulo es cadena main
    juego = Pilotando()  #llamo a mi class instanciando y me construyo juego
    juego.bucle_principal()   #la forma de iniciar el juego es llamando al método(función dentro de la class)
'''       
