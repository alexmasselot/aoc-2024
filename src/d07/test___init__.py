from unittest import TestCase

from d07 import is_operable_2


class Test(TestCase):
    def test_is_operable_2_a(self):
        target = 7290
        xs = [6, 8, 6, 15]

        got = is_operable_2(target, 0, xs)

        self.assertTrue(got)
