from unittest import TestCase

from d05 import read_start, move


class Test(TestCase):
    def test_read_start(self):
        given = '''    [D]
[N] [C]
[Z] [M] [P]
 1   2   3'''

        got = read_start(given)

        self.assertEqual(3, len(got))
        self.assertListEqual(['Z', 'N'], got[0])
        self.assertListEqual(['M', 'C', 'D'], got[1])
        self.assertListEqual(['P'], got[2])

    def test_move(self):
        w = [['Z', 'N'], ['M', 'C', 'D'], ['P']]
        move(w, 2, 2, 1)

        expected = [['Z', 'N', 'C', 'D'], ['M'], ['P']]

        self.assertListEqual(expected[0], w[0])
        self.assertListEqual(expected[1], w[1])
        self.assertListEqual(expected[2], w[2])
