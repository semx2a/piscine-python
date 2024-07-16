import sys
import unittest
from unittest.mock import patch
from filterstring import is_needle, \
    not_printable, \
    is_greater, \
    parse_string, \
    filterstring, \
    main


class TestFilterString(unittest.TestCase):

    def test_is_needle(self):
        haystack = "hello"
        self.assertTrue(is_needle(haystack)("h"))
        self.assertFalse(is_needle(haystack)("x"))

    def test_not_printable(self):
        self.assertTrue(not_printable()("\x01"))
        self.assertFalse(not_printable()("a"))

    def test_is_greater(self):
        self.assertTrue(is_greater(3)("hello"))
        self.assertFalse(is_greater(5)("hello"))
        self.assertFalse(is_greater(6)("hello"))

    def test_parse_string_valid(self):
        try:
            parse_string("hello world")
        except AssertionError:
            self.fail("parse_string() raised AssertionError unexpectedly")

    def test_parse_string_invalid(self):
        with self.assertRaises(AssertionError):
            parse_string("hello world!")

        with self.assertRaises(AssertionError):
            parse_string("hello\x01world")

    def test_filterstring(self):
        self.assertEqual(filterstring("hello world from unittest", 3),
                         ["hello", "world", "from", "unittest"])
        self.assertEqual(filterstring("hi to you", 1), ["hi", "to", "you"])
        self.assertEqual(filterstring("a bb ccc dddd", 2), ["ccc", "dddd"])

    @patch('builtins.print')
    def test_main(self, mock_print):
        with patch('sys.argv',
                   ['filterstring.py', 'hello world from unittest', '3']):
            main(sys.argv)
            mock_print.assert_called_with(
                ['hello', 'world', 'from', 'unittest'])

        with patch('sys.argv', ['filterstring.py', 'hi to you', '2']):
            main(sys.argv)
            mock_print.assert_called_with(['you'])

    @patch('builtins.print')
    def test_main_invalid_arguments(self, mock_print):
        with patch('sys.argv', ['filterstring.py', 'hello world!', '3']):
            with self.assertRaises(SystemExit) as cm:
                main(sys.argv)
            self.assertEqual(cm.exception.code, 1)
            mock_print.assert_called_with("AssertionError: \
the arguments are bad")

        with patch('sys.argv', ['filterstring.py', 'hello world', 'abc']):
            with self.assertRaises(SystemExit) as cm:
                main(sys.argv)
            self.assertEqual(cm.exception.code, 1)
            mock_print.assert_called_with("AssertionError: \
the arguments are bad")


if __name__ == "__main__":
    unittest.main()
