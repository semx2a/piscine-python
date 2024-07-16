import unittest
from sos import encrypt


class TestMorseEncryptor(unittest.TestCase):

    def test_encrypt_basic(self):
        self.assertEqual(encrypt("A"), ".-")
        self.assertEqual(encrypt("B"), "-...")
        self.assertEqual(encrypt("C"), "-.-.")
        self.assertEqual(encrypt("1"), ".----")
        self.assertEqual(encrypt(" "), "/")

    def test_encrypt_sentence(self):
        self.assertEqual(encrypt("HELLO WORLD"), ".... . .-.. .-.. --- / .-- \
--- .-. .-.. -..")
        self.assertEqual(encrypt("MORSE CODE"), "-- --- .-. ... . / -.-. \
--- -.. .")

    def test_encrypt_special_characters(self):
        self.assertEqual(encrypt("!"), '')
        self.assertEqual(encrypt(","), '')
        self.assertEqual(encrypt("?"), '')

    def test_encrypt_mixed_case(self):
        self.assertEqual(encrypt("Hello World"), ".... . .-.. .-.. --- / \
.-- --- .-. .-.. -..")
        self.assertEqual(encrypt("mOrSe cOdE"), "-- --- .-. ... . / \
-.-. --- -.. .")

    def test_encrypt_edge_cases(self):
        self.assertEqual(encrypt(""), "")  # Empty string
        self.assertEqual(encrypt("123"), ".---- ..--- ...--")
        self.assertEqual(encrypt("123 ABC"), ".---- ..--- ...-- / \
.- -... -.-.")

    def test_encrypt_unknown_characters(self):
        # Characters not in the Morse code dictionary are ignored
        self.assertEqual(encrypt("hello @world"), ".... . .-.. .-.. --- / \
.-- --- .-. .-.. -..")
        self.assertEqual(encrypt("test!"), "- . ... -")


if __name__ == "__main__":
    unittest.main()
