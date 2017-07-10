###  CHESSGAME.PY  ###

import numpy as np
import os
import time
import sys

###  CREATE MATRIX  ###

matrix = np.zeros(shape=(8,8))
str_matrix = np.array(matrix, dtype=str)

###  DEFINE VARIABLES  ###

whiteTurns = 0
gameWon = False
rows = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}
whiteGamePieces = ["R", "H", "B", "Q", "K", "P"]
blackGamePieces = ["r", "h", "b", "q", "k", "p"]

###  DRAW BOARD  ###

def startGame():
    for i in range(0,8):
        for j in range(0,8):
            str_matrix[i][j] = "[ ]"
    str_matrix[0][0] = "[r]"
    str_matrix[0][1] = "[h]"
    str_matrix[0][2] = "[b]"    ### [R] [H] [B] [Q] [K] [B] [H] [R] ###   <---- = [0][7]
    str_matrix[0][3] = "[q]"
    str_matrix[0][4] = "[k]"    ### [P] [P] [P] [P] [P] [P] [P] [P] ###
    str_matrix[0][5] = "[b]"
    str_matrix[0][6] = "[h]"    ### [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] ###
    str_matrix[0][7] = "[r]"
    str_matrix[1, :] = "[p]"    ### [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] ###
    str_matrix[7][0] = "[R]"
    str_matrix[7][1] = "[H]"    ### [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] ###
    str_matrix[7][2] = "[B]"
    str_matrix[7][3] = "[Q]"    ### [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] ###
    str_matrix[7][4] = "[K]"
    str_matrix[7][5] = "[B]"    ### [P] [P] [P] [P] [P] [P] [P] [P] ###
    str_matrix[7][6] = "[H]"
    str_matrix[7][7] = "[R]"    ### [R] [H] [B] [Q] [K] [B] [H] [R] ###   <---- = [7][7]
    str_matrix[6, :] = "[P]"
startGame()

###  INDIVIDUAL PIECE MOVES  ###

def printBoard(matrix):
    for row in matrix:
        for cell in row:
            print cell + " ",
        print("\n")


def invalidMove():
    global whiteTurns
    print("Not a Valid Move")
    whiteTurns += 1
    whiteMove()

def pawnWhiteStartMove(move):
    str_matrix[8-int(move[1])][rows.get(move[0])] = '[ ]'
    str_matrix[8-int(move[4])][rows.get(move[3])] = '[P]'
    printBoard(str_matrix)

def pawnWhiteMove(move):
    str_matrix[8-int(move[1])][rows.get(move[0])] = '[ ]'
    str_matrix[8-int(move[4])][rows.get(move[3])] = '[P]'
    printBoard(str_matrix)

def rookWhiteMove(move):
    str_matrix[8-int(move[1])][rows.get(move[0])] = '[ ]'
    str_matrix[8-int(move[4])][rows.get(move[3])] = '[R]'
    printBoard(str_matrix)

def horseWhiteMove(move):
    str_matrix[8-int(move[1])][rows.get(move[0])] = '[ ]'
    str_matrix[8-int(move[4])][rows.get(move[3])] = '[H]'
    printBoard(str_matrix)

def bishopWhiteMove(move):
    str_matrix[8-int(move[1])][rows.get(move[0])] = '[ ]'
    str_matrix[8-int(move[4])][rows.get(move[3])] = '[B]'
    printBoard(str_matrix)

def queenWhiteMove(move):
    str_matrix[8-int(move[1])][rows.get(move[0])] = '[ ]'
    str_matrix[8-int(move[4])][rows.get(move[3])] = '[Q]'
    printBoard(str_matrix)

def kingWhiteMove(move):
    str_matrix[8-int(move[1])][rows.get(move[0])] = '[ ]'
    str_matrix[8-int(move[4])][rows.get(move[3])] = '[K]'
    printBoard(str_matrix)

print("\n")
printBoard(str_matrix)

###  START GAME  ###

def whiteMove():
    global whiteTurns
    move = raw_input("White to Move - Please Type a Valid Move: (ex. A1:A3)\n")
    
