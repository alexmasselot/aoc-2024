from unittest import TestCase

from d14 import Bot, check_symmetric


class TestDay14(TestCase):
    def test_bot_constructor(self):
        got = Bot('p=0,4 v=3,-3')
        self.assertEqual(0, got.p[0])
        self.assertEqual(4, got.p[1])
        self.assertEqual(3, got.v[0])
        self.assertEqual(-3, got.v[1])

    def test_bot_step(self):
        bot = Bot('p=2,1 v=3,-3')
        dim = 5,7

        bot.step(dim)
        self.assertEqual((0, 5), bot.p)
        bot.step(dim)
        self.assertEqual((3, 2), bot.p)

    def test_check_symmetric(self):
        dim = 5,7
        bots = [
            Bot('p=1,1 v=3,-3'),
            Bot('p=3,1 v=3,-3'),
            Bot('p=2,4 v=3,-3'),
            Bot('p=0,6 v=3,-3'),
            Bot('p=4,6 v=3,-3'),
            ]
        got = check_symmetric(bots, dim)

        self.assertTrue(got)
