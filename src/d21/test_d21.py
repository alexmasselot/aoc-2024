from unittest import TestCase

from parameterized import parameterized

from d21 import command_rec, numeric_keypad, arrow_keypad, command, shortest_seq


class Test(TestCase):
    @parameterized.expand([
        ("AA", ['A']),
        ("A0", ['<A']),
        ("0A", ['>A']),
        ("A3", ['^A']),
        ("3A", ['vA']),
        ("A9", ['^^^A']),
        ("A5", ['^^<A', '<^^A']),
        ("5A", ['vv>A', '>vvA']),
        ("A4", ['^^<<A']),  # cannot go through lower left
        ("4A", ['>>vvA']),  # cannot go through lower left
        ("76", ['>>vA', 'v>>A']),
        ("91", ['<<vvA', 'vv<<A']),
        ("19", ['>>^^A', '^^>>A']),
        ("09", ['>^^^A', '^^^>A']),
    ])
    def test_command_numeric_all_level_1(self, given, expected):
        got = command(given, numeric_keypad)
        expected.sort()
        got.sort()
        self.assertEqual(expected, got)

        for g in got:
            got_back = numeric_keypad.type(given[0], g)
            self.assertEqual(given[1:], got_back)

    @parameterized.expand([
        ("A02A", ['<A^Av>A', '<A^A>vA']),
        ("A029A", ['<A^A>^^AvvvA']),
    ])
    def test_command_numeric_contains_level_1(self, given, expected):
        got = command(given, numeric_keypad)
        expected.sort()
        got.sort()
        for e in expected:
            self.assertIn(e, got)

        for g in got:
            got_back = numeric_keypad.type(given[0], g)
            self.assertEqual(given[1:], got_back)

    @parameterized.expand([
        ("AA", ['A']),
        ("A>", ['vA']),
        (">A", ['^A']),
        ("Av", ['<vA', 'v<A']),
        ("vA", ['>^A', '^>A']),
        ("A<", ['v<<A']),
        ("<A", ['>>^A']),
    ])
    def test_command_arrow_all_level_1(self, given, expected):
        got = command(given, arrow_keypad)
        expected.sort()
        got.sort()
        self.assertEqual(expected, got)

        for g in got:
            got_back = arrow_keypad.type(given[0], g)
            self.assertEqual(given[1:], got_back)

    def test_command_rec_2_029A(self):
        given = 'A029A'

        got = command_rec(given, 2)
        self.assertIn('v<<A>>^A<A>AvA<^AA>A<vAAA>^A', got)

        for g in got:
            got_back = numeric_keypad.type('A', arrow_keypad.type('A', g))
            self.assertEqual(given[1:], got_back)

    def test_command_rec_3_029A(self):
        given = 'A029A'
        got = command_rec(given, 3)
        expected = '<vA<AA>>^AvAA<^A>Av<<A>>^AvA^A<vA>^Av<<A>^A>AAvA^Av<<A>A>^AAAvA<^A>A'

        self.assertIn(expected, got)

        for g in got:
            got_back = numeric_keypad.type('A', arrow_keypad.type('A', arrow_keypad.type('A', g)))
            self.assertEqual(given[1:], got_back)

    @parameterized.expand([
        ("029A", 68),
        ("980A", 60),
        ("179A", 68),
        ("456A", 64),
        ("379A", 64),
    ])
    def test_shortest_2(self, given, expected):
        got = shortest_seq(given, 2)
        self.assertEqual(expected, got)