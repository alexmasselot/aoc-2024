from unittest import TestCase

from d17 import Computer, build_computer


class TestComputer(TestCase):
    def test_build_computer(self):
        given_reg = '''Register A: 729
Register B: 0
Register C: 1'''
        given_inst = 'Program: 3,4,5'
        c = build_computer(given_reg, given_inst)

        self.assertEqual([729, 0, 1], c.registers)
        self.assertEqual([3, 4, 5], c.instructions)

    def test_operate_1(self):
        c = Computer([0, 0, 9], [2, 6])

        got_i = c.operate(0)
        self.assertEqual(2, got_i)
        self.assertEqual([0, 1, 9], c.registers)
        self.assertEqual('', c.output())

    def test_operate_2(self):
        c = Computer([10, 0, 0], [5, 0, 5, 1, 5, 4])

        c.operate_all()
        self.assertEqual('0,1,2', c.output())

    def test_operate_3(self):
        c = Computer([2024, 0, 0], [0, 1, 5, 4, 3, 0])

        c.operate_all()
        self.assertEqual(0, c.registers[0])
        self.assertEqual('4,2,5,6,7,7,7,7,3,1,0', c.output())

    def test_operate_4(self):
        c = Computer([0, 29, 0], [1, 7])

        c.operate_all()
        self.assertEqual(26, c.registers[1])

    def test_operate_5(self):
        c = Computer([0, 2024, 43690], [4,0])

        c.operate_all()
        self.assertEqual(44354, c.registers[1])

    def test_sample(self):
        c = build_computer('''Register A: 729
Register B: 0
Register C: 0''', 'Program: 0,1,5,4,3,0')

        c.operate_all()
        self.assertEqual('4,6,3,5,6,3,5,2,1,0', c.output())