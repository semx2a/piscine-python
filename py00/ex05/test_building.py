import unittest
from unittest.mock import patch
import sys
from io import StringIO
from building import build_result, parse_text, main


class TestBuilding(unittest.TestCase):

    def test_build_result_valid(self):
        result = build_result((100, 10, 80, 5, 5, 0))
        self.assertEqual(result,
                         "The text contains 100 characters:\n"
                         "10 upper letters\n"
                         "80 lower letters\n"
                         "5 punctuation marks\n"
                         "5 spaces\n"
                         "0 digits")

    def test_build_result_invalid(self):
        with self.assertRaises(AssertionError):
            build_result((1, 2, 3))

    def test_parse_text(self):
        text = "Hello World! 123"
        result = parse_text(text)
        self.assertEqual(result, (16, 2, 8, 1, 2, 3))

    @patch('sys.stdin', new_callable=StringIO)
    @patch('builtins.print')
    def test_main_no_arguments(self, mock_print, mock_stdin):
        mock_stdin.write("Hello World!")
        mock_stdin.seek(0)
        with patch('sys.argv', ['building.py']):
            main(sys.argv)
            mock_print.assert_called_with(
                "The text contains 12 characters:\n"
                "2 upper letters\n"
                "8 lower letters\n"
                "1 punctuation marks\n"
                "1 spaces\n"
                "0 digits"
            )

    @patch('builtins.print')
    def test_main_with_argument(self, mock_print):
        with patch('sys.argv', ['building.py', 'Hello World! 123']):
            main(sys.argv)
            mock_print.assert_called_with(
                "The text contains 16 characters:\n"
                "2 upper letters\n"
                "8 lower letters\n"
                "1 punctuation marks\n"
                "2 spaces\n"
                "3 digits"
            )

    @patch('builtins.print')
    def test_main_too_many_arguments(self, mock_print):
        with patch('sys.argv', ['building.py', 'arg1', 'arg2']):
            with self.assertRaises(SystemExit) as cm:
                main(sys.argv)
            self.assertEqual(cm.exception.code, 1)
            mock_print.assert_called_with(
                "AssertionError: Too many arguments! Usage: python \
building.py \"arg\" (optional)."
            )


if __name__ == "__main__":
    unittest.main()