###  PAWN MOVES  ###
    
    if(str_matrix[8-int(move[1])][rows.get(move[0])] == '[P]' and 8-int(move[1])-(8-int(move[4])) == 2 and rows.get(move[0]) == rows.get(move[3]) and str_matrix[8-int(move[4])][rows.get(move[0])] == '[ ]'):
        pawnWhiteStartMove(move)
    elif(str_matrix[8-int(move[1])][rows.get(move[0])] == '[P]' and 8-int(move[1])-(8-int(move[4])) == 1 and rows.get(move[0]) == rows.get(move[3]) and str_matrix[8-int(move[4])][rows.get(move[0])] == '[ ]'):
        pawnWhiteMove(move)
    elif(str_matrix[8-int(move[1])][rows.get(move[0])] == '[P]' and 8-int(move[1])-(8-int(move[4])) == 1 and 1+rows.get(move[0]) == rows.get(move[3]) and str_matrix[8-int(move[4])][rows.get(move[3])] != '[ ]'):
        pawnWhiteMove(move)
    elif(str_matrix[8-int(move[1])][rows.get(move[0])] == '[P]' and 8-int(move[1])-(8-int(move[4])) == 1 and rows.get(move[0])-1 == rows.get(move[3]) and str_matrix[8-int(move[4])][rows.get(move[3])] != '[ ]'):
        pawnWhiteMove(move)

###  ROOK MOVES  ###

    elif(str_matrix[8-int(move[1])][rows.get(move[0])] == '[R]' and rows.get(move[0]) == rows.get(move[3]) and str_matrix[8-int(move[4])][rows.get(move[3])] == '[ ]'):
        for i in range(8-int(move[1])-1, (8-int(move[4])), -1):
            if(str_matrix[i][rows.get(move[0])] != '[ ]'):
                invalidMove()
                break
        else:
            rookWhiteMove(move)

###  KNIGHT MOVES  ###

    elif(str_matrix[8-int(move[1])][rows.get(move[0])] == '[H]' and 1+rows.get(move[0]) == rows.get(move[3]) and (abs(8-int(move[1])-(8-int(move[4])))) == 2 and str_matrix[8-int(move[4])][rows.get(move[3])] == '[ ]'):
        horseWhiteMove(move)
    elif(str_matrix[8-int(move[1])][rows.get(move[0])] == '[H]' and rows.get(move[0])-1 == rows.get(move[3]) and (abs(8-int(move[1])-(8-int(move[4])))) == 2 and str_matrix[8-int(move[4])][rows.get(move[3])] == '[ ]'):
        horseWhiteMove(move)
    elif(str_matrix[8-int(move[1])][rows.get(move[0])] == '[H]' and 2+rows.get(move[0]) == rows.get(move[3]) and (abs(8-int(move[1])-(8-int(move[4])))) == 1 and str_matrix[8-int(move[4])][rows.get(move[3])] == '[ ]'):
        horseWhiteMove(move)
    elif(str_matrix[8-int(move[1])][rows.get(move[0])] == '[H]' and rows.get(move[0])-2 == rows.get(move[3]) and (abs(8-int(move[1])-(8-int(move[4])))) == 1 and str_matrix[8-int(move[4])][rows.get(move[3])] == '[ ]'):
        horseWhiteMove(move)
    elif(str_matrix[8-int(move[1])][rows.get(move[0])] == '[H]' and 1+rows.get(move[0]) == rows.get(move[3]) and (abs(8-int(move[1])-(8-int(move[4])))) == 2 and str_matrix[8-int(move[4])][rows.get(move[3])] != '[ ]'):
        horseWhiteMove(move)
    elif(str_matrix[8-int(move[1])][rows.get(move[0])] == '[H]' and rows.get(move[0])-1 == rows.get(move[3]) and (abs(8-int(move[1])-(8-int(move[4])))) == 2 and str_matrix[8-int(move[4])][rows.get(move[3])] != '[ ]'):
        horseWhiteMove(move)
    elif(str_matrix[8-int(move[1])][rows.get(move[0])] == '[H]' and 2+rows.get(move[0]) == rows.get(move[3]) and (abs(8-int(move[1])-(8-int(move[4])))) == 1 and str_matrix[8-int(move[4])][rows.get(move[3])] != '[ ]'):
        horseWhiteMove(move)
    elif(str_matrix[8-int(move[1])][rows.get(move[0])] == '[H]' and rows.get(move[0])-2 == rows.get(move[3]) and (abs(8-int(move[1])-(8-int(move[4])))) == 1 and str_matrix[8-int(move[4])][rows.get(move[3])] != '[ ]'):
        horseWhiteMove(move)

