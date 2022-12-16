from unittest import TestCase

from parameterized import parameterized
from itertools import zip_longest

from d13 import in_order


class Test(TestCase):
    def test_pouet(self):
        xs = [4, 5, 6]
        ys = [1, 2]
        print(list(zip_longest(xs, ys, fillvalue=None)))

    @parameterized.expand([
        [[1, 1, 3, 1, 1], [1, 1, 5, 1, 1]],
        [[[1], [2, 3, 4]], [[1], 4]],
        [[[4, 4], 4, 4], [[4, 4], 4, 4, 4]],
        [[], [3]],
    ])
    def test_in_order_true(self, xs, ys):
        self.assertTrue(in_order(xs, ys))

    @parameterized.expand([
        [[9], [[8, 7, 6]]],
        [[7, 7, 7, 7], [7, 7, 7]],
        [[3], []],
        [[[1], [6, 3, 4]], [[1], 4]],
        [[[]], [[]]],
        [[1, [2, [3, [4, [5, 6, 7]]]], 8, 9], [1, [2, [3, [4, [5, 6, 0]]]], 8, 9]],

    ])
    def test_in_order_false(self, xs, ys):
        self.assertFalse(in_order(xs, ys))
