from unittest import TestCase

from d03 import match_item


class Test(TestCase):
    def test_match_item(self):
        got = match_item('vJrwpWtwJgWrhcsFMMfFFhFp')

        self.assertEqual('p', got)
