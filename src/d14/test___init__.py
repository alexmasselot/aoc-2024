from unittest import TestCase

from d14 import read_path, path_points


class Test(TestCase):
    def test_read_path(self):
        given = '498,4 -> 498,6 -> 496,6'

        got = read_path(given)

        self.assertListEqual([(498, 4), (498, 6), (496, 6)], got)

    def test_path_points(self):
        path = [(498, 4), (498, 6), (496, 6)]
        got = path_points(path)

        expected = {(498, 4), (498, 5), (498, 6), (497, 6), (496, 6)}
        self.assertEqual(expected, got)

    def test_path_points_2(self):
        path = [(503, 4), (502, 4), (502, 6)]
        got = path_points(path)

        expected = {(503, 4), (502, 4), (502, 5), (502, 6)}
        self.assertEqual(expected, got)
