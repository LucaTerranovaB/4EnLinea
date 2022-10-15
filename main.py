from juego import *

class Main(Grafics,Check,GanaPierde):
    
    def juego(self):

        while True:
            if GanaPierde(self._gw) == True:
                break
            else:
                Grafics.prints()
                self._fila = int(input("X, column: "))
                self._fila -= 1
                if 0 > self._fila or self._fila > 6:
                    continue
                else:
                    for x in range(4, -1, -1):
                        if Grafics.grid[x][self._fila] == '.':
                            Grafics.grid[x][self._fila] = 'X'
                            break
                Grafics.prints()
                self._fila = int(input("O, column: "))
                self._fila -= 1
                if 0 > self._fila or self._fila > 6:
                    continue
                else:
                    for x in range(4, -1, -1):
                        if Grafics.grid[x][self._fila] == '.':
                            Grafics.grid[x][self._fila] = 'O'
                            break

if __name__=='__main__':
   a = Grafics.grid and Grafics.prints() and Grafics.printsespacios()
   print(a)
   b = Check.check_all()
   print(b)
   c = GanaPierde.ow() or GanaPierde.xw()
   print(c) 
   d = Main.juego()
   print(d)    