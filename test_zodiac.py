from unittest import TestCase

import zodiac


class Test(TestCase):
    def test_zodiac(self):
        self.assertEqual("sagittarius", zodiac.zodiac("december", 1))
        self.assertEqual("cancer", zodiac.zodiac("june", 29))
        self.assertEqual("aries", zodiac.zodiac("march", 31))
        self.assertEqual("aquarius", zodiac.zodiac("february", 3))
        self.assertEqual("aries", zodiac.zodiac("april", 14))
        self.assertIsNone(zodiac.zodiac("december", 70))

    def test_zodiac2(self):
        self.assertEqual("sagittarius", zodiac.zodiac2("december", 1))
        self.assertEqual("cancer", zodiac.zodiac2("june", 29))
        self.assertEqual("aries", zodiac.zodiac2("march", 31))
        self.assertEqual("aquarius", zodiac.zodiac2("february", 3))
        self.assertEqual("aries", zodiac.zodiac2("april", 14))
        self.assertIsNone(zodiac.zodiac2("december", 70))
