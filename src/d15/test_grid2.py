from unittest import TestCase

from d15.grid2 import Grid2, build_grid2

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


class TestGrid2(TestCase):
    def setUp(self):
        self.grid = build_grid2(sample_0_grid)

    def test_constructor(self):
        self.assertEqual((8, 16), self.grid.dim())
        self.assertEqual((2, 4), self.grid.bot)

    def test_is_free_t(self):
        self.assertTrue(self.grid.is_free_in((2, 2), 0))

    def test_is_free_f(self):
        self.assertFalse(self.grid.is_free_in((2, 2), 3))

    def test_move_0_free(self):
        grid = Grid2('''
######
#....#
#....#
#.@..#
#....#
######
''')

        self.assertEqual((True, set()), grid.can_move(1))

    def test_move_3_wall(self):
        grid = Grid2('''
######
#....#
#....#
#@...#
#....#
######
''')
        self.assertEqual((False, set()), grid.can_move(3))

    def test_move_1_push_one(self):
        grid = Grid2('''
######
#....#
#....#
#@[].#
#....#
######
''')
        self.assertEqual((True, {(3, 2), (3, 3)}), grid.can_move(1))

    def test_move_1_push_two(self):
        grid = Grid2('''
########
#......#
#......#
#@[][].#
#......#
########
''')
        self.assertEqual((True, {(3, 2), (3, 3), (3, 4), (3, 5)}), grid.can_move(1))

    def test_move_1_push_blocked(self):
        grid = Grid2('''
#########
#.......#
#.......#
#@[][][]#
#.......#
#########
''')
        self.assertEqual((False, set()), grid.can_move(1))

    def test_move_3_push_one(self):
        grid = Grid2('''
######
#....#
#....#
#.[]@#
#....#
######
''')
        self.assertEqual((True, {(3, 3), (3, 2)}), grid.can_move(3))

    def test_move_3_push_two(self):
        grid = Grid2('''
########
#......#
#......#
#.[][]@#
#......#
########
''')
        self.assertEqual((True, {(3, 5), (3, 4), (3, 3), (3, 2)}), grid.can_move(3))

    def test_move_3_push_blocked(self):
        grid = Grid2('''
#########
#.......#
#.......#
#[][][]@#
#.......#
#########
''')
        self.assertEqual((False, set()), grid.can_move(3))

    def test_move_0_push_one_left(self):
        grid = Grid2('''
######
#....#
#....#
#.[].#
#.@..#
######
''')
        self.assertEqual((True, {(3, 3), (3, 2)}), grid.can_move(0))

    def test_move_0_push_one_right(self):
        grid = Grid2('''
######
#....#
#....#
#.[].#
#..@.#
######
''')
        self.assertEqual((True, {(3, 3), (3, 2)}), grid.can_move(0))

    def test_move_0_push_two_a(self):
        grid = Grid2('''
######
#....#
#.[].#
#.[].#
#.@..#
######
''')
        self.assertEqual((True, {(3, 3), (3, 2), (2, 2), (2, 3)}), grid.can_move(0))

    def test_move_0_push_two_b(self):
        grid = Grid2('''
######
#....#
#[]..#
#.[].#
#.@..#
######
    ''')
        print(grid)
        self.assertEqual((True, {(3, 3), (3, 2), (2, 2), (2, 1)}), grid.can_move(0))

    def test_move_0_push_two_c(self):
        grid = Grid2('''
######
#.[].#
#[]..#
#.[].#
#.@..#
######
    ''')
        print(grid)
        self.assertFalse(False, grid.can_move(0)[0])
    def test_move_0_push_two_d(self):
        grid = Grid2('''
######
#....#
#[][]#
#.[].#
#.@..#
######
    ''')
        print(grid)
        self.assertEqual((True, {(3, 3), (3, 2), (2, 1), (2, 2), (2, 3), (2, 4)}), grid.can_move(0))

    def test_move_0_push_two_e(self):
        grid = Grid2('''
######
#....#
#[][]#
#.[]@#
#....#
######
    ''')
        self.assertEqual((True, {(2, 3), (2, 4)}), grid.can_move(0))

    def test_move_0(self):
        grid = Grid2('''
######
#....#
#[][]#
#.[]@#
#....#
######
    ''')
        grid.move(0)
        expected = Grid2('''
######
#..[]#
#[].@#
#.[].#
#....#
######
    ''')

        self.assertEqual(expected, grid)

