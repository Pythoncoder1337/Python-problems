from unittest import TestCase

import random

import addition


class Test(TestCase):
    def test_addition(self):
        a = random.randint(0, 100)
        b = random.randint(1, 100)
        c = random.randint(1, 100)
        self.assertEqual(addition.addition(a, b, c), a + b + c)
        print(a, b, c)
        print(a + b, a + c, c + b)
        print(a + b + c)
        print(a + a + a)
        print(b + b + b)
        print(c + c + c)
        print(c + c + b)
        print(c + c + a)
        print(b + b + c)
        print(b + b + a)
        print(a + a + c)
        print(a + a + b)
