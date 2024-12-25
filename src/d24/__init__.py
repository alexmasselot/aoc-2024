import re

from utils import read_input, read_input_blocks


def read_values(init_input: str, dep_input: str):
    vs = {}
    for l in init_input.split('\n'):
        t = l.split(': ')
        vs[t[0]] = t[1] == '1'

    rx = r'''([a-z0-9]+) ([A-Z]+) ([a-z0-9]+) .> ([a-z0-9]+)'''
    for l in dep_input.split('\n'):
        m = re.match(rx, l)
        vs[m.group(4)] = (m.group(1), m.group(3), m.group(2))

    return vs


def compute(k: str, tv: dict):
    kv = tv[k]
    if isinstance(kv, int):
        return kv
    a, b, op = kv
    av = compute(a, tv)
    bv = compute(b, tv)
    if op == 'XOR':
        return av ^ bv
    if op == 'OR':
        return av | bv
    if op == 'AND':
        return av & bv
    print('FUCK')


if __name__ == '__main__':
    blocks = read_input_blocks('input.txt')
    value_tree = read_values(blocks[0], blocks[1])
    print(value_tree)

    zs = [k for k in value_tree.keys() if k.startswith('z')]
    zs.sort()
    zs.reverse()
    tot = 0
    for z in zs:
        zv = compute(z, value_tree)
        tot = (tot << 1) + zv
    print(tot)

# lines = read_input('input-a.txt')
