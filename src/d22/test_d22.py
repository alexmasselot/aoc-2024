from unittest import TestCase

from d22 import next_secret, loop_secret


class Test(TestCase):
    def test_next_1(self):
        self.assertEqual(15887950, next_secret(123))

    def test_next_2(self):
        self.assertEqual(16495136, next_secret(15887950))

    def test_loop(self):
        self.assertEqual(8685429, loop_secret(1, 2000))
