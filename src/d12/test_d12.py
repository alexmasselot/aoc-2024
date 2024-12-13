from unittest import TestCase

from d12 import tag_grid, price_2


class Test(TestCase):

    def get_grid(self, block: str):
        lines = [l.strip() for l in block.strip().split('\n')]
        grid = [list(l) for l in lines]
        n = len(grid)
        tag_grid(grid, n)
        return grid

    def test_price_2_ABCD(self):
        given = '''AAAA
BBCD
BBCC
EEEC'''
        grid = self.get_grid(given)
        n = len(grid)

        got = price_2(grid, n)
        self.assertEqual(80, got)

    def test_price_2_E(self):
        given = '''EEEEE
EXXXX
EEEEE
EXXXX
EEEEE'''
        grid = self.get_grid(given)
        n = len(grid)

        got = price_2(grid, n)
        self.assertEqual(236, got)

    def test_price_2_XO(self):
        given = '''OOOOO
OXOXO
OOOOO
OXOXO
OOOOO'''
        grid = self.get_grid(given)
        n = len(grid)

        got = price_2(grid, n)
        self.assertEqual(436, got)

    def test_price_2_ABBA(self):
        given = '''
AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA'''
        grid = self.get_grid(given)
        n = len(grid)

        got = price_2(grid, n)
        self.assertEqual(368, got)

    def test_price_large(self):
        given = '''
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
'''
        grid = self.get_grid(given)
        n = len(grid)

        got = price_2(grid, n)
        expected = 1206
        self.assertEqual(expected, got)

    def test_price_2_L(self):
        given = '''
L.
LL
'''
        grid = self.get_grid(given)
        n = len(grid)

        got = price_2(grid, n)
        expected = 1 * 4 + 3 * 6
        self.assertEqual(expected, got)

    def test_price_nico_0(self):
        given = '''
X.
.X
'''
        grid = self.get_grid(given)
        n = len(grid)

        got = price_2(grid, n)
        expected = 4 * 1 * 4
        self.assertEqual(expected, got)

    def test_price_nico(self):
        given = '''
....
.X..
..X.
....
'''
        grid = self.get_grid(given)
        n = len(grid)

        got = price_2(grid, n)
        expected = 1 * 4 + 1 * 4 + 14 * (6 + 6)
        self.assertEqual(expected, got)
