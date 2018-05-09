import unittest
from roman_numerals import roman_numerals

class TestRomanNumerals(unittest.TestCase):

    def test_one(self):
        expected = "I"
        actual = roman_numerals(1)

        self.assertEqual(expected, actual)

    def test_three(self):
        expected = "III"
        actual = roman_numerals(3)
        self.assertEqual(expected, actual)

    def test_four(self):
        expected = "IV"
        actual = roman_numerals(4)
        self.assertEqual(expected, actual)

    def test_eight(self):
        expected = "VIII"
        actual = roman_numerals(8)
        self.assertEqual(expected, actual)

    def test_nine(self):
        expected = "IX"
        actual = roman_numerals(9)
        self.assertEqual(expected, actual)

    def test_ten(self):
        expected = "X"
        actual = roman_numerals(10)
        self.assertEqual(expected, actual)

    def test_thirty_one(self):
        expected = "XXXI"
        actual = roman_numerals(31)
        self.assertEqual(expected, actual)

    def test_forty(self):
        expected = "XL"
        actual = roman_numerals(40)
        self.assertEqual(expected, actual)

    def test_eighty(self):
        expected = "LXXX"
        actual = roman_numerals(80)
        self.assertEqual(expected, actual)

    def test_ninety(self):
        expected = "XC"
        actual = roman_numerals(90)
        self.assertEqual(expected, actual)

    def test_three_hundred_sixty_nine(self):
        expected = "CCCLXIX"
        actual = roman_numerals(369)
        self.assertEqual(expected, actual)

    def test_four_hundred(self):
        expected = "CD"
        actual = roman_numerals(400)
        self.assertEqual(expected, actual)

    def test_four_hundred_forty_eight(self):
        expected = "CDXLVIII"
        actual = roman_numerals(448)
        self.assertEqual(expected, actual)

    def test_one_thousand_nine_hundred_ninety_eight(self):
        expected = "MCMXCVIII"
        actual = roman_numerals(1998)
        self.assertEqual(expected, actual)

    def two_thousand_seven_hundred_fifty_one(self):
        expected = "MMDCCLI"
        actual = roman_numerals(2751)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
