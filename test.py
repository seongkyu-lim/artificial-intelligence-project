def hanoi(n, f_pos, b_pos, t_pos):
    if n == 1:
        move_disk(f_pos, t_pos)
        print(tower)
        return

    hanoi(n-1, f_pos, t_pos, b_pos)
    move_disk(f_pos, t_pos)
    print(tower)
    hanoi(n-1, b_pos, f_pos, t_pos)
