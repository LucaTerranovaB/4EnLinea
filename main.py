from juego import Stack
from juego import *


# Main program
def main():
    # Prompt player input
    player1 = str( input('Choose X or O: ') )
    if player1 != 'X' and player1 != 'O':
        player1 = str( input('Choose X or O: ') )
    if player1 == 'X':
        computer1 = 'O'
    else:
        computer1 = 'X'
        
    # Print board
    board = initBoard()
    Stacks = initStacks()
    printBoard(board)
    print('To play: enter an integer between 1 to 7 ' + \
          'corresponding to each column in the board. ' + \
          'Whoever stacks 4 pieces next to each other, ' + \
          'either horizontally, vertically or diagonally wins.')
    game = False
    while game == False:
        # X player
        board, Stacks = move('X',board,Stacks,computer1)
        printBoard(board)
        game = checkWin('X',board)
        if game == True:
            break
        # O player
        board, Stacks = move('O',board,Stacks,computer1)
        printBoard(board)
        game = checkWin('O',board)
        if game == True:
            break
    print('Good game.')
if __name__ == '__main__':
    main()