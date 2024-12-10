import re

from utils import read_input


def combine(x1: int, x2: int):
    return int(f'{x1}{x2}')


def is_operable_1(tot: int, acc: int, xs: list[int]) -> bool:
    if acc > tot:
        return False
    if acc == tot and len(xs) == 0:
        return True
    if len(xs) == 0:
        return False
    if acc == 0:
        return is_operable_1(tot, xs[0] + xs[1], xs[2:]) or is_operable_1(tot, xs[0] * xs[1], xs[2:])
    return is_operable_1(tot, acc + xs[0], xs[1:]) or is_operable_1(tot, acc * xs[0], xs[1:])


def is_operable_2(tot: int, acc: int, xs: list[int]) -> bool:
    if acc > tot:
        return False
    if acc == tot and len(xs) == 0:
        return True
    if len(xs) == 0:
        return False
    if acc == 0:
        return is_operable_2(tot, xs[0] + xs[1], xs[2:]) or is_operable_2(tot, xs[0] * xs[1], xs[2:]) or is_operable_2(tot, combine(xs[0], xs[1]), xs[2:])
    return is_operable_2(tot, acc + xs[0], xs[1:]) or is_operable_2(tot, acc * xs[0], xs[1:]) or is_operable_2(tot, combine(acc, xs[0]), xs[1:])


if __name__ == '__main__':
    lines = read_input('input-a.txt')
    re_input = r'(.*): (.*)'
    input = []
    for l in lines:
        m = re.match(re_input, l)
        input.append((int(m.group(1)), list(map(int, m.group(2).split(' ')))))
    tot_1 = 0
    for inp in input:
        if is_operable_1(inp[0], 0, inp[1]):
            tot_1 += inp[0]
    print(tot_1)

    tot_2 = 0
    for inp in input:
        if is_operable_2(inp[0], 0, inp[1]):
            tot_2 += inp[0]
    print(tot_2)
    # lines = read_input('input-a.txt')
