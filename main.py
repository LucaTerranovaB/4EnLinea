
from cuatrolinea import Cuatro_Linea
from cuatrolinea import *

def play():
    juego = Cuatro_Linea()
    juego.createTablero()
    try:
        while True:
            juego.printTab()
            juego.turno()
            op = int(input('Donde desea poner su ficha?? 1 - 7: '))
            juego.añadirF(op)
            if juego.ganador != None:
                juego.printTab()
                juego.imprimirWinnwer()
                return again()
    except Exception as e:
        print(f'Error!: {e}')   

def again():
    eleccion = input("Revancha? [s/n] ")
    if eleccion == "s":
        play()
    elif eleccion == "n":
        return False

if __name__=='__main__':
    play()