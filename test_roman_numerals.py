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

if __name__ == '__main__':
    unittest.main()
