from unittest import TestCase

from d25 import read_key_lock


class Test(TestCase):
    def test_read_key_lock_1(self):
        input = '''
#####
.####
.####
.####
.#.#.
.#...
.....
'''.strip()

        got_is_lock, got_values = read_key_lock(input)
        self.assertTrue(got_is_lock)
        self.assertEqual([0, 5, 3, 4, 3], got_values)

    def test_read_key_lock_2(self):
        input = '''
.....
#....
#....
#...#
#.#.#
#.###
#####
'''.strip()

        got_is_lock, got_values = read_key_lock(input)
        self.assertFalse(got_is_lock)
        self.assertEqual([5, 0, 2, 1, 3], got_values)
