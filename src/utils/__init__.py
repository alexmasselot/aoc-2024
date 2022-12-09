import numpy as np


def read_input(filename: str):
    with open(filename) as fd:
        return [l.replace('\n', '') for l in fd.readlines()]


def np_dense_matrix(filename: str):
    lines = read_input(filename)
    array = [
        [int(x) for x in list(l)]
        for l in lines
    ]

    return np.asmatrix(array)

