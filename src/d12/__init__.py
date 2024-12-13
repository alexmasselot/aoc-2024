import itertools

from utils import read_input, read_input_matrix_char


def tag_from(grid, n, r, c, i_lab):
    taggued = {}
    x = grid[r][c]
    if isinstance(x, int):
        return
    grid[r][c] = i_lab
    # print(f'{i_lab}  -->  {grid[r][c]}')

    taggued[i_lab] = grid[r][c]
    if c > 0 and grid[r][c - 1] == x:
        tag_from(grid, n, r, c - 1, i_lab)
    if c < n - 1 and grid[r][c + 1] == x:
        tag_from(grid, n, r, c + 1, i_lab)
    if r > 0 and grid[r - 1][c] == x:
        tag_from(grid, n, r - 1, c, i_lab)
    if r < n - 1 and grid[r + 1][c] == x:
        tag_from(grid, n, r + 1, c, i_lab)
    return taggued


def price_1(grid, n):
    tot_1 = 0
    labels = set(itertools.chain(*grid))

    for label in labels:
        n_lab = len([c for c in itertools.chain(*grid) if c == label])
        p = 4 * n_lab
        for r, row in enumerate(grid):
            for c, l in enumerate(row):
                if l != label:
                    continue
                if c > 0 and row[c - 1] == label:
                    p = p - 1
                if c < n - 1 and row[c + 1] == label:
                    p = p - 1
                if r > 0 and grid[r - 1][c] == label:
                    p = p - 1
                if r < n - 1 and grid[r + 1][c] == label:
                    p = p - 1
        tot_1 += n_lab * p
    return tot_1


def is_same_east(grid, n, r, c):
    if c < 0 or c >= n or r < 0 or r >= n:
        return False
    label = grid[r][c]
    return c < n - 1 and grid[r][c + 1] == label


def is_same_west(grid, n, r, c):
    if c < 0 or c >= n or r < 0 or r >= n:
        return False
    label = grid[r][c]
    return c > 0 and grid[r][c - 1] == label


def is_same_north(grid, n, r, c):
    if c < 0 or c >= n or r < 0 or r >= n:
        return False
    label = grid[r][c]
    return r > 0 and grid[r - 1][c] == label


def is_same_south(grid, n, r, c):
    if c < 0 or c >= n or r < 0 or r >= n:
        return False
    label = grid[r][c]
    return r < n - 1 and grid[r + 1][c] == label


def price_2(grid, n):
    tot_1 = 0
    labels = set(itertools.chain(*grid))

    for label in labels:
        n_lab = len([c for c in itertools.chain(*grid) if c == label])
        p = 4 * n_lab
        # print(f'----------- {label} -------')
        for r, row in enumerate(grid):
            for c, l in enumerate(row):
                if l != label:
                    continue
                if is_same_east(grid, n, r, c):
                    p = p - 1
                if is_same_west(grid, n, r, c):
                    p = p - 1
                if is_same_north(grid, n, r, c):
                    p = p - 1
                if is_same_south(grid, n, r, c):
                    p = p - 1
                # print(f'{r}\t{c}')
                if is_same_east(grid, n, r, c) and not is_same_north(grid, n, r, c) and not is_same_north(grid, n, r, c + 1):
                    p = p - 1
                    # print(f'rm east  {r} {c}')
                if is_same_west(grid, n, r, c) and not is_same_south(grid, n, r, c) and not is_same_south(grid, n, r, c - 1):
                    p = p - 1
                    # print(f'rm west  {r} {c}')
                if is_same_north(grid, n, r, c) and not is_same_east(grid, n, r, c) and not is_same_east(grid, n, r - 1, c):
                    p = p - 1
                    # print(f'rm north {r} {c}')
                if is_same_south(grid, n, r, c) and not is_same_west(grid, n, r, c) and not is_same_west(grid, n, r + 1, c):
                    p = p - 1
                    # print(f'rm south {r} {c}')
        tot_1 += n_lab * p
        # print(f'{label}\t{n_lab}\t{p}')
    return tot_1


def tag_grid(grid, n):
    for r in range(n):
        for c in range(n):
            tag_from(grid, n, r, c, r * n + c)


if __name__ == '__main__':
    grid = read_input_matrix_char('input-a.txt')
    n = len(grid)

    tag_grid(grid, n)

    print(price_1(grid, n))
    print(price_2(grid, n))
    # lines = read_input('input-a.txt')
