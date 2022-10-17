from main import *
from cuatrolinea import *
import unittest

class Cuatro_LineUnittest(unittest.TestCase):

    def test_Fichax(self):
        
        Cuatro_Linea().createTablero()
        Cuatro_Linea().añadirF(1)
        juego = Cuatro_Linea()
        juego.tablero
        self.assertEqual(juego.tablero[7][1], 'X')

if __name__=='__main__':

    unittest.main()