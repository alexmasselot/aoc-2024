filename = 'input-a.txt'

rank = {
    'A': 0,
    'B': 1,
    'C': 2
}

code = {
    'X': 'A',
    'Y': 'B',
    'Z': 'C',
}


def score(a, b):
    if a == b:
        return 3
    if (rank[a] == rank[b] + 1) or (a == 'A' and b == 'C'):
        return 0
    return 6


if __name__ == '__main__':
    with open(filename) as fd:
        tot_score_1 = 0
        tot_score_2 = 0
        for l in fd.readlines():
            [a, b] = l.strip().split(' ')
            ba = code[b]
            tot_score_1 += score(a, ba) + rank[ba] + 1

            if b == 'X':
                ba = (rank[a] - 1 + 3) % 3
                tot_score_2 += 0
            elif b == 'Y':
                ba = rank[a]
                tot_score_2 += 3
            else:
                tot_score_2 += 6
                ba = (rank[a] + 1) % 3

            tot_score_2 += ba + 1

        print(tot_score_1)
        print(tot_score_2)
