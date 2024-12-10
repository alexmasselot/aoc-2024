from unittest import TestCase

from d02 import check_increase, check_decrease


class Test(TestCase):
    def test_check_increase_1(self):
        given = [50, 51, 51, 52, 54]
        self.assertTrue(check_increase(given, 1))

    def test_check_increase_1_start(self):
        given = [51, 50, 51, 52, 54]
        self.assertTrue(check_increase(given, 1))

    def test_check_decrease_0(self):
        given = [60, 59, 57, 55, 52, 48, 51]
        self.assertFalse(check_decrease(given, 0))

    def test_check_decrease_last(self):
        given = [60, 59, 57, 55, 52, 48, 51]
        self.assertTrue(check_decrease(given, 1))

    def test_check_increase_second(self):
        given = [51, 48, 52, 55, 57, 59, 60]
        self.assertTrue(check_increase(given, 1))
