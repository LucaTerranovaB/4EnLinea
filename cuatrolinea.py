ficha1 = 'X'
ficha2 = 'O'
jugador1 = 1
jugador2 = 2 

class Cuatro_Linea():
    
    def __init__(self):
        self.filas = 8
        self.columnas = 8
        self.tablero = list()
        self.vacio = ' '
        self.linea = 4
        self.ficha = ficha1
        self.jugador = jugador1
        self.ganador = None 
    
    
    def createTablero(self):
        self.tablero = [[self.vacio for columna in range(self.columnas)] for fila in range(self.filas)]
        return self.tablero
    

    
   
    def añadirF(self, columna:int):
        fila = self.checkColum(columna)
        if fila == -1:
            return "Invalido"
        self.tablero[fila][columna] = self.ficha
        if self.checkganador(self.ficha):
            self.ganador = self.jugador
        self.cambioPlayer()

        
   
    def checkColum(self, columna:int):
        a = len(self.tablero) - 1
        while a >= 0:
            if self.tablero[a][columna] == self.vacio:
                return a
            a -= 1
        return -1
        
    
    def cambioPlayer(self):
        if self.jugador == jugador1:
            self.jugador = jugador2
        else:
            self.jugador = jugador1
        self.cambioTurno()        
    
    def cambioTurno(self):
        if self.jugador == jugador2:
            self.ficha = ficha2
        else:
            self.ficha = ficha1
        

    def checkganador(self, ficha):
        
        for i in range(self.columnas - 3):
            for j in range(self.filas):
                if self.tablero[j][i] == ficha and self.tablero[j][i+1] == ficha and self.tablero[j][i+2] == ficha and self.tablero[j][i+3] == ficha:
                    return True
       
       
        for i in range(self.columnas):
            for j in range(self.filas - 3):
                if self.tablero[j][i] == ficha and self.tablero[j+1][i] == ficha and self.tablero[j+2][i] == ficha and self.tablero[j+3][i] == ficha:
                    return True
                    
        for i in range(self.columnas):
            for j in range(self.filas - 3):
                if self.tablero[j][i] == ficha and self.tablero[j+1][i+1] == ficha and self.tablero[j+2][i+2] == ficha and self.tablero[j+3][i+3] == ficha:
                    return True
        
        for i in range(self.columnas):
            for j in range(self.filas - 3):
                if self.tablero[j][i] == ficha and self.tablero[j-1][i-1] == ficha and self.tablero[j-2][i-2] == ficha and self.tablero[j-3][i-3] == ficha:
                    return True
                
        return False
    
    def printTab(self):

        print("|", end="")
        for f in range(0, len(self.tablero[0])):
            print(f, end="|")
        print("")
        
      
        for fila in self.tablero:
            print('|', end='')
            for valor in fila:
                print(valor, end='')
                print('|', end='')
            print('') 
        
  
        print('+', end='')
        for x in range(1, len(self.tablero[0]) + 1):
            print('-', end='+')
        print('')
    
    def turno(self):
        print(f'Player 1: {ficha1} | Player 2 : {ficha2}')
        if self.jugador == jugador1:
            print(f'Player 1 juega: ({ficha1})')
        else:
            print(f'Player 2 Juega: ({ficha2})')
    
    def imprimirWinnwer(self):
        print(f' {self.ganador} WINS!!!!!!!!!!')