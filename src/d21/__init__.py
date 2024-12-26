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
    is_empty_bl: bool
    sub_paths: dict[str, dict[str, list[str]]]

    def __init__(self, layout: str, is_empty_bl: bool):
        self.grid = [list(l) for l in layout.split('\n')]
        self.is_empty_bl = is_empty_bl
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
                sub_paths[a] = {a: 'A'}
                for r_b, line_b in enumerate(self.grid):
                    for c_b, b in enumerate(line_b):
                        if b == ' ':
                            continue
                        d_r = r_b - r_a
                        d_c = c_b - c_a
                        if d_r >= 0 and d_c >= 0:  # >v
                            p = '>' * d_c + 'v' * d_r
                        if d_r >= 0 > d_c:  # v<
                            p = 'v' * d_r + '<' * (-d_c)
                        if d_r < 0 and d_c < 0:  # ^<
                            p = '^' * (-d_r) + '<' * (-d_c)
                        if d_r < 0 <= d_c:  # >^
                            p = '>' * d_c + '^' * (-d_r)
                        sub_paths[a][b] = p + 'A'
        self.sub_paths = sub_paths

    def type(self, seq: str):
        move = {
            '<': (0, -1),
            '>': (0, 1),
            'v': (1, 0),
            '^': (-1, 0),
        }
        p = find_in_matrix(self.grid, 'A')
        ret = ''
        for m in list(seq):
            if m == 'A':
                ret += self.grid[p[0]][p[1]]
                continue
            p = (p[0] + move[m][0], p[1] + move[m][1])
        return ret


def command(cs, keypad) -> str:
    ret = ''
    for a, b in zip('A' + cs, cs):
        ret += keypad.sub_paths[a][b]
    return ret



def command_rec(target: str, level: int = 3):
    l1 = command(target, numeric_keypad)
    if level == 1:
        return l1
    l2 = command(l1, arrow_keypad)
    if level == 2:
        return l2
    return command(l2, arrow_keypad)


numeric_keypad = Keypad(LAYOUT_NUMERIC, True)
arrow_keypad = Keypad(LAYOUT_ARROW, False)

if __name__ == '__main__':

    # <A^A>^^AvvvA, <A^A^>^AvvvA, and <A^A^^>AvvvA.
    tot_1 = 0
    for line in read_input('sample.txt'):
        print(f'----------------------------')
        l3 = command_rec(line, 3)
        print(f'''{line}: {len(l3)} {int(line.replace('A', ''))}''')
        tot_1 += len(l3) * int(line.replace('A', ''))

    print(tot_1)

    # lines = read_input('input-a.txt')
# <v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A
# v<<A^>>Av<A<A^>>AA<A>vAA^Av<<A^>>AAvA^Av<A^>AA<A>Av<A<A^>>AAA<A>vA^A
