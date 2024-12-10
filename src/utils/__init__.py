import numpy as np


def read_input(filename: str):
    with open(filename) as fd:
        return [l.replace('\n', '') for l in fd.readlines()]


def read_input_blocks(filename: str, sep='\n\n'):
    all = '\n'.join(read_input(filename))
    if sep is None:
        return [all]
    return all.split(sep)


def np_dense_matrix(filename: str):
    lines = read_input(filename)
    array = [
        [int(x) for x in list(l)]
        for l in lines
    ]

    return np.asmatrix(array)
