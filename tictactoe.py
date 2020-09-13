
from random import *
import sys

board = [['~' for col in range(3)] for row in range(3)]


def win_check(board):
    if board[1][1] == 'X':
        if (board[1][0] == 'X' and board[1][2] == 'X') or (board[0][1] == 'X' and board[2][1] == 'X') or (board[0][0] == 'X' and board[2][2] == 'X') or (board[0][2] == 'X' and board[2][0] == 'X'):
            if user_piece == 'X':
                print('win')
                sys.exit(0)
            else:
                print('loss')
                sys.exit(0)

    elif board[2][0] == 'X':
        if (board[0][0] == 'X' and board[1][0] == 'X') or (board[2][1] == 'X' and board[2][2] == 'X'):
            if user_piece == 'X':
                print('win')
                sys.exit(0)
            else:
                print('loss')
                sys.exit(0)
    elif board[0][2] == 'X':
        if (board[0][0] == 'X' and board[0][1] == 'X') or (board[1][2] == 'X' and board[2][2] == 'X'):
            if user_piece == 'X':
                print('win')
                sys.exit(0)
            else:
                print('loss')
                sys.exit(0)
    elif board[1][1] == 'O':
        if (board[1][0] == 'O' and board[1][2] == 'O') or (board[0][1] == 'O' and board[2][1] == 'O') or (board[0][0] == 'O' and board[2][2] == 'O') or (board[0][2] == 'O' and board[2][0] == 'O'):
            if user_piece == 'O':
                print('win')
                sys.exit(0)
            else:
                print('loss')
                sys.exit(0)

    elif board[2][0] == 'O':
        if (board[0][0] == 'O' and board[1][0] == 'O') or (board[2][1] == 'O' and board[2][2] == 'O'):
            if user_piece == 'O':
                print('win')
                sys.exit(0)
            else:
                print('loss')
                sys.exit(0)
    elif board[0][2] == 'O':
        if (board[0][0] == 'O' and board[0][1] == 'O') or (board[1][2] == 'O' and board[2][2] == 'O'):
            if user_piece == 'O':
                print('win')
                sys.exit(0)
            else:
                print('loss')
                sys.exit(0)


def print_board(list):

    for i in list:
        for j in i:
            print(j, end=' ')
        print()


def tic_tac_toe(x, y, z):

    if z == 0:

        if board[x][y] != '~':
            x, y = map(int, input().split())
            print(' ')
            tic_tac_toe(x, y, 0)

        else:
            board[x][y] = user_piece
            print_board(board)
            print(' ')
            win_check(board)

    elif z == 1:

        if board[x][y] != '~':

            x = randint(0, 2)
            y = randint(0, 2)
            tic_tac_toe(x, y, 1)

        else:
            board[x][y] = computer_piece
            print_board(board)
            print(' ')
            win_check(board)


order_num = randint(0, 1)
if order_num == 0:
    user_piece = 'X'
    computer_piece = 'O'
else:
    user_piece = 'O'
    computer_piece = 'X'


#count = 0

if user_piece == 'X':

    while True:
        # if count == 9:
        # print('tie')
        else:
            x, y = map(int, input().split())
            print(' ')
            tic_tac_toe(x, y, 0)
            #count += 1

            x = randint(0, 2)
            y = randint(0, 2)
            tic_tac_toe(x, y, 1)
            #count += 1

else:
    while True:
        # if count == 9:
        # print('tie')
        else:
            x = randint(0, 2)
            y = randint(0, 2)
            tic_tac_toe(x, y, 1)
            #count += 1

            x, y = map(int, input().split())
            print(' ')
            tic_tac_toe(x, y, 0)
            #count += 1


# user - 0, computer - 1 // X ,  O

'''
문제점 

무승부 없다
'''
