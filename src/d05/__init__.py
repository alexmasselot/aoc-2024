import re

from utils import read_input, read_input_blocks


def parse_is_not_before(block: str) -> dict[int, set[int]]:
    d = {}
    pattern = re.compile('''([0-9]+)\\|([0-9]+)''')
    for l in block.split('\n'):
        m = pattern.match(l)
        i = int(m.group(1))
        j = int(m.group(2))
        if j not in d:
            d[j] = set()
        d[j].add(i)

    return d


def parse_is_before(block: str) -> dict[int, set[int]]:
    d = {}
    pattern = re.compile('''([0-9]+)\\|([0-9]+)''')
    for l in block.split('\n'):
        m = pattern.match(l)
        i = int(m.group(1))
        j = int(m.group(2))
        if i not in d:
            d[i] = set()
        d[i].add(j)

    return d


def parse_sequences(block: str) -> list[list[int]]:
    return [list(map(int, line.split(','))) for line in block.strip().split('\n')]


def is_correct(seq: list[int], is_not_bef: dict[int, set[int]]):
    # print(seq)
    cmp = list(zip(seq, seq[1:]))
    for p in cmp:
        i0 = p[0]
        i1 = p[1]
        if i0 in is_not_bef and i1 in is_not_bef[i0]:
            # print(f'{i0},{i1}\t{i1 in is_not_bef and i0 in is_not_bef[i1]}')
            return False
    return True


if __name__ == '__main__':
    blocks = read_input_blocks('input-a.txt')
    # blocks = read_input_blocks('sample.txt')
    is_not_before = parse_is_not_before(blocks[0])
    is_before = parse_is_before(blocks[0])

    pages = list(is_before.keys())
    pages.sort()
    pages_before = []
    for x in pages:
        xs = list(is_before[x])
        xs.sort()
        # print(xs)
        xs = [False for _ in range(100)]
        for i in is_before[x]:
            xs[i] = True
        # xs = ''.join(['| ' if y else '- ' for y in xs])
        xs = ''.join([y if i in pages else '' for i, y in enumerate(['|' if y else '-' for y in xs])])
        pages_before.append(xs)
        print(f'{x}\t{len(is_before[x])}\t{xs}')

    sequences = parse_sequences(blocks[1])
    tot = 0
    tot_2 = 0
    for seq in sequences:
        c = is_correct(seq, is_not_before)
        if c:
            tot += seq[int((len(seq) - 1) / 2)]
        else:
            for i in seq:
                c = len([1 for j in seq if j in is_before[i]])
                if c == (len(seq) - 1) / 2:
                    tot_2 += i

    print(f'part1 {tot}')
    print(f'part2 {tot_2}')
    # lines = read_input('input-a.txt')