###  QUEEN MOVES  ###

    elif(str_matrix[8-int(move[1])][rows.get(move[0])] == '[Q]' and 1+rows.get(move[0]) == rows.get(move[3]) and (abs(8-int(move[1])-(8-int(move[4])))) == 0 and str_matrix[8-int(move[4])][rows.get(move[3])] == '[ ]'):
        kingWhiteMove(move)
    elif(str_matrix[8-int(move[1])][rows.get(move[0])] == '[Q]' and rows.get(move[0])-1 == rows.get(move[3]) and (abs(8-int(move[1])-(8-int(move[4])))) == 0 and str_matrix[8-int(move[4])][rows.get(move[3])] == '[ ]'):
        kingWhiteMove(move)
    elif(str_matrix[8-int(move[1])][rows.get(move[0])] == '[Q]' and 1+rows.get(move[0]) == rows.get(move[3]) and (abs(8-int(move[1])-(8-int(move[4])))) == 1 and str_matrix[8-int(move[4])][rows.get(move[3])] == '[ ]'):
        kingWhiteMove(move)
    elif(str_matrix[8-int(move[1])][rows.get(move[0])] == '[Q]' and rows.get(move[0])-1 == rows.get(move[3]) and (abs(8-int(move[1])-(8-int(move[4])))) == 1 and str_matrix[8-int(move[4])][rows.get(move[3])] == '[ ]'):
        kingWhiteMove(move)
    elif(str_matrix[8-int(move[1])][rows.get(move[0])] == '[Q]' and rows.get(move[0]) == rows.get(move[3]) and (abs(8-int(move[1])-(8-int(move[4])))) == 1 and str_matrix[8-int(move[4])][rows.get(move[3])] == '[ ]'):
        kingWhiteMove(move)
    elif(str_matrix[8-int(move[1])][rows.get(move[0])] == '[Q]' and rows.get(move[0]) == rows.get(move[3]) and str_matrix[8-int(move[4])][rows.get(move[3])] == '[ ]'):
        for i in range(8-int(move[1])-1, (8-int(move[4])), -1):
            if(str_matrix[i][rows.get(move[0])] != '[ ]'):
                invalidMove()
                break
            else:
                rookWhiteMove(move)

###  KING MOVES  ###

    elif(str_matrix[8-int(move[1])][rows.get(move[0])] == '[K]' and 1+rows.get(move[0]) == rows.get(move[3]) and (abs(8-int(move[1])-(8-int(move[4])))) == 0 and str_matrix[8-int(move[4])][rows.get(move[3])] == '[ ]'):
        kingWhiteMove(move)
    elif(str_matrix[8-int(move[1])][rows.get(move[0])] == '[K]' and rows.get(move[0])-1 == rows.get(move[3]) and (abs(8-int(move[1])-(8-int(move[4])))) == 0 and str_matrix[8-int(move[4])][rows.get(move[3])] == '[ ]'):
        kingWhiteMove(move)
    elif(str_matrix[8-int(move[1])][rows.get(move[0])] == '[K]' and 1+rows.get(move[0]) == rows.get(move[3]) and (abs(8-int(move[1])-(8-int(move[4])))) == 1 and str_matrix[8-int(move[4])][rows.get(move[3])] == '[ ]'):
        kingWhiteMove(move)
    elif(str_matrix[8-int(move[1])][rows.get(move[0])] == '[K]' and rows.get(move[0])-1 == rows.get(move[3]) and (abs(8-int(move[1])-(8-int(move[4])))) == 1 and str_matrix[8-int(move[4])][rows.get(move[3])] == '[ ]'):
        kingWhiteMove(move)
    elif(str_matrix[8-int(move[1])][rows.get(move[0])] == '[K]' and rows.get(move[0]) == rows.get(move[3]) and (abs(8-int(move[1])-(8-int(move[4])))) == 1 and str_matrix[8-int(move[4])][rows.get(move[3])] == '[ ]'):
        kingWhiteMove(move)

###  INVALID MOVE  ###

    else:
        invalidMove()

###  REPEAT GAME  ###

while gameWon == False:
    whiteMove()
