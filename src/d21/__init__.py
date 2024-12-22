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

class Keypad():
    grid: list[list[int]]

    def __init__(self, layout: str):
        self.grid = [list(l) for l in layout.split('\n')]

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


def build_path(kp_input_str):
    sub_path = {}
    for r_a, line_a in enumerate(kp_input_str.split('\n')):
        for c_a, a in enumerate(line_a):
            if a == ' ':
                continue
            sub_path[a] = {a: 'A'}
            for r_b, line_b in enumerate(kp_input_str.split('\n')):
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
                    sub_path[a][b] = p + 'A'
    return sub_path


def command(cs, keypad) -> str:
    ret = ''
    for a, b in zip('A' + cs, cs):
        ret += keypad[a][b]
    return ret


def build_numeric_keypad():
    txt = LAYOUT_NUMERIC
    return build_path(txt)


def build_arrow_keypad():
    txt = LAYOUT_ARROW
    return build_path(txt)


def command_rec(target: str, level: int = 3):
    l1 = command(target, numeric_keypad_path)
    if level == 1:
        return l1
    l2 = command(l1, arrow_keypad_path)
    if level == 2:
        return l2
    return command(l2, arrow_keypad_path)


numeric_keypad_path = build_numeric_keypad()
numeric_keypad = Keypad(LAYOUT_NUMERIC)
arrow_keypad_path = build_arrow_keypad()
arrow_keypad = Keypad(LAYOUT_ARROW)

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
