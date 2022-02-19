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

def Play():
    pass

def showBoard():
    pass

def main():
    gameOver = False
    while gameOver == False:
        option = menu()
        if option == '1':
            PlayersNames()
        elif option == '2':
            PlayersSimbols()
        elif option == '3':
            Play()
        elif option == '4':
            gameOver = True
        else:
            print('Invalid option. Enter a valid option')

main()