import unittest
from fizz_buzz import fizz_buzz


class TestFizzBuzz(unittest.TestCase):

    def test_fizzBuzz_divisible_by_3(self):
        actual = fizz_buzz(6)
        expected = "Fizz"
        self.assertEqual(actual, expected)

    def test_fizzBuzz_divisible_by_5(self):
        actual = fizz_buzz(10)
        expected = "Buzz"
        self.assertEqual(actual, expected)

    def test_fizzBuzz_divisible_by_3_and_5(self):
        actual = fizz_buzz(15)
        expected = "FizzBuzz"
        self.assertEqual(actual, expected)

    def test_fizzBuzz_divisible_by_and_contains_3(self):
        actual = fizz_buzz(33)
        expected = "Fizz"
        self.assertEqual(actual, expected)

    def test_fizzBuzz_contains_3(self):
        actual = fizz_buzz(13)
        expected = "Fizz"
        self.assertEqual(actual, expected)

    def test_fizzBuzz_contains_5(self):
        actual = fizz_buzz(152)
        expected = "Buzz"
        self.assertEqual(actual, expected)

    def test_fizzBuzz_not_divisible_contain_3_or_5(self):
        actual = fizz_buzz(14)
        expected = 14
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
