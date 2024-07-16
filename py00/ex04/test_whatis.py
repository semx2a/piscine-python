import unittest
import sys
from unittest.mock import patch
from whatis import whatis, main


class TestWhatis(unittest.TestCase):

    def test_whatis_even(self):
        self.assertEqual(whatis(2), "I'm Even.")
        self.assertEqual(whatis(0), "I'm Even.")

    def test_whatis_odd(self):
        self.assertEqual(whatis(1), "I'm Odd.")
        self.assertEqual(whatis(-1), "I'm Odd.")

    @patch('sys.exit')
    @patch('builtins.print')
    def test_main_no_arguments(self, mock_print, mock_exit):
        with patch('sys.argv', ['whatis.py']):
            main(sys.argv)
            mock_print.assert_not_called()
            mock_exit.assert_not_called()

    @patch('sys.exit')
    @patch('builtins.print')
    def test_main_single_argument_even(self, mock_print, mock_exit):
        with patch('sys.argv', ['whatis.py', '2']):
            main(sys.argv)
            mock_print.assert_called_with("I'm Even.")
            mock_exit.assert_not_called()

    @patch('sys.exit')
    @patch('builtins.print')
    def test_main_single_argument_odd(self, mock_print, mock_exit):
        with patch('sys.argv', ['whatis.py', '3']):
            main(sys.argv)
            mock_print.assert_called_with("I'm Odd.")
            mock_exit.assert_not_called()

    @patch('builtins.print')
    def test_main_invalid_argument(self, mock_print):
        with patch('sys.argv', ['whatis.py', 'a']):
            with self.assertRaises(SystemExit) as cm:
                main(sys.argv)
            self.assertEqual(cm.exception.code, 1)
            mock_print.assert_called_with(
                'AssertionError: argument is not an integer')

    @patch('builtins.print')
    def test_main_too_many_arguments(self, mock_print):
        with patch('sys.argv', ['whatis.py', '1', '2']):
            with self.assertRaises(SystemExit) as cm:
                main(sys.argv)
            self.assertEqual(cm.exception.code, 1)
            mock_print.assert_called_with(
                'AssertionError: more than one argument provided')


if __name__ == "__main__":
    unittest.main()
