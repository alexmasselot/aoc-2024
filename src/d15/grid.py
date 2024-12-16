class Grid:
    bot: tuple
    grid: list[list[str]]

    def __init__(self, input: str):
        self.grid = [list(l) for l in input.strip().split('\n')]
        self.bot = [(r, c)
                    for r, c in enumerate([l.find('@') for l in input.strip().split('\n')]) if c >= 0][0]
        self.set(self.bot, '.')

    def dim(self):
        return len(self.grid), len(self.grid[0])

    def get(self, p: tuple[int, int]):
        return self.grid[p[0]][p[1]]

    def set(self, p: tuple[int, int], v: str):
        self.grid[p[0]][p[1]] = v

    def neigh_pos(self, p: tuple[int], dir: int, dist: int = 1):
        if dir == 0:
            return p[0] - dist, p[1]
        elif dir == 1:
            return p[0], p[1] + dist
        elif dir == 2:
            return p[0] + dist, p[1]
        elif dir == 3:
            return p[0], p[1] - dist

    def is_free_in(self, p: tuple[int], dir: int, dist: int = 1):
        p = self.neigh_pos(p, dir, dist)
        return self.get(p) == '.'

    def is_box_in(self, p: tuple[int], dir: int, dist: int = 1):
        p = self.neigh_pos(p, dir, dist)
        return self.get(p) == 'O'

    def is_wall_in(self, p: tuple[int], dir: int, dist: int = 1):
        p = self.neigh_pos(p, dir, dist)
        return self.get(p) == '#'

    def move(self, dir: int):
        p_n = self.neigh_pos(self.bot, dir)
        if self.is_wall_in(self.bot, dir):
            return self
        if self.is_free_in(self.bot, dir):
            self.bot = p_n
            return self

        # we have a wall
        p = self.bot
        while self.is_box_in(p, dir):
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
        p_bot = (self.dim()[1] + 1) * self.bot[0] + self.bot[1]
        return buf[:p_bot] + '@' + buf[(p_bot + 1):]

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return str(self) == str(other)
