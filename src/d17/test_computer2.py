from unittest import TestCase

from d17.computer2 import Computer2, build_computer2


class TestComputer(TestCase):
    def test_build_computer(self):
        given_reg = '''Register A: 729
Register B: 0
Register C: 1'''
        given_inst = 'Program: 3,4,5'
        c, r = build_computer2(given_reg, given_inst)

        self.assertEqual([729, 0, 1], r)
        self.assertEqual([3, 4, 5], c.instructions)

    def test_operate_1(self):
        c = Computer2([2, 6])
        r = [0, 0, 9]

        got_i, got_r, got_o = c.operate(0, r)
        self.assertEqual(2, got_i)
        print(r)
        print(got_r)
        self.assertEqual([0, 1, 9], got_r)
        self.assertEqual(None, got_o)

    def test_operate_2(self):
        c = Computer2([5, 0, 5, 1, 5, 4])
        r = [10, 0, 0]

        got_o = c.operate_all(r)
        self.assertEqual('0,1,2', got_o)

    def test_operate_3(self):
        c = Computer2([0, 1, 5, 4, 3, 0])
        r = [2024, 0, 0]

        got_o = c.operate_all(r)
        self.assertEqual('4,2,5,6,7,7,7,7,3,1,0', got_o)

    def test_sample(self):
        c,r = build_computer2('''Register A: 729
Register B: 0
Register C: 0''', 'Program: 0,1,5,4,3,0')

        got_o = c.operate_all(r)
        self.assertEqual('4,6,3,5,6,3,5,2,1,0', got_o)
