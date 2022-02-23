from random import randint

global Player1Name
Player1Name = 'Player 1'
global Player2Name
Player2Name = 'Player 2'

global Simbol1
Simbol1 = 'X'
global Simbol2
Simbol2 = 'O'

def menu():
    print("\n\tTic Tac Toe")
    print('1. Players names\n' +
          '2. Change simbols\n'+
          '3. Play\n' + 
          '4. Exit')
    return input('Enter your option: ')

def PlayersNames():
    global Player1Name
    global Player2Name
    print(f'\n\tPlayers names:\n1.{Player1Name}\n2.{Player2Name}')
    option = input('Which you wanna change? ')
    if option == '1':
        Player1Name = input('Enter new name for player 1: ')
    elif option == '2':
        Player2Name = input('Enter new name for player 2: ')
    else:
        print('Invalid option. Enter a valid option')

def PlayersSimbols():
    global Simbol1
    global Simbol2
    print(f'\n\tPlayers simbols:\n1.{Simbol1}\n2.{Simbol2}')
    option = input('Which you wanna change? ')
    if option == '1':
        Simbol1aux = input('Enter new simbol for player 1: ')
        if (Simbol1aux != Simbol2):
            Simbol1 = Simbol1aux
        else:
            print('Same simbol as Player 2. Try again.')
    elif option == '2':
        Simbol2aux = input('Enter new simbol for player 2: ')
        if (Simbol2aux != Simbol1):
            Simbol2 = Simbol2aux
        else:
            print('Same simbol as Player 2. Try again.')
    else:
        print('Invalid option. Enter a valid option')

def createBoard():
    matrix = []
    nRows = 3
    nColumns = 3
    for i in range(nRows):
        matrix.append(['-'] * nColumns)
    size = (nRows,nColumns)
    return matrix, size

def showBoard(matrix, size):
    rows, columns = size
    for i in range(rows):
        for j in range(columns):
            print(matrix[i][j], end='\t')
        print('')

def fillBoard(matrix, simbol):
    nRows = int(input('Enter the row: '))
    nColumns = int(input('Enter the column: '))
    matrix[nRows-1][nColumns-1] = simbol

def Play(Board, size):
    end = False
    showBoard(Board, size)
    turn = randint(1,2)
    while end == False:
        currentSimbol = ''
        currentPlayer = ''
        if turn == 1:
            print('\n\tIt\'s turn of', Player1Name)
            currentSimbol = Simbol1
            currentPlayer = Player1Name
            fillBoard(Board,Simbol1)
            turn = 2
        else:
            print('\n\tIt\'s turn of', Player2Name)
            currentSimbol = Simbol2
            currentPlayer = Player2Name
            fillBoard(Board, Simbol2)
            turn = 1
        showBoard(Board,size)

        if Board[0][0] == currentSimbol and Board[0][1] == currentSimbol and Board[0][2] == currentSimbol:
            end = True            
        if Board[1][0] == currentSimbol and Board[1][1] == currentSimbol and Board[1][2] == currentSimbol:           
            end = True        
        if Board[2][0] == currentSimbol and Board[2][1] == currentSimbol and Board[2][2] == currentSimbol:           
            end = True
        if Board[0][0] == currentSimbol and Board[1][0] == currentSimbol and Board[2][0] == currentSimbol:
            end = True            
        if Board[0][1] == currentSimbol and Board[1][1] == currentSimbol and Board[2][1] == currentSimbol:
            end = True     
        if Board[0][2] == currentSimbol and Board[1][2] == currentSimbol and Board[2][2] == currentSimbol:
            end = True
        if Board[0][0] == currentSimbol and Board[1][1] == currentSimbol and Board[2][2] == currentSimbol:
            end = True            
        if Board[2][0] == currentSimbol and Board[1][1] == currentSimbol and Board[0][2] == currentSimbol:
            end = True 
    print('\n\tGame Over!\n\n\t' + currentPlayer + ' wins!')

def main():
    gameOver = False
    while gameOver == False:
        option = menu()
        if option == '1':
            PlayersNames()
        elif option == '2':
            PlayersSimbols()
        elif option == '3':
            Board, size = createBoard()
            Play(Board,size)
        elif option == '4':
            print('Thanks for playing. See you later!')
            gameOver = True
        else:
            print('Invalid option. Enter a valid option')

main()