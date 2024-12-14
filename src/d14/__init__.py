import os
import re
import time

from utils import read_input


class Bot:
    p: tuple[int, int]
    v: tuple[int, int]

    def __init__(self, input: str):
        rx = f'''p=(\\-?\\d+),(\\-?\\d+) v=(\\-?\\d+),(\\-?\\d+)'''
        m = re.match(rx, input)
        self.p = int(m.group(1)), int(m.group(2))
        self.v = int(m.group(3)), int(m.group(4))

    def __eq__(self, other):
        if not isinstance(other, Bot):
            return False
        return self.p == other.p and self.v == other.v

    def __hash__(self):
        return hash((self.p, self.v))

    def __str__(self):
        return f'{self.p[0]}\t{self.p[1]}\t{self.v[0]}\t{self.v[1]}'

    def __repr__(self):
        return f'{self.p[0]}\t{self.p[1]}\t{self.v[0]}\t{self.v[1]}'

    def step(self, dim: tuple[int, int], n=1):
        self.p = (self.p[0] + self.v[0] * n) % dim[0], (self.p[1] + self.v[1] * n) % dim[1]


def map_string(bots: list[Bot], dim=tuple[int]):
    grid = [['.' for _ in range(dim[0])] for _ in range(dim[1])]
    for b in bots:
        grid[b.p[1]][b.p[0]] = 'X'

    return '\n'.join([''.join(l) for l in grid])


def count_quadrants(bots: list[Bot], dim=tuple[int]):
    mid = (dim[0] - 1) / 2, (dim[1] - 1) / 2
    q0 = len([b for b in bots if b.p[0] < mid[0] and b.p[1] < mid[1]])
    q1 = len([b for b in bots if b.p[0] < mid[0] and b.p[1] > mid[1]])
    q2 = len([b for b in bots if b.p[0] > mid[0] and b.p[1] < mid[1]])
    q3 = len([b for b in bots if b.p[0] > mid[0] and b.p[1] > mid[1]])
    return ((q0, q2), (q1, q3))


def part_1(bots: list[Bot], dim=tuple[int]):
    steps = 100
    for b in bots:
        b.step(dim, steps)

    cq = count_quadrants(bots, dim)

    map_string(bots, dim)
    print(cq[0][0] * cq[0][1] * cq[1][0] * cq[1][1])


def check_symmetric(bots: list[Bot], dim: tuple[int], step: int) -> bool:
    mid_x = (dim[0] - 1) / 2
    b_left = [b.p for b in bots if b.p[0] < mid_x]
    b_right = [(dim[0] - 1 - b.p[0], b.p[1]) for b in bots if b.p[0] > mid_x]
    b_left.sort(key=lambda p: p[0] * 10000 + p[1])
    b_right.sort(key=lambda p: p[0] * 10000 + p[1])

    row_left = [[] for _ in range(dim[1])]
    row_right = [[] for _ in range(dim[1])]
    for p in b_left:
        row_left[p[1]].append(p[0])
    for p in b_right:
        row_right[p[1]].append(p[0])
    for y, px in enumerate(zip(row_left, row_right)):
        if len(px[0]) == 0:
            continue
        if px[0] == px[1]:
            print(f'{step}\t{y}\t{[b for b in bots if b.p[1] == y]}')
    if (len(b_left) != len(b_right)):
        return False
    return b_left == b_right


def part_2(bots: list[Bot], dim=tuple[int]):
    #    for b in bots:
    #        b.step(dim, 59)
    with open ('d14-scrren.txt', 'w') as fd:
        for s in range(dim[0] * dim[1]):
            fd.write(f'--------- {s} ---------------\n')
            fd.write(map_string(bots, dim))
            fd.write('\n')
            for b in bots:
                b.step(dim)

if __name__ == '__main__':
    lines = read_input('input.txt')
    bots = [Bot(l) for l in lines]
    dim = 11, 7
    bots = [Bot(l) for l in lines]
    dim = 101, 103

    part_2(bots, dim)
    # bots.sort(key=lambda b: b.v[1])
    # print(f'len ={len(bots)}')
    # for b in bots:
    #     print(b)
