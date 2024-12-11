from unittest import TestCase

from d09 import map_disk, checksum, pop_mem, checksum_2


class Test(TestCase):
    def test_map_disk(self):
        got = map_disk('12345')

        self.assertEqual([(0, 0, 1), (1, 3, 3), (2, 10, 5)], got)

    def test_checksum_simple(self):
        mem = [(0, 0, 1), (1, 3, 3), (2, 10, 5)]
        got = checksum(mem)

        expected = 0
        for i, c in enumerate('022111222'):
            expected+=i*int(c)

        self.assertEqual(expected, got)

    def test_checksum_example(self):
        got = checksum(map_disk('2333133121414131402'))

        self.assertEqual(1928, got)

    def test_checksum_2_example(self):
        got = checksum_2(map_disk('2333133121414131402'))

        self.assertEqual(2858, got)