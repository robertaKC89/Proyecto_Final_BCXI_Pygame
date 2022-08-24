#main está en la raíz y es archivo que lanza el programa
from pilotando import ANCHO, ALTO
from pilotando.game import Pilotando

if __name__ == '__main__':
    print (f"el tamaño de pantalla es: {ANCHO}x{ALTO}")
    juego = Pilotando () #me guardo mi juego
    juego.jugando ()    #quiero jugar, por ello llamo a bucle principal