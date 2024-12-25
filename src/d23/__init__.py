from functools import cache

from utils import read_input


def set_str(s: set):
    l = list(s)
    l.sort()
    return '-'.join(l)


def largest_cluster(pool: list[str], conns: dict[str, set[str]]) -> tuple[int, list[int]]:
    memoize = {}

    def fhandler(cluster: list[str], rem: list[str], depth: int = 0) -> tuple[int, list[int]]:
        key = [*cluster]
        key.sort()
        key = '-'.join(key)
        if key in memoize:
            return memoize[key]

        tag = '\t' * depth
        # print(f'{tag}fhandler: {cluster}\t{rem}')
        if not rem:
            return len(cluster), cluster
        r_max = len(cluster)
        r_set = cluster
        for i in range(len(rem)):
            n_rem = [*rem]
            n = n_rem.pop(i)
            # print(f'{tag}n={n} nrem={n_rem}')
            # print(f'{tag}{i} {n}  {[n in conns[x] for x in cluster]}')
            if all(n in conns[x] for x in cluster):
                a, ax = fhandler([*cluster, n], n_rem, depth + 1)
                if a > r_max:
                    r_max = a
                    r_set = ax
        memoize[key] = (r_max, r_set)
        return r_max, r_set

    return fhandler(list(), list(pool))


if __name__ == '__main__':
    pairs = [(l.split('-')[0], l.split('-')[1]) for l in read_input('input.txt')]
    connections: dict[str, set[str]] = {**{p[0]: set() for p in pairs}, **{p[1]: set() for p in pairs}}
    for c1, c2 in pairs:
        connections[c1].add(c2)
        connections[c2].add(c1)

    # Part 1
    lan_3 = set()
    for x, xs in connections.items():
        for y in xs:
            for z in connections[y]:
                if z in xs:
                    lan_3.add(set_str({x, y, z}))

    print(f'part1: {len([l for l in lan_3 if "-t" in l or l.startswith("t")])}')

    # Part 2
    # adding connectionsto itself
    connections: dict[str, set[str]] = {**{p[0]: {p[0]} for p in pairs}, **{p[1]: {p[1]} for p in pairs}}
    for c1, c2 in pairs:
        connections[c1].add(c2)
        connections[c2].add(c1)
    # n_c, cs = max([largest_cluster(cs, connections) for c, cs in {'ta': connections['ta']}.items()], key=lambda a: a[0])
    n_c, cs = max([largest_cluster(cs, connections) for c, cs in connections.items()], key=lambda a: a[0])
    cs.sort()
    print(','.join(cs))
