from unittest import TestCase

from parameterized import parameterized

from d02 import score


class Test(TestCase):
    @parameterized.expand([
        ['B', 'A'],
        ['C', 'B'],
        ['A', 'C'],
    ])
    def test_score_lose(self, a, b):
        got = score(a, b)

        self.assertEqual(0, got)

    @parameterized.expand([
        ['A', 'B'],
        ['B', 'C'],
        ['C', 'A'],
    ])
    def test_score_win(self, a, b):
        got = score(a, b)

        self.assertEqual(6, got)

    def test_raw(self):
        got = score('B', 'B')

        self.assertEqual(3, got)
