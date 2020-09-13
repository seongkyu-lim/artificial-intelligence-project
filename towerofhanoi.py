global count
count = 0


def move_disk(x, y):
    if tower[x][2] == 0:
        if tower[x][1] == 0:
            a = tower[x][0]
            tower[x][0] = 0
            if tower[y][2] == 0:
                if tower[y][1] == 0:
                    if tower[y][0] == 0:
                        tower[y][0] = a
                    else:
                        tower[y][1] = a
                else:
                    tower[y][2] = a
        else:
            a = tower[x][1]
            tower[x][1] = 0
            if tower[y][2] == 0:
                if tower[y][1] == 0:
                    if tower[y][0] == 0:
                        tower[y][0] = a
                    else:
                        tower[y][1] = a
                else:
                    tower[y][2] = a
    else:
        a = tower[x][2]
        if tower[y][2] == 0:
            if tower[y][1] == 0:
                if tower[y][0] == 0:
                    tower[y][0] = a
                else:
                    tower[y][1] = a
            else:
                tower[y][2] = a
        tower[x][2] = 0


def print_tower(list):

    for i in list:
        for j in i:
            print(j, end=' ')
        print()


def hanoi(n, A_rod, C_rod, B_rod):
    global count
    if n == 1:
        move_disk(A_rod, B_rod)
        count += 1
        print(count)
        print_tower(tower)
        print(' ')
        return

    hanoi(n-1, A_rod, B_rod, C_rod)
    move_disk(A_rod, B_rod)
    count += 1
    print(count)
    print_tower(tower)
    print(' ')
    hanoi(n-1, C_rod, A_rod, B_rod)


tower = board = [[0 for col in range(3)] for row in range(3)]
tower[0][0] = 3
tower[0][1] = 2
tower[0][2] = 1
print_tower(tower)
print(' ')

hanoi(3, 0, 2, 1)
