from unittest import TestCase
import outliers


class Test(TestCase):
    def test_remove(self):
        self.assertEqual([4, 7], outliers.remove(1, [7, 4, 3, 9]))
        self.assertEqual([99, 100], outliers.remove(1, [101, 100, 3, 99]))
        self.assertEqual([6, 7, 8], outliers.remove(2, [5, 4, 8, 9, 6, 7, 10]))