import random

print("Welcome to Tic Tac Toe")
print("----------------------")
print("\nEnter the turn in the following format")
print('1|2|3')
print('-+-+-')
print('4|5|6')
print('-+-+-')
print('7|8|9')

player = '0'
bot = 'X'

possibleNumbers = [1,2,3,4,5,6,7,8,9]
gameBoard = {1: ' ', 2: ' ', 3: ' ',
             4: ' ', 5: ' ', 6: ' ',
             7: ' ', 8: ' ', 9: ' '}

#printing the board
def printBoard(gameBoard):
    print(gameBoard[1] + '|' + gameBoard[2] + '|' + gameBoard[3])
    print('-+-+-')
    print(gameBoard[4] + '|' + gameBoard[5] + '|' + gameBoard[6])
    print('-+-+-')
    print(gameBoard[7] + '|' + gameBoard[8] + '|' + gameBoard[9])

def checkInput(pos):
    if pos in possibleNumbers:
        return True
    else:
        return False

#check if free space is available
def freeSpace(pos):
    if (gameBoard[pos] == ' '):
        return True
    else:
        return False

#checking draw condition
def draw():
    for i in gameBoard.keys():
        if (gameBoard[i] == ' '):
            return False  
    return True

#conditions to win the game
def win():
    if (gameBoard[1] == gameBoard[2] == gameBoard[3] and gameBoard[1] != ' '):
        return True
    elif (gameBoard[4] == gameBoard[5] == gameBoard[6] and gameBoard[4] != ' '):
        return True
    elif (gameBoard[7] == gameBoard[8] == gameBoard[9] and gameBoard[7] != ' '):
        return True
    elif (gameBoard[1] == gameBoard[4] == gameBoard[7] and gameBoard[1] != ' '):
        return True
    elif (gameBoard[2] == gameBoard[5] == gameBoard[8] and gameBoard[2] != ' '):
        return True
    elif (gameBoard[3] == gameBoard[6] == gameBoard[9] and gameBoard[3] != ' '):
        return True
    elif (gameBoard[1] == gameBoard[5] == gameBoard[9] and gameBoard[1] != ' '):
        return True
    elif (gameBoard[3] == gameBoard[5] == gameBoard[7] and gameBoard[3] != ' '):
        return True
    else:
        return False

def winMark(letter):
    if (gameBoard[1] == gameBoard[2] == gameBoard[3] == letter):
        return True
    elif (gameBoard[4] == gameBoard[5] == gameBoard[6] == letter):
        return True
    elif (gameBoard[7] == gameBoard[8] == gameBoard[9] == letter):
        return True
    elif (gameBoard[1] == gameBoard[4] == gameBoard[7] == letter):
        return True
    elif (gameBoard[2] == gameBoard[5] == gameBoard[8] == letter):
        return True
    elif (gameBoard[3] == gameBoard[6] == gameBoard[9] == letter):
        return True
    elif (gameBoard[1] == gameBoard[5] == gameBoard[9] == letter):
        return True
    elif (gameBoard[3] == gameBoard[5] == gameBoard[7] == letter):
        return True
    else:
        return False

def insertLetter(letter, pos):

    if checkInput(pos):
        if freeSpace(pos):
            gameBoard[pos] = letter
            printBoard(gameBoard)
            if(draw()):
                print("\nIT'S A DRAW!")
                exit()

            if winMark(letter):
                if letter == bot:
                    print("\nBOT WINS!")
                    exit()
                else:
                    print("\nPlayer WINS!")
                    exit()
            return

        else:
            print("No space available")
            pos = int(input("Enter a new position: "))
            insertLetter(letter, pos)
            return

    else:
        print("Invalid input")
        pos = int(input("Enter a new position between 1-9: "))
        insertLetter(letter, pos)
        return

#using minimax algorithm
def minimax(gameBoard, maximizing):
    
    if winMark(bot):
        return 1    #returning 1 if winning mark is 'X'
    elif winMark(player):
        return -1   #returning 1 if winning mark is '0'
    elif draw():
        return 0    #returning 0 if match is draw

    if maximizing:
        bestScore = -10
        for i in gameBoard.keys():
            if (gameBoard[i] == ' '):
                gameBoard[i] = bot
                score = minimax(gameBoard, False)
                gameBoard[i] = ' '
                if score > bestScore:
                    bestScore = score
        return bestScore
    else:
        bestScore = 10
        for i in gameBoard.keys():
            if (gameBoard[i] == ' '):
                gameBoard[i] = player
                score = minimax(gameBoard, True)
                gameBoard[i] = ' '
                if score < bestScore:
                    bestScore = score
        return bestScore

#taking the player's move as input
def playerMove():
    pos = int(input("Enter a position for '0': "))
    print("\n------")
    print("PLAYER")
    print("------")
    insertLetter(player, pos)
    return

def botMove():
    bestScore = -10
    bestMove = 0
    for i in gameBoard.keys():
        if (gameBoard[i] == ' '):
            gameBoard[i] = bot
            score = minimax(gameBoard, False)
            gameBoard[i] = ' '
            if score > bestScore:
                bestScore = score
                bestMove = i
    print("\n---")
    print("BOT")
    print("---")
    insertLetter(bot, bestMove)
    return

while not win():
    playerMove()
    botMove()