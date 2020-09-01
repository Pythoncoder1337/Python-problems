from unittest import TestCase
import reverse


class Test(TestCase):
    def test_reverse(self):
        self.assertEqual([3, 2, 1], reverse.reverse([1, 2, 3]))
        self.assertEqual([], reverse.reverse([]))
        self.assertEqual(["1", "2", "3"], reverse.reverse(["3", "2", "1"]))

    def test_reverse2(self):
        self.assertEqual([3, 2, 1], reverse.reverse([1, 2, 3]))
        self.assertEqual([], reverse.reverse([]))
        self.assertEqual(["1", "2", "3"], reverse.reverse(["3", "2", "1"]))
