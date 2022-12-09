import re

from utils import read_input


def read_start(block: str):
    n = len(block.strip().split('\n')[-1].replace(' ', ''))
    w = [[] for i in range(0, n)]

    for l in block.split('\n')[0:-1]:
        for i in range(0, n):
            offset = i * 4 + 1
            if len(l) > offset and l[offset] != ' ':
                w[i].append(l[offset])
    for v in w:
        v.reverse()
    return w


def move(world, n, i_from, i_to):
    s = world[i_from - 1][(-n):]
    world[i_from - 1] = world[i_from - 1][0:(len(world[i_from - 1]) - n)]
    # for case 1, uncomment
    # s.reverse()
    world[i_to - 1].extend(s)


if __name__ == '__main__':
    lines = read_input('input-a.txt')
    [b_world, b_moves] = '\n'.join(lines).split('\n\n')
    world = read_start(b_world)

    r = re.compile('move ([0-9]+) from ([0-9]+) to ([0-9]+)')
    for l in b_moves.split('\n'):
        m = r.match(l)
        n = int(m[1])
        i_from = int(m[2])
        i_to = int(m[3])
        move(world, n, i_from, i_to)
    # lines = read_input('input-a.txt')
    sentence = []
    for w in world:
        sentence.append(w[-1])

    print(''.join(sentence))
