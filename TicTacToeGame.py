def printGameField(gameField): #field output
    print("---------")
    for i in range(3):
        print(gameField[0+i*3], '|', gameField[1+i*3], '|', gameField[2+i*3])
        print("---------")


def checkWin(gameField): #check for win
    #horizontal
    wins = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for i in wins:
        if gameField[i[0]] == gameField[i[1]] == gameField[i[2]]:
            return 1
    return 0

def gameOneTurn(turnSide, gameField): #turn side x or o
    valid = True
    while valid:
        try:
            userInput = int(input())
            if turnSide == 1:
                gameField[gameField.index(userInput)] = 'X'
                valid = False
            else:
                gameField[gameField.index(userInput)] = '0'
                valid = False
        except:
            print("incorrect input")
    return gameField

 
def main(): #main game function
    gameField = [1,2,3,4,5,6,7,8,9]
    turn = 1
    print("X turn")
    printGameField(gameField)
    for i in range(0,9):
        printGameField(gameOneTurn(turn,gameField))
        if checkWin(gameField) == 1:
            if turn == 1:
                print('X win')
            else:
                print('0 win')
            break
        else:
            if turn == 1:
                turn = 0
                print("\n0 turn")
            else:
                turn = 1
                print("\nX turn")
            continue
    return 0

if __name__ == "__main__": #start the main function
    main()