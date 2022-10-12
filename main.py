import os

gw = False

def cls():
    os.system('cls')


#Validar 4 en linea por columna


def columna_check():

    for fila in range(6):
        xcount = 0
        for columna in range(5):
            if (grid[columna][fila] == "X"):
                xcount += 1
        if xcount == 4:
            xw()
    for fila in range(6):
        ocount = 0
        for columna in range(5):
            if (grid[columna][fila] == "O"):
                ocount += 1
        if ocount == 4:
            ow()
#Validacion 4 en linea por fila
def fila_check():
    for columna in range(5):
        xcount = 0
        for fila in range(6):
            if (grid[columna][fila] == "X"):
                xcount += 1
            if xcount == 4:
                xw()
    for columna in range(5):
        ocount = 0
        for fila in range(6):
            if (grid[columna][fila] == "O"):
                ocount += 1
            if ocount == 4:
                ow()
#validar todo
def check_all():
    columna_check()
    fila_check()


#validacion ganador e imprime pantalla

def prints():
    cls()
    check_all()
    for x in range(5):
        print(*grid[x], sep=" | ")
    for x in range(2):
        print(*info[x], sep=" | ")

#Separador
def printsespacios():
    for x in range(3):
        print("")

#Gana O

def ow():
    cls()
    printsespacios()
    print("O, Wins!".center(16))
    printsespacios()
    gw = True

# Gana X
def xw():
    cls()
    printsespacios()
    print("X, Wins!".center(16))
    printsespacios()
    gw = True

#Tablero

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
info = [['==+===+===+===+===+=='],
        ['1', '2', '3', '4', '5', '6']]

class Sudoku():

    while True:
        if gw == True:
            break
        else:
            prints()
            fila = int(input("X, column: "))
            fila -= 1
            if 0 > fila or fila > 6:
                continue
            else:
                for x in range(4, -1, -1):
                    if grid[x][fila] == '.':
                       grid[x][fila] = 'X'
                       break
            prints()
            fila = int(input("O, column: "))
            fila -= 1
            if 0 > fila or fila > 6:
                continue
            else:
                for x in range(4, -1, -1):
                    if grid[x][fila] == '.':
                       grid[x][fila] = 'O'
                       break

if __name__=='__main__':
    Sudoku
  