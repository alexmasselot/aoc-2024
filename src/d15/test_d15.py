from unittest import TestCase

from d15 import Grid

sample_0_grid = '''
########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########
'''


class TestGrid(TestCase):
    def setUp(self):
        self.grid = Grid(sample_0_grid)

    def test_constructor(self):
        self.assertEqual(8, self.grid.size())
        self.assertEqual((2, 2), self.grid.bot)

    def test_str(self):
        got = str(self.grid)
        self.assertEqual(sample_0_grid.strip(), got)

    def test_neigh_pos_0(self):
        self.assertEqual((1, 2), self.grid.neigh_pos((2, 2), 0))

    def test_neigh_pos_1(self):
        self.assertEqual((2, 3), self.grid.neigh_pos((2, 2), 1))

    def test_neigh_pos_2(self):
        self.assertEqual((3, 2), self.grid.neigh_pos((2, 2), 2))

    def test_neigh_pos_3(self):
        self.assertEqual((2, 1), self.grid.neigh_pos((2, 2), 3))

    def test_is_free_t(self):
        self.assertTrue(self.grid.is_free((2, 2), 0))

    def test_is_free_f(self):
        self.assertFalse(self.grid.is_free((2, 2), 3))

    def test_move_0_free(self):
        grid = Grid('''
######
#....#
#....#
#.@..#
#....#
######
''')
        grid.move(0)
        expected = Grid('''
######
#....#
#.@..#
#....#
#....#
######
''')
        self.assertEqual(expected, grid)

    def test_move_3_wall(self):
        grid = Grid('''
######
#....#
#....#
#@...#
#....#
######
''')
        grid.move(3)
        expected = Grid('''
######
#....#
#....#
#@...#
#....#
######
''')
        self.assertEqual(expected, grid)


    def test_move_push_one(self):
        grid = Grid('''
######
#....#
#....#
#@O..#
#....#
######
''')
        grid.move(1)
        expected = Grid('''
######
#....#
#....#
#.@O.#
#....#
######
''')
        self.assertEqual(expected, grid)

    def test_move_push_one_b(self):
        grid = Grid('''
######
#....#
#....#
#@O.O#
#....#
######
''')
        grid.move(1)
        expected = Grid('''
######
#....#
#....#
#.@OO#
#....#
######
''')
        self.assertEqual(expected, grid)

    def test_move_push_two(self):
        grid = Grid('''
######
#....#
#....#
#@OO.#
#....#
######
''')
        grid.move(1)
        expected = Grid('''
######
#....#
#....#
#.@OO#
#....#
######
''')
        self.assertEqual(expected, grid)
    def test_move_push_blocked(self):
        grid = Grid('''
######
#....#
#....#
#@OOO#
#....#
######
''')
        grid.move(1)
        expected = Grid('''
######
#....#
#....#
#@OOO#
#....#
######
''')
        self.assertEqual(expected, grid)
