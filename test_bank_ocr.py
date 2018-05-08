from unittest import TestCase
from BankOCR import bank_ocr


class TestBankOcr(TestCase):

    def test_all_zeroes(self):
        input_num = " _  _  _  _  _  _  _  _  _ " \
                "| || || || || || || || || |" \
                "|_||_||_||_||_||_||_||_||_|"

        expected = "000000000"
        actual = bank_ocr(input_num)

        self.assertEqual(expected, actual)

    def test_all_ones(self):
        input_num = "" \
                "|  |  |  |  |  |  |  |  |" \
                "|  |  |  |  |  |  |  |  |"
        expected = "111111111"
        actual = bank_ocr(input_num)

        self.assertEqual(expected, actual)

    def test_bank_ocr(self):
        self.fail()
