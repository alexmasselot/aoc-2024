from unittest import TestCase

from parameterized import parameterized

from d09 import tail_new_pos, next_move_stack


class Test(TestCase):
    @parameterized.expand([
        # same pos
        [(5, 3), (5, 3)],
        # contact straight
        [(5, 2), (5, 2)],
        [(5, 4), (5, 4)],
        [(4, 3), (4, 3)],
        [(6, 3), (6, 3)],
        # contact diag
        [(4, 2), (4, 2)],
        [(6, 4), (6, 4)],
        # straight distance 2
        [(3, 3), (4, 3)],
        [(7, 3), (6, 3)],
        [(5, 1), (5, 2)],
        [(5, 5), (5, 4)],
        # horse move (2,1)
        [(7, 2), (6, 3)],
        [(7, 4), (6, 3)],
        [(4, 1), (5, 2)],
        [(6, 1), (5, 2)],
        [(4, 5), (5, 4)],
        [(6, 5), (5, 4)],
    ])
    def test_tail_new_pos(self, given_tail, expected):
        head = (5, 3)
        got = tail_new_pos(given_tail, head)

        self.assertEqual(expected, got)

    @parameterized.expand([
        ([('R', 4), ('L', 2), ('U', 4)], 'R', [('R', 3), ('L', 2), ('U', 4)]),
        ([('R', 1), ('L', 2), ('U', 4)], 'R', [('L', 2), ('U', 4)]),
        ([('R', 1)], 'R', []),
        ([], None, []),

    ])
    def test_next_move_stack(self, given, expected_dir, expected_stack):
        got_dir, got_stack = next_move_stack(given)

        self.assertEqual(expected_dir, got_dir)
        self.assertListEqual(expected_stack, got_stack)
