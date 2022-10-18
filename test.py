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
        pass

    def test_cambioTurno(self):
        juego = Cuatro_Linea()
        pass

    def test_checkganador_1(self):
        juego = Cuatro_Linea()
        pass

    def test_checkganador_2(self):
        juego = Cuatro_Linea()
        pass

    def test_checkganador_3(self):
        juego = Cuatro_Linea()
        pass

    def test_checkganador_4(self):
        juego = Cuatro_Linea()
        pass

    def test_printTab(self):
        juego = Cuatro_Linea()
        pass

    def test_turno(self):
        juego = Cuatro_Linea()
        pass
          

if __name__=='__main__':
    
    unittest.main()