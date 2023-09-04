import random

board = ["-","-","-",
         "-","-","-",
         "-","-","-"]
currentPlayer="X"
winner=None
gameRunning=True



def printBoard(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-----")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-----") 
    print(board[6] + "|" + board[7] + "|" + board[8]) 
print(board)
    
def playerInput(board):

    inp = int(input("enter the number 1-9:"))
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1]=currentPlayer
    else:
        print("Oops player is already in the spot!")
    
def checkHorizontle(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != '-':
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != '-':
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != '-':
        winner = board[6]
        return True
    
def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != '-':
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != '-':
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != '-':
        winner = board[2]
        return True
    
def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != '-':
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != '-':
        winner = board[2]
        return True
        
def checkWin(board):
    if checkHorizontle(board)or checkRow(board)or checkDiag(board):
        print(f"the winner is {winner}")
        
def checktie(board):
    global Gamerunning
    if "-" not in board:
        printBoard(board)
        print("it is a tie!")
        gameRunning=False

    
    
def switchplayer():
    global currentPlayer
    if currentPlayer == "X":
            currentPlayer = "0"
    else:
            currentPlayer = "X"

   
def computer(board):
    while currentPlayer == "0":
        postion = random.randint(0,8)
        if board[postion] == "-":
            board[postion] = "0"
            switchplayer()

   
while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin(board)
    checktie(board)
    switchplayer()
    computer(board)
    checkWin(board)
    checktie(board)
