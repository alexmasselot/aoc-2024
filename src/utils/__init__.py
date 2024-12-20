import numpy as np


def read_input(filename: str):
    return [*map(str.strip, open(filename).readlines())]


def read_input_blocks(filename: str, sep='\n\n'):
    all = '\n'.join(read_input(filename))
    if sep is None:
        return [all]
    return all.split(sep)


def read_input_matrix_char(filename: str):
    return [list(l) for l in read_input(filename)]


def np_dense_matrix(filename: str):
    lines = read_input(filename)
    array = [
        [int(x) for x in list(l)]
        for l in lines
    ]

    return np.asmatrix(array)


def dim_matrix(m):
    return len(m), len(m[0])


def find_in_matrix(m, v):
    for r, row in enumerate(m):
        for c, x in enumerate(row):
            if v == x:
                return r, c
    return None


def fill_matrix(dim, v):
    n_rows, n_cols = dim
    return [[v for _ in range(n_cols)] for _ in range(n_rows)]


def print_grid(m):
    print('\n'.join(''.join(r) for r in m))


def print_matrix(m, fmt=None):
    if fmt is None:
        print('\n'.join(' '.join(r) for r in m))
    else:
        print('\n'.join(' '.join([fmt(x) for x in r]) for r in m))
