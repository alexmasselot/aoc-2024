from utils import read_input, fill_matrix, dim_matrix, print_matrix

dirs = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1)
]


def build_grid(n: int, ps: list[tuple[int, int]]):
    g = fill_matrix((n, n), '.')
    for p in ps:
        g[p[1]][p[0]] = '#'
    return g


def walk(grid, p_start):
    min_dist_target = 99999
    min_dist = fill_matrix(dim_matrix(grid), min_dist_target)

    def walk_handler(p: tuple[int, int]) -> int:
        nonlocal min_dist_target
        if grid[p[0]][p[1]] == 'E':
            min_dist_target = min(min_dist[p[0]][p[1]], min_dist_target)
        s = min_dist[p[0]][p[1]]
        for d in range(4):
            p_n = p[0] + dirs[d][0], p[1] + dirs[d][1]
            if p_n[0] < 0 or p_n[0] >= n or p_n[1] < 0 or p_n[1] >= n or grid[p_n[0]][p_n[1]] == '#':
                continue
            s_n = s + 1
            if min_dist[p_n[0]][p_n[1]] < s_n:
                continue
            min_dist[p_n[0]][p_n[1]] = s_n
            walk_handler(p_n)

    min_dist[p_start[0]][p_start[1]] = 0

    queue = [(p_start, d) for d in range(4)]
    while len(queue) > 0:
        p, d = queue.pop(0)
        if grid[p[0]][p[1]] == 'E':
            min_dist_target = min(min_dist[p[0]][p[1]], min_dist_target)
            continue

        s = min_dist[p[0]][p[1]]
        for d in range(4):
            p_n = p[0] + dirs[d][0], p[1] + dirs[d][1]
            if p_n[0] < 0 or p_n[0] >= n or p_n[1] < 0 or p_n[1] >= n or grid[p_n[0]][p_n[1]] == '#':
                continue
            s_n = s + 1
            if min_dist[p_n[0]][p_n[1]] < s_n:
                continue
            min_dist[p_n[0]][p_n[1]] = s_n
            for d1 in range(4):
                if (p_n, d1) not in queue:
                    queue.append((p_n, d1))

    # for r in min_dist:
    #     print(' '.join([str(x).ljust(6, ' ') for x in r]))
    return min_dist_target


if __name__ == '__main__':
    ps = [(int(l.split(',')[0]), int(l.split(',')[1])) for l in read_input('sample.txt')]
    n = 7
    n_bytes = 12
    ps = [(int(l.split(',')[0]), int(l.split(',')[1])) for l in read_input('input.txt')]
    n = 71
    n_bytes = 1024
    grid = build_grid(n, ps[:n_bytes])
    grid[n - 1][n - 1] = 'E'
    n_1 = walk(grid, (0, 0))
    print(n_1)


    def f_handler(i_0: int, i_1: int) -> int:
        if i_0 + 1 == i_1:
            return i_1
        i_mid = (i_0 + i_1) >> 1
        grid = build_grid(n, ps[:i_mid])
        grid[n - 1][n - 1] = 'E'
        l = walk(grid, (0, 0))
        if l == 99999:
            return f_handler(i_0, i_mid)
        else:
            return f_handler(i_mid, i_1)


    n_2 = f_handler(0, len(ps) - 1)
    print(n_2)
    print(ps[n_2-1])
# lines = read_input('input-a.txt')
