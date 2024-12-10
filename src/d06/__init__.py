from re import Pattern

from utils import read_input


def print_map(m, n):
    print('\n\n')
    mi = ['#' if i == 1 << 4 else str(i) for i in m]
    print('\n'.join([''.join(mi[i * n:(i + 1) * n]) for i in range(n)]))


def walk(p_start, map, n):
    """
    return walked map if can exit. True if there is a loop
    :param p_start:
    :param map:
    :param n:
    :return:
    """
    dir = 0
    move = [-n, 1, n, -1]
    p = p_start
    map[p] = 1 << 0
    while True:
        step = move[dir]
        dir_mask = 1 << dir
        p1 = p + step
        if p1 < 0 or p1 >= n * n:
            return map
        if step == 1 and p1 % n == 0:
            return map
        if step == -1 and p % n == 0:
            return map
        if map[p1] == 1 << 4:
            dir = (dir + 1) % 4
            continue
        if (map[p1] & dir_mask) != 0:
            return True
        map[p1] = map[p1] | dir_mask
        p = p1


if __name__ == '__main__':
    lines = read_input('input-a.txt')
    n = len(lines)
    map = ''.join(lines)
    p_start = map.index('^')
    map = [1 << 4 if c == '#' else 0 for c in list(''.join(lines))]

    map_w = walk(p_start, [*map], n)
    tot_1 = len([1 for x in map_w if 0 < x < (1 << 4)])
    print(f'part 1: {tot_1}')

    nb_obs = 0
    for io in range(n * n):
        if io == p_start or map[io] == 1 << 4:
            continue
        map_w = [*map]
        map_w[io] = 1 << 4
        if walk(p_start, map_w, n) is True:
            nb_obs += 1
    print(f'part 2: {nb_obs}')
