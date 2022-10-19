from main import *
from cuatrolinea import *
import unittest

class Cuatro_LineUnittest(unittest.TestCase):

    def test_Fichax(self):
        
        juego = Cuatro_Linea()
        juego.createTablero()
        juego.añadirF(1)
        self.assertEqual(juego.tablero[7][1], 'X')

    def test_checkColumn_success(self):

        juego = Cuatro_Linea()
        juego.createTablero()
        juego.añadirF(3)
        self.assertEqual(juego.checkColum(3),6)

    def test_checkColumn_full(self):

        juego = Cuatro_Linea()
        juego.createTablero()
        
        for i in range(8):
            juego.añadirF(3)
        self.assertEqual(juego.checkColum(3),-1)
        

    def test_cambioPlayer(self):
        juego = Cuatro_Linea()
        self.assertEqual(juego.cambioPlayer(),2)

    def test_cambioTurno(self):
        juego = Cuatro_Linea()
        self.assertEqual(juego.cambioTurno(),"X")

    #Verifica ganador jugador 1 horizontalmente

    def test_checkganador_1(self):
        juego = Cuatro_Linea()
        juego.createTablero()
        juego.añadirF(1)     
        juego.añadirF(0)
        juego.añadirF(1)
        juego.añadirF(0)
        juego.añadirF(1)
        juego.añadirF(0)
        juego.añadirF(1)
        
        self.assertEqual(juego.ganador,1)


    #Verifica ganador jugador 1 verticalmente
    def test_checkganador_2(self):
        
        juego = Cuatro_Linea()
        juego.createTablero()
        juego.añadirF(0)     
        juego.añadirF(1)
        juego.añadirF(0)
        juego.añadirF(1)
        juego.añadirF(0)
        juego.añadirF(1)
        juego.añadirF(0)
        
        self.assertEqual(juego.ganador,1)

    def test_checkganador_3(self):
        juego = Cuatro_Linea()
        juego.createTablero()
        juego.añadirF(0)
        juego.añadirF(1)
        juego.añadirF(1)
        juego.añadirF(2)
        juego.añadirF(0)
        juego.añadirF(2)
        juego.añadirF(2)
        juego.añadirF(3)
        juego.añadirF(3)
        juego.añadirF(3)
        juego.añadirF(3)
        self.assertEqual(juego.tablero[4][3], 'X')
        self.assertEqual(juego.tablero[5][2], 'X')
        self.assertEqual(juego.tablero[6][1], 'X')
        self.assertEqual(juego.tablero[7][0], 'X')

   

    def test_turno(self):
        juego = Cuatro_Linea()
        self.assertEqual(juego.turno(),"X")
        

if __name__=='__main__':
    
    unittest.main()