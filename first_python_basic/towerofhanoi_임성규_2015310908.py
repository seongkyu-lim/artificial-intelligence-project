global count
count = 0
# 시행횟수를 카운트 하기 위한 전역변수 count 선언


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
# move_disk 함수를 만들어 원반이 옮겨지는 것을 tower라는 이름으로 선언된 이차원리스트에 갱신.


def print_tower(list):

    for i in list:
        for j in i:
            print(j, end=' ')
        print()
# 이차원리스트를 출력하는 함수를 따로 만듬.


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
# 재귀를 이용하여


tower = board = [[0 for col in range(3)] for row in range(3)]
tower[0][0] = 3
tower[0][1] = 2
tower[0][2] = 1
print_tower(tower)
print(' ')
# 최초 하노이 타워 생성 및 출력

hanoi(3, 0, 2, 1)
# 원반 갯수 3 개, 출발 기둥->첫번째, 중간다리 기둥->세번째, 도착 기둥->두번째

'''
재귀를 이용하여 하노이 함수를 만들고 원반을 옮겨주는 함수를 만들어 타워리스트가 갱신되도록 하였습니다.

옮긴횟수를 전역변수 count를 이용하여 세었습니다.
'''
