from unittest import TestCase

from parameterized import parameterized

from d15 import read_line, sensor_beacon_y_coverage, interval_union


class Test(TestCase):
    def test_read_line(self):
        given = 'Sensor at x=2, y=18: closest beacon is at x=-2, y=15'

        got = read_line(given)

        self.assertEqual(((2, 18), (-2, 15)), got)

    @parameterized.expand([
        [12, (4, 12)],
        [-2, (8, 8)],
        [16, (8, 8)],
        [-3, None],
        [17, None],
    ])
    def test_sensor_beacon_y_coverage(self, given_y, expected):
        given_sb = ((8, 7), (2, 10))

        got = sensor_beacon_y_coverage(given_sb, given_y)

        self.assertEqual(expected, got)

    def test_interval_union_none(self):
        got = interval_union([])

        self.assertListEqual([], got)

    def test_interval_union_disjoint(self):
        got = interval_union([(1, 5), (7, 10)])

        self.assertListEqual([(1, 5), (7, 10)], got)

    def test_interval_union_intersect(self):
        got = interval_union([(1, 8), (7, 10)])

        self.assertListEqual([(1, 10)], got)
