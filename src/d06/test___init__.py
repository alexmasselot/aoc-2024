from unittest import TestCase

from d06 import marker_1


class Test(TestCase):
    def test_marker_1_a(self):
        got = marker_1('mjqjpqmgbljsphdztnvjfqwrcgsmlb')

        self.assertEqual(7, got)

    def test_marker_1_b(self):
        got = marker_1('bvwbjplbgvbhsrlpgdmjqwftvncz')

        self.assertEqual(5, got)
