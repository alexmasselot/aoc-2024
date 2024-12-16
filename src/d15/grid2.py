from d15 import Grid


class Grid2(Grid):

    def __init__(self, input: str):
        super().__init__(input)
        self.grid = [list(l) for l in input.strip().split('\n')]
        self.bot = [(r, c)
                    for r, c in enumerate([l.strip().find('@') for l in input.strip().split('\n')]) if c >= 0][0]
        self.set(self.bot, '.')

    def is_box_in(self, p: tuple[int], dir: int):
        p = self.neigh_pos(p, dir)
        return self.get(p) == '[' or self.get(p) == ']'

    def can_move(self, dir: int):
        if self.is_wall_in(self.bot, dir):
            return False, set()
        if self.is_free_in(self.bot, dir):
            return True, set()

        def move_list(p: tuple[int, int], dir: int, acc: set[int]) -> tuple[bool, set[int]]:
            v = self.get(p)

            if self.is_free_in(p, dir):
                return True, acc
            if self.is_wall_in(p, dir):
                return False, set()

            if dir == 1 or dir == 3:
                if self.is_wall_in(p, dir, 2):
                    return False, set()
                if self.is_free_in(p, dir, 2):
                    return True, acc | {p, self.neigh_pos(p, dir)}
                return move_list(self.neigh_pos(p, dir, 2), dir, acc | {self.neigh_pos(p, dir), self.neigh_pos(p, dir, 2)})
            elif dir % 2 == 0:
                p_n = self.neigh_pos(p, dir)
                p_ox = p_n[1] + 1 if self.get(p_n) == '[' else p_n[1] - 1
                c_1, px_1 = move_list(p_n, dir, acc | {p_n})
                c_2, px_2 = move_list((p_n[0], p_ox), dir, acc | {(p_n[0], p_ox)})
                if p != self.bot:
                    return c_1 and c_2, px_1 | px_2 | {p}
                else:
                    return c_1 and c_2, px_1 | px_2

            else:  # dir == 2
                pass

        return move_list(self.bot, dir, set())

    def move(self, dir: int):
        can_move, ms = self.can_move(dir)
        if not can_move:
            return
        new_els = [(self.neigh_pos(p, dir), self.get(p)) for p in ms]
        for p in ms:
            self.set(p, '.')
        for p, v in new_els:
            self.set(p, v)
        self.bot = self.neigh_pos(self.bot, dir)

    def coords_sum(self):
        tot = 0
        for r, row in enumerate(self.grid):
            for c, v in enumerate(row):
                if v == '[':
                    tot += 100 * r + c
        return tot


def build_grid2(input: str):
    return Grid2(input.replace('#', '##').replace('.', '..').replace('@', '@.').replace('O', '[]'))
