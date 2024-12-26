from itertools import chain

from utils import read_input, find_in_matrix

LAYOUT_NUMERIC = '789\n456\n123\n 0A'
LAYOUT_ARROW = ' ^A\n<v>'


# +---+---+---+
# | 7 | 8 | 9 |
# +---+---+---+
# | 4 | 5 | 6 |
# +---+---+---+
# | 1 | 2 | 3 |
# +---+---+---+
#     | 0 | A |
#     +---+---+

#     +---+---+
#     | ^ | A |
# +---+---+---+
# | < | v | > |
# +---+---+---+

class Keypad:
    grid: list[list[str]]
    is_numeric: bool
    sub_paths: dict[str, dict[str, list[str]]]

    def __init__(self, layout: str, is_numeric: bool):
        self.grid = [list(l) for l in layout.split('\n')]
        self.is_numeric = is_numeric
        self.build_paths()

    def build_paths(self):
        """
        for two keys a and b on the keyboard, build the list of possible paths to go from one to the other.
        Do not go through the empty position.
        just make L paths, as staircase patterns wil only be longer.
        :return:
        """
        sub_paths = {}
        for r_a, line_a in enumerate(self.grid):
            for c_a, a in enumerate(line_a):
                if a == ' ':
                    continue
                sub_paths[a] = {a: ['A']}
                for r_b, line_b in enumerate(self.grid):
                    for c_b, b in enumerate(line_b):
                        if b == ' ':
                            continue
                        sub_paths[a][b] = []
                        d_r = r_b - r_a
                        d_c = c_b - c_a
                        # no move
                        if d_r == 0 and d_c == 0:
                            sub_paths[a][b].append('A')
                            continue
                        # v
                        if d_r > 0 and d_c == 0:
                            sub_paths[a][b].append('v' * d_r + 'A')
                            continue
                        # ^
                        if d_r < 0 and d_c == 0:
                            sub_paths[a][b].append('^' * -d_r + 'A')
                            continue
                        # >
                        if d_r == 0 and d_c > 0:
                            sub_paths[a][b].append('>' * d_c + 'A')
                            continue
                        # <
                        if d_r == 0 and d_c < 0:
                            sub_paths[a][b].append('<' * -d_c + 'A')
                            continue

                        # >v or v>
                        if d_r > 0 and d_c > 0:  # >v + v>
                            sub_paths[a][b].append('>' * d_c + 'v' * d_r + 'A')
                            if not self.is_numeric or not (r_b == 3 and c_a == 0):
                                sub_paths[a][b].append('v' * d_r + '>' * d_c + 'A')

                        if d_r < 0 and d_c < 0:  # ^< + ^<
                            sub_paths[a][b].append('^' * -d_r + '<' * -d_c + 'A')
                            if not self.is_numeric or not (r_a == 3 and c_b == 0):
                                sub_paths[a][b].append('<' * -d_c + '^' * -d_r + 'A')

                        if d_r >= 0 > d_c:  # v< + <v
                            sub_paths[a][b].append('v' * d_r + '<' * (-d_c) + 'A')
                            if self.is_numeric or not (r_a == 0 and c_b == 0):
                                sub_paths[a][b].append('<' * (-d_c) + 'v' * d_r + 'A')

                        if d_r < 0 < d_c:  # >^ + ^>
                            sub_paths[a][b].append('>' * d_c + '^' * (-d_r) + 'A')
                            if self.is_numeric or not (r_b == 0 and c_a == 0):
                                sub_paths[a][b].append('^' * (-d_r) + '>' * d_c + 'A')
        self.sub_paths = sub_paths

    def type(self, start: str, seq: str):
        move = {
            '<': (0, -1),
            '>': (0, 1),
            'v': (1, 0),
            '^': (-1, 0),
        }
        p = find_in_matrix(self.grid, start)
        ret = ''
        for m in list(seq):
            if m == 'A':
                ret += self.grid[p[0]][p[1]]
                continue
            p = (p[0] + move[m][0], p[1] + move[m][1])
            if self.is_numeric and p[0] == 3 and p[1] == 0:
                raise 'Numeric: cannot go through (3,0)'
            if not self.is_numeric and p[0] == 0 and p[1] == 0:
                raise 'Arrow: cannot go through (0,0)'
        return ret


def command(cs, keypad) -> list[str]:
    def fhandler(acc: str, rem: list[tuple[str, str]]) -> list[str]:
        if not rem:
            return [acc]
        a, b = rem[0]
        r = list(chain(*[fhandler(acc + p, rem[1:]) for p in keypad.sub_paths[a][b]]))
        return r

    steps = list(zip(cs, cs[1:]))
    return fhandler('', steps)


def command_rec(target: str, level: int = 3):
    l1 = command(target, numeric_keypad)
    if level == 1:
        return l1
    l2 = list(chain(*[command('A' + l, arrow_keypad) for l in l1]))
    if level == 2:
        return l2
    l3 = list(chain(*[command('A' + l, arrow_keypad) for l in l2]))
    return l3

def shortest_arrow_seq(target: str, level:int):
    def fhandler(ts: str, level:int):
        if level ==0:
            return len(ts)
        next_seqs = command('A' + ts, arrow_keypad)
        return min(shortest_arrow_seq(s, level -1) for s in next_seqs)
    return fhandler(target, level)

def shortest_seq(target: str, level:int):
    numeric_seq = command('A' + target, numeric_keypad)
    ml = min(shortest_arrow_seq(t,level) for t in numeric_seq)
    return ml


numeric_keypad = Keypad(LAYOUT_NUMERIC, True)
arrow_keypad = Keypad(LAYOUT_ARROW, False)

if __name__ == '__main__':

    # <A^A>^^AvvvA, <A^A^>^AvvvA, and <A^A^^>AvvvA.
    tot_1 = 0
    for line in read_input('input.txt'):
        print(f'----------------------------')

        ml = shortest_seq(line, 2)
        print(f'''{line}: {ml} {int(line.replace('A', ''))}''')
        tot_1 += ml * int(line.replace('A', ''))

    print(tot_1)

    # lines = read_input('input-a.txt')
# <v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A
# v<<A^>>Av<A<A^>>AA<A>vAA^Av<<A^>>AAvA^Av<A^>AA<A>Av<A<A^>>AAA<A>vA^A
