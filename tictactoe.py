
from random import *

board = [[0 for col in range(3)] for row in range(3)]


def tic_tac_toe(x, y, z):

    if z == 0:

        if board[x][y] != 0:

            print("retry")

        else:
            board[x][y] = user_piece

        print(board)

    elif z == 1:

        if board[x][y] != 0:

            print("retry")

        else:
            board[x][y] = computer_piece

        print(board)


order_num = randint(0, 1)
print(order_num)
if order_num == 0:
    user_piece = 'X'
    computer_piece = 'O'
else:
    user_piece = 'O'
    computer_piece = 'X'


print(user_piece)
print(computer_piece)


if user_piece == 'X':

    while True:
        x, y = map(int, input().split())
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
        tic_tac_toe(x, y, 0)


### user - 0, computer - 1 // X ,  O
