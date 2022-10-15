import os



def cls():
    os.system('cls')


#Validar 4 en linea por columna

class Grafics():
    

    grid = [['.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.']]
    info = [['==+===+===+===+===+=='],
            ['1', '2', '3', '4', '5', '6']]
        
#validacion ganador e imprime pantalla
    
    def prints(self):
        cls()
        Check.check_all()
        for x in range(5):
            print(*Grafics.grid[x], sep=" | ")
        for x in range(2):
            print(*Grafics.info[x], sep=" | ")

#Separador
    def printsespacios(self):
        for x in range(3):
            print("")



class Check():

    def __init__(self,fila,columna,xcount,ocount):

        self._fila = fila
        self._columna = columna 
        self._xcount = xcount
        self._ocount = ocount

    def columna_check(self):

        for self._fila in range(6):
            self._xcount = 0
            for self._columna in range(5):
                if (Grafics.grid[self._columna][self._fila] == "X"):
                    self._xcount += 1
            if self._xcount == 4:
                GanaPierde.xw()
        for self._fila in range(6):
            self._ocount = 0
            for self._columna in range(5):
                if (Grafics.grid[self._columna][self._fila] == "O"):
                    self._ocount += 1
            if self._ocount == 4:
                GanaPierde.ow()
#Validacion 4 en linea por fila
    def fila_check(self):
        for self._columna in range(5):
            self._xcount = 0
            for self._fila in range(6):
                if (Grafics.grid[self._columna][self._fila] == "X"):
                    self._xcount += 1
                if self._xcount == 4:
                    GanaPierde.xw()
        for self._columna in range(5):
            self._ocount = 0
            for self._fila in range(6):
                if (Grafics.grid[self._columna][self._fila] == "O"):
                    self._ocount += 1
                if self._ocount == 4:
                    GanaPierde.ow()
#validar todo
    def check_all(self):
        Check.columna_check()
        Check.fila_check()


class GanaPierde():

#Gana O

    def __init__(self,gw):

        self._gw = gw


    def ow(self):
        cls()
        Grafics.printsespacios()
        print("O, Wins!".center(16))
        Grafics.printsespacios()
        self._gw = True

# Gana X
    def xw(self):
        cls()
        Grafics.printsespacios()
        print("X, Wins!".center(16))
        Grafics.printsespacios()
        self._gw = True


