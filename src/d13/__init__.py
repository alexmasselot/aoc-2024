import json
from itertools import zip_longest, chain
from functools import cmp_to_key

from utils import read_input


def in_order(xs, ys):
    for p in zip_longest(xs, ys, fillvalue=None):
        (x, y) = p
        if x is None:
            return True
        if y is None:
            return False
        if type(x) == int and type(y) == int and x != y:
            return x < y

        if type(x) == int and isinstance(y, list):
            r = in_order([x], y)
            if r is not None:
                return r
        if type(y) == int and isinstance(x, list):
            r = in_order(x, [y])
            if r is not None:
                return r
        if isinstance(x, list) and isinstance(y, list):
            r = in_order(x, y)
            if r is not None:
                return r

    return None


if __name__ == '__main__':
    lines = read_input('input-a.txt')
    # lines = read_input('input-a.txt')
    pairs = [b.split('\n') for b in '\n'.join(lines).split('\n\n')]
    pairs = [[json.loads(b[0]), json.loads(b[1])] for b in pairs]

    # part 1
    t = 0
    for i, p in enumerate(pairs):
        if in_order(p[0], p[1]):
            t += i + 1
    print(t)

    # part 2
    packets = list(chain(*pairs))
    packets.append([2])
    packets.append([6])


    def compare_packet(xs, ys):
        return -1 if in_order(xs, ys) else 1


    packets.sort(key=cmp_to_key(compare_packet))

    print((packets.index([2])+1) * (packets.index([6])+1))
