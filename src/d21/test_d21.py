from unittest import TestCase

from d21 import command_rec, numeric_keypad, arrow_keypad


class Test(TestCase):
    def test_command_rec_1_1(self):
        given = '029A'
        got = command_rec(given, 1)
        self.assertEqual('<A^A>^^AvvvA', got)

        got_back = numeric_keypad.type(got)
        self.assertEqual(given, got_back)


    def test_command_rec_1_2(self):
        given = '029A'

        got = command_rec(given, 2)
        self.assertEqual('v<<A>>^A<A>AvA<^AA>A<vAAA>^A', got)

        got_back = numeric_keypad.type(arrow_keypad.type(got))
        self.assertEqual(given, got_back)

    def test_command_rec_1_3(self):
        given = '029A'
        got = command_rec(given, 3)
        # self.assertEqual('<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A', got)

        got_back = numeric_keypad.type(arrow_keypad.type(arrow_keypad.type(got)))
        self.assertEqual(given, got_back)

    def test_command_rec_4_3(self):
        given = '379A'
        print(command_rec(given, 1))
        print(command_rec(given, 2))
        print(command_rec(given, 3))
        got = command_rec(given, 3)
        self.assertEqual('<v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A', got)

        got_back = numeric_keypad.type(arrow_keypad.type(arrow_keypad.type(got)))
        self.assertEqual(given, got_back)
