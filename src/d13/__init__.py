import re

from utils import read_input, read_input_blocks


class Machine():
    a_x: int
    a_y: int
    b_x: int
    b_y: int

    p_x: int
    p_y: int

    def __init__(self, text: str, shift=0):
        rx = r'''Button A: X\+([0-9]+), Y\+([0-9]+)
Button B: X\+([0-9]+), Y\+([0-9]+)
Prize: X=([0-9]+), Y=([0-9]+)'''
        m = re.match(rx, text)
        self.a_x = int(m.group(1))
        self.a_y = int(m.group(2))
        self.b_x = int(m.group(3))
        self.b_y = int(m.group(4))
        self.p_x = int(m.group(5)) + shift
        self.p_y = int(m.group(6)) + shift

    def min_token_brutal(self):
        mt = None
        n_a = 0
        while n_a * self.a_x <= self.p_x and n_a * self.a_y <= self.p_y:
            tot_a_x = n_a * self.a_x
            tot_a_y = n_a * self.a_y
            n_b = 0
            while (tot_a_x + n_b * self.b_x < self.p_x) and (tot_a_y + n_b * self.b_y < self.p_y):
                n_b += 1
            if tot_a_x + n_b * self.b_x == self.p_x and tot_a_y + n_b * self.b_y == self.p_y:
                nb_tokens = 3 * n_a + n_b
                if mt is None or nb_tokens < mt:
                    mt = nb_tokens
            n_a += 1
        return mt

    def min_token(self):
        n_b = (self.p_x * self.a_y - self.p_y * self.a_x) / (self.a_y * self.b_x - self.a_x * self.b_y)
        if int(n_b) != n_b or n_b < 0:
            return None
        n_a = (self.p_x - n_b * self.b_x) / self.a_x
        if int(n_a) != n_a or n_a < 0:
            return None
        return int(3 * n_a + n_b)


if __name__ == '__main__':
    machines = [Machine(b) for b in read_input_blocks('input-a.txt')]
    tot_1 = 0
    for m in machines:
        t = m.min_token()
        if t is not None:
            tot_1 += t
    print(tot_1)

    machines = [Machine(b, shift=10000000000000) for b in read_input_blocks('input-a.txt')]
    tot_2 = 0
    for m in machines:
        t = m.min_token()
        if t is not None:
            tot_2 += t
    print(tot_2)
    # lines = read_input('input-a.txt')
