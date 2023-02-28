import random
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

gamecontinue = True
winner = None
currentplayer = "X"

def printboard(board):
     print(board[0] + " | " + board[1] + " | " + board[2])
     print("----------")
     print(board[3] + " | " + board[4] + " | " + board[5])
     print("----------")
     print(board[6] + " | " + board[7] + " | " + board[8])

def playerinput(board):
    p_input = int(input("Enter a number between 1-9: "))
    if p_input >= 1 and p_input <= 9 and board[p_input-1] == "-":
        board[p_input - 1] = currentplayer
    else:
        print("The selected part is not empty!")

def winforrow(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

def winforcolumn(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True

def winfordiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True

def tie(board):
    global gamecontinue
    if "-" not in board:
        printboard(board)
        print("It's a tie")
        gamecontinue = False

def win():
    global gamecontinue
    if winfordiagonal(board) or winforrow(board) or winforcolumn(board):
        printboard(board)
        print(f"The winner is {winner}")
        gamecontinue = False

def switchplayer():
    global currentplayer
    if currentplayer == "X":
        currentplayer = "O"
    else:
        currentplayer = "X"

def comp(board):
    while currentplayer == "O" and gamecontinue:
        position = random.randint(0,8)
        if board[position] == "-":
            board[position] = "O"
            switchplayer()

while gamecontinue:
    printboard(board)
    playerinput(board)
    win()
    tie(board)
    switchplayer()
    comp(board)
    win()
    tie(board)
