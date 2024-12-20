from utils import read_input, read_input_matrix_char, find_in_matrix, fill_matrix, dim_matrix, print_matrix

dirs = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1)
]


def walk(grid, p_start):
    min_dist_target = 99999
    min_dist = fill_matrix(dim_matrix(grid), min_dist_target)
    n = dim_matrix(grid)[0]

    # def walk_handler(p: tuple[int, int]) -> int:
    #     nonlocal min_dist_target
    #     if grid[p[0]][p[1]] == 'E':
    #         min_dist_target = min(min_dist[p[0]][p[1]], min_dist_target)
    #         return
    #     s = min_dist[p[0]][p[1]]
    #     for d in range(4):
    #         p_n = p[0] + dirs[d][0], p[1] + dirs[d][1]
    #         if grid[p_n[0]][p_n[1]] == '#':
    #             continue
    #         s_n = s + 1
    #         if min_dist[p_n[0]][p_n[1]] < s_n:
    #             continue
    #         min_dist[p_n[0]][p_n[1]] = s_n
    #         walk_handler(p_n)

    min_dist[p_start[0]][p_start[1]] = 0
    # walk_handler(p_start)

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
    return min_dist_target, min_dist


if __name__ == '__main__':
    grid = read_input_matrix_char('input.txt')
    n = dim_matrix(grid)[0]

    p_start = find_in_matrix(grid, 'S')

    longest_short, dist_start = walk(grid, p_start)

    savings = [0 for _ in range(longest_short)]
    for r in range(n):
        for c in range(n):
            for d in range(4):
                p_n = r + 2 * dirs[d][0], c + 2 * dirs[d][1]
                if 0 <= p_n[0] < n and 0 <= p_n[1] < n and grid[p_n[0]][p_n[1]] != '#' and grid[r][c] != '#':
                    shortcut = dist_start[p_n[0]][p_n[1]] - dist_start[r][c]
                    if shortcut > 0:
                        savings[shortcut - 2] += 1

    for i, s in enumerate(savings):
        if s > 0:
            print(f'{i}\t{s}')
    print(sum([s for i, s in enumerate(savings) if i>=100]))
    # lines = read_input('input-a.txt')
