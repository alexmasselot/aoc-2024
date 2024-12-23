from utils import read_input


def set_str(s: set):
    l = list(s)
    l.sort()
    return '-'.join(l)


if __name__ == '__main__':
    pairs = [(l.split('-')[0], l.split('-')[1]) for l in read_input('input.txt')]
    connections: dict[str, set[str]] = {**{p[0]: set() for p in pairs}, **{p[1]: set() for p in pairs}}
    for c1, c2 in pairs:
        connections[c1].add(c2)
        connections[c2].add(c1)


    lan_3 = set()
    for x, xs in connections.items():
        for y in xs:
            for z in connections[y]:
                if z in xs:
                    lan_3.add(set_str({x, y, z}))

    print('------ lan_3')
    lan_3 = list(lan_3)
    lan_3.sort()
    for xs in lan_3:
        print(f'{xs}')
    print(f'part1: {len([l for l in lan_3 if "-t" in l or l.startswith("t")])}')

    # lines = read_input('input-a.txt')

# tc	{'kh', 'td', 'tc', 'co', 'wh'}
# kh	{'qp', 'ta', 'kh', 'tc', 'ub'}
# td	{'qp', 'yn', 'td', 'tc', 'wh'}
# co	{'de', 'ka', 'ta', 'tc', 'co'}
# wh	{'qp', 'yn', 'td', 'tc', 'wh'}
# 
# tc,td,wh
