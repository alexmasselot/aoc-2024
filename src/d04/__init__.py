from utils import read_input

import re

if __name__ == '__main__':
    lines = read_input('input-a.txt')
    block = '\n'.join(lines)
    n = len(lines)
    straight = '.' * n
    diag_1 = '.' * (n - 1)
    diag_2 = '.' * (n + 1)
    res = [
        r'XMAS',
        r'SAMX',
        fr'(?=X{straight}M{straight}A{straight}S)',
        fr'(?=S{straight}A{straight}M{straight}X)',
        fr'(?=X{diag_1}M{diag_1}A{diag_1}S)',
        fr'(?=S{diag_1}A{diag_1}M{diag_1}X)',
        fr'(?=X{diag_2}M{diag_2}A{diag_2}S)',
        fr'(?=S{diag_2}A{diag_2}M{diag_2}X)',
    ]

    n_1 = 0
    for rx in res:
        n_1 += len(re.findall(rx, block, re.DOTALL))
    print(n_1)

    dots = '.' * (n - 2)
    res_x = [
        fr'(?=M.M{dots}.A.{dots}S.S)',
        fr'(?=M.S{dots}.A.{dots}M.S)',
        fr'(?=S.M{dots}.A.{dots}S.M)',
        fr'(?=S.S{dots}.A.{dots}M.M)',
    ]
    n_2 = 0
    for rx in res_x:
        n_2 += len(re.findall(rx, block, re.DOTALL))
    print(n_2)
