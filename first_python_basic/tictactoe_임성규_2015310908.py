
from random import *
import sys

board = [['~' for col in range(3)] for row in range(3)]

global count
count = 0


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
# 승리여부를 체크하여 출력하고 게임종료하는 함수


def print_board(list):

    for i in list:
        for j in i:
            print(j, end=' ')
        print()
# 진행판 출력함수


def tic_tac_toe(x, y, z):
    global count

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
            count += 1
            if count == 9:
                print('tie')
                sys.exit(0)

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
            count += 1
            if count == 9:
                print('tie')
                sys.exit(0)
# 말을 놓는 것을 실행하는 함수


order_num = randint(0, 1)
if order_num == 0:
    user_piece = 'X'
    computer_piece = 'O'
else:
    user_piece = 'O'
    computer_piece = 'X'
# 랜덤으로 순서 결정.

if user_piece == 'X':

    while True:
        x, y = map(int, input().split())
        print(' ')
        tic_tac_toe(x, y, 0)

        x = randint(0, 2)
        y = randint(0, 2)
        tic_tac_toe(x, y, 1)

else:
    while True:
        x = randint(0, 2)
        y = randint(0, 2)
        tic_tac_toe(x, y, 1)

        x, y = map(int, input().split())
        print(' ')
        tic_tac_toe(x, y, 0)


'''
tic-tac-toe 함수로 유저 혹은 컴퓨터가 특정 위치에 말을 놓도록 하였습니다.
말을 놓고나면 win_check함수로 게임종료여부를 체크하고 누군가가 이겼다면 게임을 종료하도록하였습니다.
print_board라는 진행상황 출력 함수를 따로 만들어 말을 놓을 때마다 현재 진행상황이 출력되도록 하였습니다.
말을 놓고 win_check로 결판이 나지않았을 때, 총 9번 두었다면 무승부로 게임을 종료 시켰습지

'''
