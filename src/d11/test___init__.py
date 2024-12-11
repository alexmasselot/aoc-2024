from unittest import TestCase

from d11 import blink_stone


class Test(TestCase):
    def test_blink_rule_1(self):
        self.assertEqual([1], blink_stone(0))

    def test_blink_rule_2(self):
        self.assertEqual([17, 43], blink_stone(1743))

    def test_blink_rule_2_b(self):
        self.assertEqual([1, 7], blink_stone(17))

    def test_blink_rule_2_0(self):
        self.assertEqual([17, 3], blink_stone(1703))

    def test_blink_rule_3(self):
        self.assertEqual([111*2024], blink_stone(111))

