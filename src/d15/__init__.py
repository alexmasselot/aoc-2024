from utils import read_input_blocks


class Grid:
    bot: tuple
    grid: list[list[str]]

    def __init__(self, input: str):
        self.grid = [list(l) for l in input.strip().split('\n')]
        self.bot = [(r, c)
                    for r, c in enumerate([l.find('@') for l in input.strip().split('\n')]) if c >= 0][0]
        self.set(self.bot, '.')

    def size(self):
        return len(self.grid)

    def get(self, p: tuple[int, int]):
        return self.grid[p[0]][p[1]]

    def set(self, p: tuple[int, int], v: str):
        self.grid[p[0]][p[1]] = v

    def neigh_pos(self, p: tuple[int], dir: int):
        if dir == 0:
            return p[0] - 1, p[1]
        elif dir == 1:
            return p[0], p[1] + 1
        elif dir == 2:
            return p[0] + 1, p[1]
        elif dir == 3:
            return p[0], p[1] - 1

    def is_free(self, p: tuple[int], dir: int):
        p = self.neigh_pos(p, dir)
        return self.get(p) == '.'

    def is_box(self, p: tuple[int], dir: int):
        p = self.neigh_pos(p, dir)
        return self.get(p) == 'O'

    def is_wall(self, p: tuple[int], dir: int):
        p = self.neigh_pos(p, dir)
        return self.get(p) == '#'

    def move(self, dir: int):
        p_n = self.neigh_pos(self.bot, dir)
        if self.is_wall(self.bot, dir):
            return self
        if self.is_free(self.bot, dir):
            self.bot = p_n
            return self

        # we have a wall
        p = self.bot
        while self.is_box(p, dir):
            p = self.neigh_pos(p, dir)
        p1 = self.neigh_pos(p, dir)
        if self.get(p1) == '.':
            # we can push all boxes
            self.set(p1, 'O')
            self.set(p_n, '.')
            self.bot = p_n

        return self

    def coords_sum(self):
        tot = 0
        for r, row in enumerate(self.grid):
            for c, v in enumerate(row):
                if v == 'O':
                    tot += 100 * r + c
        return tot

    def __str__(self):
        buf = '\n'.join([''.join(row) for row in self.grid])
        p_bot = (self.size() + 1) * self.bot[0] + self.bot[1]
        return buf[:p_bot] + '@' + buf[(p_bot + 1):]

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return str(self) == str(other)


c_dir = {
    '^': 0,
    '>': 1,
    'v': 2,
    '<': 3,
}


def read_move_sequence(input: str):
    return [c_dir[c] for c in input.replace('\n', '')]


if __name__ == '__main__':
    blocks = read_input_blocks('input.txt')

    grid = Grid(blocks[0])
    move_sequence = read_move_sequence(blocks[1])

    for move in move_sequence:
        grid.move(move)
        # print(move)
        # print(grid)
        # print('\n\n')

    print(grid.coords_sum())
    # lines = read_input('input-a.txt')
