from unittest import TestCase

import chess


class Test(TestCase):
    def test_square_color(self):
        self.assertEqual("black", chess.square_color("b", 2))
        self.assertEqual("black", chess.square_color("a", 1))
        self.assertEqual("white", chess.square_color("a", 2))

    def test_square_color_error(self):
        self.assertIsNone(chess.square_color("i", 1))

    def test_odd(self):
        self.assertTrue(chess.odd(3))
        self.assertTrue(not chess.odd(6))
