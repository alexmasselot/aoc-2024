import itertools

from utils import read_input


def build_connections(alts):
    """
    for each poition, give the coordinates where it is possible to walk to
    :param alts:
    :return:
    """
    connections = []
    for r, alt_row in enumerate(alts):
        connection_row = []
        for c, el in enumerate(alt_row):
            z = el[0]
            neighb = []
            if c > 0 and alts[r][c - 1][0] == z + 1:
                neighb.append((r, c - 1))
            if c < n - 1 and alts[r][c + 1][0] == z + 1:
                neighb.append((r, c + 1))
            if r > 0 and alts[r - 1][c][0] == z + 1:
                neighb.append((r - 1, c))
            if r < n - 1 and alts[r + 1][c][0] == z + 1:
                neighb.append((r + 1, c))
            connection_row.append(neighb)
        connections.append(connection_row)
    return connections


def summits(alts, connections, pos, nines):
    if pos in nines:
        return 1, {pos}
    neighbs = connections[pos[0]][pos[1]]
    if not neighbs:
        return None
    pxs = set()
    nb_trails = 0
    for neighb in neighbs:
        px = summits(alts, connections, neighb, nines)
        if px:
            pxs = pxs | px[1]
            nb_trails += px[0]
    return nb_trails, pxs


if __name__ == '__main__':
    lines = read_input('input-a.txt')
    n = len(lines)
    alts = [[(int(x), (r, c)) for c, x in enumerate(list(l))] for r, l in enumerate(lines)]

    els = list(itertools.chain(*alts))
    zeros = [e[1] for e in els if e[0] == 0]
    nines = {e[1] for e in els if e[0] == 9}
    connections = build_connections(alts)

    tot_1 = 0
    tot_2 = 0
    for z in zeros:
        sts = summits(alts, connections, z, nines)
        tot_1 += len(sts[1])
        tot_2 += sts[0]
    print(tot_1)
    print(tot_2)
