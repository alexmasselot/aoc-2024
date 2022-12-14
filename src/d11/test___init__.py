from unittest import TestCase

from d11 import parse_monkey, parse_operation


class Test(TestCase):
    def test_parse_monkey(self):
        given = '''Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3'''

        got = parse_monkey(given)

        self.assertListEqual([79, 98], got.items)
        self.assertEqual(38, got.operation(2))
        self.assertEqual(23, got.divisible_by)
        self.assertEqual(2, got.sent_to_true)
        self.assertEqual(3, got.sent_to_false)

    def test_parse_operation_plus(self):
        given = 'old + 4'

        got = parse_operation(given)

        self.assertEqual(42, got(38))

    def test_parse_operation_mtpy(self):
        given = 'old * 2'

        got = parse_operation(given)

        self.assertEqual(42, got(21))

    def test_parse_operation_square(self):
        given = 'old * old'

        got = parse_operation(given)

        self.assertEqual(225, got(15))

