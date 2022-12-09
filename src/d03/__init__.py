import re

from utils import read_input


def match_item(rucksack: str):
    n = len(rucksack)
    n_2 = int(n / 2)
    r_a = rucksack[0:n_2]
    p = re.compile('.*([%s]).*' % rucksack[n_2:])
    return p.match(r_a)[1]


def item_score(p):
    if p == p.lower():
        return ord(p) - ord('a') + 1
    else:
        return ord(p) - ord('A') + 27


if __name__ == '__main__':
    lines = read_input('sample.txt')
    lines = read_input('input-a.txt')

    tot_1 = 0
    for l in lines:
        p = match_item(l)
        tot_1 += item_score(p)
    print(tot_1)

    tot_2=0
    for i in range(0, int((len(lines) / 3))):
        r_0 = set(lines[i * 3])
        r_1 = set(lines[i * 3 + 1])
        r_2 = set(lines[i * 3 + 2])
        p = list(r_0.intersection(r_1).intersection(r_2))[0]
        tot_2 += item_score(p)

    print(tot_2)
