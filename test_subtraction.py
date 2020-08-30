from unittest import TestCase

import random

import subtraction


class Test(TestCase):
    def test_subtraction(self):
        a = random.randint(0, 100)
        b = random.randint(0, 100)
        self.assertEqual(subtraction.subtraction(a, b), a - b)
        print("a", "=", a)
        print("b", "=", b)
        if a > b:
            print(a, "-", b, "=", a - b)
        else:
            print(b, "-", a, "=", b - a)
