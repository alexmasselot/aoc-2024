from utils import read_input, read_input_matrix_char, find_in_matrix, fill_matrix, dim_matrix

dirs = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1)
]


def walk(grid, p_start):
    min_dist_target = 99999
    min_dist = fill_matrix(dim_matrix(grid), min_dist_target)

    def walk_handler(p: tuple[int, int], from_dir: int) -> int:
        nonlocal min_dist_target
        if grid[p[0]][p[1]] == 'E':
            min_dist_target = min(min_dist[p[0]][p[1]], min_dist_target)
        s = min_dist[p[0]][p[1]]
        for d in range(4):
            p_n = p[0] + dirs[d][0], p[1] + dirs[d][1]
            if grid[p_n[0]][p_n[1]] == '#':
                continue
            s_n = (s + 1) if d == from_dir else (s + 1001)
            if min_dist[p_n[0]][p_n[1]] < s_n:
                continue
            min_dist[p_n[0]][p_n[1]] = s_n
            walk_handler(p_n, d)

    min_dist[p_start[0]][p_start[1]] = 0
    walk_handler(p_start, 1)

    # for r in min_dist:
    #     print(' '.join([str(x).ljust(6, ' ') for x in r]))
    return min_dist_target


def min_dist_to_end(grid):
    min_dist_target = 99999
    min_dist = fill_matrix(dim_matrix(grid), min_dist_target)

    def walk_handler(p: tuple[int, int], from_dir: int) -> int:
        nonlocal min_dist_target
        if grid[p[0]][p[1]] == 'S':
            min_dist_target = min(min_dist[p[0]][p[1]], min_dist_target)
        s = min_dist[p[0]][p[1]]
        for d in range(4):
            p_n = p[0] + dirs[d][0], p[1] + dirs[d][1]
            if grid[p_n[0]][p_n[1]] == '#':
                continue
            s_n = (s + 1) if d == from_dir else (s + 1001)
            if min_dist[p_n[0]][p_n[1]] < s_n:
                continue
            min_dist[p_n[0]][p_n[1]] = s_n
            walk_handler(p_n, d)

    p_end = find_in_matrix(grid, 'E')
    min_dist[p_end[0]][p_end[1]] = 0
    walk_handler(p_end, 2)

    # for r in min_dist:
    #     print(' '.join([str(x).ljust(6, ' ') for x in r]))
    return min_dist


def walk_2(grid, p_start, d_target: int):
    all_nodes = set()

    mdte = min_dist_to_end(grid)

    def walk_handler(p: tuple[int, int], from_dir: int, dist: int, acc: list[tuple[int, int]]) -> int:
        nonlocal all_nodes
        nonlocal d_target

        # print(f'{p}\t{dist}\t{acc}')
        if dist + mdte[p[0]][p[1]] > d_target:
            return

        if grid[p[0]][p[1]] == 'E':
            if dist == d_target:
                all_nodes = all_nodes | set(acc)
        for d in range(4):
            d = (d + dist) % 4
            p_n = p[0] + dirs[d][0], p[1] + dirs[d][1]
            if grid[p_n[0]][p_n[1]] == '#':
                continue
            # print(f'?? {d}\t{p_n}')
            if p_n in acc:
                continue
            # print(f'walking {d}')
            s_n = (dist + 1) if d == from_dir else (dist + 1001)
            walk_handler(p_n, d, s_n, acc + [p_n])

    walk_handler(p_start, 1, 1, [p_start])

    return all_nodes


if __name__ == '__main__':
    grid = read_input_matrix_char('input.txt')
    p_start = find_in_matrix(grid, 'S')

    d_1 = walk(grid, p_start)
    print(d_1)
    min_dist_to_end(grid)
    d_2 = walk_2(grid, p_start, d_1 + 1)
    print(len(d_2))

    # lines = read_input('input-a.txt')
