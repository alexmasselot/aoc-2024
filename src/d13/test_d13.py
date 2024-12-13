from unittest import TestCase

from d13 import Machine


class TestMachine(TestCase):
    def test_constructor(self):
        given = '''Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400'''

        got = Machine(given)
        self.assertEqual(94, got.a_x)
        self.assertEqual(34, got.a_y)
        self.assertEqual(22, got.b_x)
        self.assertEqual(67, got.b_y)
        self.assertEqual(8400, got.p_x)
        self.assertEqual(5400, got.p_y)

    def test_min_token_1(self):
        got = Machine('''Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400''')

        self.assertEqual(280, got.min_token())
    def test_min_token_2(self):
        got = Machine('''Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176''')

        self.assertEqual(None, got.min_token())
    def test_min_token_3(self):
        got = Machine('''Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450''')

        self.assertEqual(200, got.min_token())
    def test_min_token_4(self):
        got = Machine('''Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279''')

        self.assertEqual(None, got.min_token())
